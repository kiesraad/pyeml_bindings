"""This file was generated by xsdata, v23.8, on 2023-10-17 11:34:35

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Any
from xsdata.models.datatype import XmlDateTime
from pyeml_bindings.emlcore_kiesraad_strict import (
    Emlstructure,
    EventIdentifier,
    ReferendumOptionIdentifier,
)
from pyeml_bindings.kiesraad_eml_restrictions import (
    AffiliationIdentifierStructureKr,
    CandidateIdentifierStructureKr,
    CandidateStructureKr,
    ContestIdentifierStructureKr,
    EmlstructureKr,
    ElectionIdentifierStructureKr,
    ManagingAuthorityStructureKr,
    ReportingUnitIdentifierStructureKr,
)

__NAMESPACE__ = "urn:oasis:names:tc:evs:schema:eml"


class RejectedVotesReasonCode(Enum):
    BLANCO = "blanco"
    ONGELDIG = "ongeldig"


class UncountedVotesReasonCode(Enum):
    GELDIGE_STEMPASSEN = "geldige stempassen"
    GELDIGE_VOLMACHTBEWIJZEN = "geldige volmachtbewijzen"
    GELDIGE_KIEZERSPASSEN = "geldige kiezerspassen"
    TOEGELATEN_KIEZERS = "toegelaten kiezers"
    MEER_GETELDE_STEMBILJETTEN = "meer getelde stembiljetten"
    MINDER_GETELDE_STEMBILJETTEN = "minder getelde stembiljetten"
    MEEGENOMEN_STEMBILJETTEN = "meegenomen stembiljetten"
    TE_WEINIG_UITGEREIKTE_STEMBILJETTEN = "te weinig uitgereikte stembiljetten"
    TE_VEEL_UITGEREIKTE_STEMBILJETTEN = "te veel uitgereikte stembiljetten"
    GEEN_BRIEFSTEMBILJETTEN = "geen briefstembiljetten"
    TE_VEEL_BRIEFSTEMBILJETTEN = "te veel briefstembiljetten"
    KWIJTGERAAKTE_STEMBILJETTEN = "kwijtgeraakte stembiljetten"
    GEEN_VERKLARING = "geen verklaring"
    ANDERE_VERKLARING = "andere verklaring"


@dataclass(kw_only=True)
class AffiliationIdentifierStructure510(AffiliationIdentifierStructureKr):
    """
    Mandatory ElectionCategory, and some additional Elements.
    """

    id: str = field(
        metadata={
            "name": "Id",
            "type": "Attribute",
            "required": True,
            "pattern": r"[1-9]\d*",
        }
    )


@dataclass(kw_only=True)
class CandidateIdentifierStructure510(CandidateIdentifierStructureKr):
    """
    Only CandidateName and ShortCode (Element or Attribute) allowed, Id Attribute
    mandatory.
    """

    short_code_attribute: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(kw_only=True)
class CandidateStructure510(CandidateStructureKr):
    """
    Only CandidateIdentifier and Gender allowed.
    """


@dataclass(kw_only=True)
class Emlstructure510(Emlstructure, EmlstructureKr):
    """
    Only TransactionId and IssueDate needed, CanoncalizationMethod added.
    """

    class Meta:
        name = "EMLstructure510"

    managing_authority: ManagingAuthorityStructureKr = field(
        metadata={
            "name": "ManagingAuthority",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
            "required": True,
        }
    )
    creation_date_time: List[XmlDateTime] = field(
        default_factory=list,
        metadata={
            "name": "CreationDateTime",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/extensions",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )


@dataclass(kw_only=True)
class ElectionIdentifierStructure510(ElectionIdentifierStructureKr):
    """
    Mandatory ElectionCategory, and some additional Elements.
    """


@dataclass(kw_only=True)
class ReportingUnitVotes:
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"

    reporting_unit_identifier: ReportingUnitIdentifierStructureKr = field(
        metadata={
            "name": "ReportingUnitIdentifier",
            "type": "Element",
            "required": True,
        }
    )
    selection: List["ReportingUnitVotes.Selection"] = field(
        default_factory=list,
        metadata={
            "name": "Selection",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    cast: int = field(
        metadata={
            "name": "Cast",
            "type": "Element",
            "required": True,
        }
    )
    total_counted: int = field(
        metadata={
            "name": "TotalCounted",
            "type": "Element",
            "required": True,
        }
    )
    rejected_votes: List["ReportingUnitVotes.RejectedVotes"] = field(
        default_factory=list,
        metadata={
            "name": "RejectedVotes",
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )
    uncounted_votes: List["ReportingUnitVotes.UncountedVotes"] = field(
        default_factory=list,
        metadata={
            "name": "UncountedVotes",
            "type": "Element",
            "max_occurs": 14,
        },
    )

    @dataclass(kw_only=True)
    class Selection:
        candidate: Optional[CandidateStructure510] = field(
            default=None,
            metadata={
                "name": "Candidate",
                "type": "Element",
            },
        )
        affiliation_identifier: Optional[AffiliationIdentifierStructure510] = field(
            default=None,
            metadata={
                "name": "AffiliationIdentifier",
                "type": "Element",
            },
        )
        referendum_option_identifier: Optional[ReferendumOptionIdentifier] = field(
            default=None,
            metadata={
                "name": "ReferendumOptionIdentifier",
                "type": "Element",
            },
        )
        valid_votes: int = field(
            metadata={
                "name": "ValidVotes",
                "type": "Element",
                "required": True,
            }
        )
        value: Optional[int] = field(
            default=None,
            metadata={
                "name": "Value",
                "type": "Attribute",
            },
        )
        category: Optional[str] = field(
            default=None,
            metadata={
                "name": "Category",
                "type": "Attribute",
            },
        )

    @dataclass(kw_only=True)
    class RejectedVotes:
        value: int = field(
            metadata={
                "required": True,
            }
        )
        reason: Optional[str] = field(
            default=None,
            metadata={
                "name": "Reason",
                "type": "Attribute",
            },
        )
        reason_code: RejectedVotesReasonCode = field(
            metadata={
                "name": "ReasonCode",
                "type": "Attribute",
                "required": True,
            }
        )
        vote_type: Optional[str] = field(
            default=None,
            metadata={
                "name": "VoteType",
                "type": "Attribute",
            },
        )

    @dataclass(kw_only=True)
    class UncountedVotes:
        value: int = field(
            metadata={
                "required": True,
            }
        )
        reason: Optional[str] = field(
            default=None,
            metadata={
                "name": "Reason",
                "type": "Attribute",
            },
        )
        reason_code: UncountedVotesReasonCode = field(
            metadata={
                "name": "ReasonCode",
                "type": "Attribute",
                "required": True,
            }
        )
        vote_type: Optional[str] = field(
            default=None,
            metadata={
                "name": "VoteType",
                "type": "Attribute",
            },
        )


@dataclass(kw_only=True)
class Count:
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"

    event_identifier: EventIdentifier = field(
        metadata={
            "name": "EventIdentifier",
            "type": "Element",
            "required": True,
        }
    )
    election: "Count.Election" = field(
        metadata={
            "name": "Election",
            "type": "Element",
            "required": True,
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )

    @dataclass(kw_only=True)
    class Election:
        election_identifier: ElectionIdentifierStructure510 = field(
            metadata={
                "name": "ElectionIdentifier",
                "type": "Element",
                "required": True,
            }
        )
        contests: "Count.Election.Contests" = field(
            metadata={
                "name": "Contests",
                "type": "Element",
                "required": True,
            }
        )

        @dataclass(kw_only=True)
        class Contests:
            contest: List["Count.Election.Contests.Contest"] = field(
                default_factory=list,
                metadata={
                    "name": "Contest",
                    "type": "Element",
                    "min_occurs": 1,
                },
            )

            @dataclass(kw_only=True)
            class Contest:
                contest_identifier: ContestIdentifierStructureKr = field(
                    metadata={
                        "name": "ContestIdentifier",
                        "type": "Element",
                        "required": True,
                    }
                )
                total_votes: "Count.Election.Contests.Contest.TotalVotes" = field(
                    metadata={
                        "name": "TotalVotes",
                        "type": "Element",
                        "required": True,
                    }
                )
                reporting_unit_votes: List[ReportingUnitVotes] = field(
                    default_factory=list,
                    metadata={
                        "name": "ReportingUnitVotes",
                        "type": "Element",
                        "min_occurs": 1,
                        "sequence": 1,
                    },
                )

                @dataclass(kw_only=True)
                class TotalVotes:
                    selection: List[
                        "Count.Election.Contests.Contest.TotalVotes.Selection"
                    ] = field(
                        default_factory=list,
                        metadata={
                            "name": "Selection",
                            "type": "Element",
                            "min_occurs": 1,
                        },
                    )
                    cast: int = field(
                        metadata={
                            "name": "Cast",
                            "type": "Element",
                            "required": True,
                        }
                    )
                    total_counted: int = field(
                        metadata={
                            "name": "TotalCounted",
                            "type": "Element",
                            "required": True,
                        }
                    )
                    rejected_votes: List[
                        "Count.Election.Contests.Contest.TotalVotes.RejectedVotes"
                    ] = field(
                        default_factory=list,
                        metadata={
                            "name": "RejectedVotes",
                            "type": "Element",
                            "min_occurs": 2,
                            "max_occurs": 2,
                        },
                    )
                    uncounted_votes: List[
                        "Count.Election.Contests.Contest.TotalVotes.UncountedVotes"
                    ] = field(
                        default_factory=list,
                        metadata={
                            "name": "UncountedVotes",
                            "type": "Element",
                            "max_occurs": 14,
                        },
                    )

                    @dataclass(kw_only=True)
                    class Selection:
                        candidate: Optional[CandidateStructure510] = field(
                            default=None,
                            metadata={
                                "name": "Candidate",
                                "type": "Element",
                            },
                        )
                        affiliation_identifier: Optional[
                            AffiliationIdentifierStructure510
                        ] = field(
                            default=None,
                            metadata={
                                "name": "AffiliationIdentifier",
                                "type": "Element",
                            },
                        )
                        referendum_option_identifier: Optional[
                            ReferendumOptionIdentifier
                        ] = field(
                            default=None,
                            metadata={
                                "name": "ReferendumOptionIdentifier",
                                "type": "Element",
                            },
                        )
                        valid_votes: int = field(
                            metadata={
                                "name": "ValidVotes",
                                "type": "Element",
                                "required": True,
                            }
                        )
                        value: Optional[int] = field(
                            default=None,
                            metadata={
                                "name": "Value",
                                "type": "Attribute",
                            },
                        )
                        category: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "Category",
                                "type": "Attribute",
                            },
                        )

                    @dataclass(kw_only=True)
                    class RejectedVotes:
                        value: int = field(
                            metadata={
                                "required": True,
                            }
                        )
                        reason: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "Reason",
                                "type": "Attribute",
                            },
                        )
                        reason_code: RejectedVotesReasonCode = field(
                            metadata={
                                "name": "ReasonCode",
                                "type": "Attribute",
                                "required": True,
                            }
                        )
                        vote_type: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "VoteType",
                                "type": "Attribute",
                            },
                        )

                    @dataclass(kw_only=True)
                    class UncountedVotes:
                        value: int = field(
                            metadata={
                                "required": True,
                            }
                        )
                        reason: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "Reason",
                                "type": "Attribute",
                            },
                        )
                        reason_code: UncountedVotesReasonCode = field(
                            metadata={
                                "name": "ReasonCode",
                                "type": "Attribute",
                                "required": True,
                            }
                        )
                        vote_type: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "VoteType",
                                "type": "Attribute",
                            },
                        )


@dataclass(kw_only=True)
class Eml(Emlstructure510):
    class Meta:
        name = "EML"
        namespace = "urn:oasis:names:tc:evs:schema:eml"

    count: Count = field(
        metadata={
            "name": "Count",
            "type": "Element",
            "required": True,
        }
    )
