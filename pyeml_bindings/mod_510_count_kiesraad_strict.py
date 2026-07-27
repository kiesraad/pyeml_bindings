from dataclasses import dataclass, field
from typing import Any, Optional

from pyeml_bindings.emlcore_kiesraad_strict import (
    EventIdentifier,
    ReferendumOptionIdentifier,
)
from pyeml_bindings.kiesraad_eml_extensions import (
    CountingMethod,
    CreationDateTime,
    InitialCast,
    InitialRejectedVotes,
    InitialTotalCounted,
    InitialUncountedVotes,
    InitialValidVotes,
    Phase,
    RejectedVotesType,
    ReportingUnitInvestigations,
    ReportingUnitType,
    SharedLocation,
    UncountedVotesType,
)
from pyeml_bindings.kiesraad_eml_restrictions import (
    AffiliationIdentifierStructureKr,
    CandidateIdentifierStructureKr,
    CandidateStructureKr,
    ContestIdentifierStructureKr,
    ElectionIdentifierStructureKr,
    EmlstructureKr,
    ManagingAuthorityStructureKr,
    ReportingUnitIdentifierStructureKr,
)

__NAMESPACE__ = "urn:oasis:names:tc:evs:schema:eml"


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
    mandatory when candidate number is known at this level.
    """

    candidate_name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    known_as: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    candidate_gender: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    short_code_attribute: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(kw_only=True)
class CandidateStructure510(CandidateStructureKr):
    """
    Only CandidateIdentifier and Gender allowed.
    """

    date_of_birth: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    contact: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    agent: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    date_of_birth_annex: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    national_identification_number: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(kw_only=True)
class Emlstructure510(EmlstructureKr):
    """
    Only TransactionId and IssueDate needed, CanoncalizationMethod added.
    """

    class Meta:
        name = "EMLstructure510"

    issue_date: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    managing_authority: ManagingAuthorityStructureKr = field(
        metadata={
            "name": "ManagingAuthority",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
            "required": True,
        }
    )
    creation_date_time: list[CreationDateTime] = field(
        default_factory=list,
        metadata={
            "name": "CreationDateTime",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/extensions",
            "min_occurs": 2,
            "max_occurs": 3,
        },
    )


@dataclass(kw_only=True)
class ElectionIdentifierStructure510(ElectionIdentifierStructureKr):
    """
    Mandatory ElectionCategory, and some additional Elements.
    """

    nomination_date: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


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
    reporting_unit_type: Optional[ReportingUnitType] = field(
        default=None,
        metadata={
            "name": "ReportingUnitType",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/extensions",
        },
    )
    shared_location: Optional[SharedLocation] = field(
        default=None,
        metadata={
            "name": "SharedLocation",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/extensions",
        },
    )
    selection: list["ReportingUnitVotes.Selection"] = field(
        default_factory=list,
        metadata={
            "name": "Selection",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    initial_cast: Optional[InitialCast] = field(
        default=None,
        metadata={
            "name": "InitialCast",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/extensions",
        },
    )
    cast: int = field(
        metadata={
            "name": "Cast",
            "type": "Element",
            "required": True,
        }
    )
    initial_total_counted: Optional[InitialTotalCounted] = field(
        default=None,
        metadata={
            "name": "InitialTotalCounted",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/extensions",
        },
    )
    total_counted: int = field(
        metadata={
            "name": "TotalCounted",
            "type": "Element",
            "required": True,
        }
    )
    initial_rejected_votes: list[InitialRejectedVotes] = field(
        default_factory=list,
        metadata={
            "name": "InitialRejectedVotes",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/extensions",
            "max_occurs": 2,
        },
    )
    rejected_votes: list[RejectedVotesType] = field(
        default_factory=list,
        metadata={
            "name": "RejectedVotes",
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )
    initial_uncounted_votes: list[InitialUncountedVotes] = field(
        default_factory=list,
        metadata={
            "name": "InitialUncountedVotes",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/extensions",
            "max_occurs": 14,
        },
    )
    uncounted_votes: list[UncountedVotesType] = field(
        default_factory=list,
        metadata={
            "name": "UncountedVotes",
            "type": "Element",
            "max_occurs": 14,
        },
    )
    reporting_unit_investigations: Optional[ReportingUnitInvestigations] = (
        field(
            default=None,
            metadata={
                "name": "ReportingUnitInvestigations",
                "type": "Element",
                "namespace": "http://www.kiesraad.nl/extensions",
            },
        )
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
        affiliation_identifier: Optional[AffiliationIdentifierStructure510] = (
            field(
                default=None,
                metadata={
                    "name": "AffiliationIdentifier",
                    "type": "Element",
                },
            )
        )
        referendum_option_identifier: Optional[ReferendumOptionIdentifier] = (
            field(
                default=None,
                metadata={
                    "name": "ReferendumOptionIdentifier",
                    "type": "Element",
                },
            )
        )
        initial_valid_votes: Optional[InitialValidVotes] = field(
            default=None,
            metadata={
                "name": "InitialValidVotes",
                "type": "Element",
                "namespace": "http://www.kiesraad.nl/extensions",
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
class Count:
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"

    counting_method: Optional[CountingMethod] = field(
        default=None,
        metadata={
            "name": "CountingMethod",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/extensions",
        },
    )
    event_identifier: EventIdentifier = field(
        metadata={
            "name": "EventIdentifier",
            "type": "Element",
            "required": True,
        }
    )
    phase: Optional[Phase] = field(
        default=None,
        metadata={
            "name": "Phase",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/extensions",
        },
    )
    election: "Count.Election" = field(
        metadata={
            "name": "Election",
            "type": "Element",
            "required": True,
        }
    )
    other_element: list[object] = field(
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
            contest: list["Count.Election.Contests.Contest"] = field(
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
                total_votes: "Count.Election.Contests.Contest.TotalVotes" = (
                    field(
                        metadata={
                            "name": "TotalVotes",
                            "type": "Element",
                            "required": True,
                        }
                    )
                )
                reporting_unit_votes: list[ReportingUnitVotes] = field(
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
                    selection: list[
                        "Count.Election.Contests.Contest.TotalVotes.Selection"
                    ] = field(
                        default_factory=list,
                        metadata={
                            "name": "Selection",
                            "type": "Element",
                            "min_occurs": 1,
                        },
                    )
                    initial_cast: Optional[InitialCast] = field(
                        default=None,
                        metadata={
                            "name": "InitialCast",
                            "type": "Element",
                            "namespace": "http://www.kiesraad.nl/extensions",
                        },
                    )
                    cast: int = field(
                        metadata={
                            "name": "Cast",
                            "type": "Element",
                            "required": True,
                        }
                    )
                    initial_total_counted: Optional[InitialTotalCounted] = (
                        field(
                            default=None,
                            metadata={
                                "name": "InitialTotalCounted",
                                "type": "Element",
                                "namespace": "http://www.kiesraad.nl/extensions",
                            },
                        )
                    )
                    total_counted: int = field(
                        metadata={
                            "name": "TotalCounted",
                            "type": "Element",
                            "required": True,
                        }
                    )
                    initial_rejected_votes: list[InitialRejectedVotes] = field(
                        default_factory=list,
                        metadata={
                            "name": "InitialRejectedVotes",
                            "type": "Element",
                            "namespace": "http://www.kiesraad.nl/extensions",
                            "max_occurs": 2,
                        },
                    )
                    rejected_votes: list[RejectedVotesType] = field(
                        default_factory=list,
                        metadata={
                            "name": "RejectedVotes",
                            "type": "Element",
                            "min_occurs": 2,
                            "max_occurs": 2,
                        },
                    )
                    initial_uncounted_votes: list[InitialUncountedVotes] = (
                        field(
                            default_factory=list,
                            metadata={
                                "name": "InitialUncountedVotes",
                                "type": "Element",
                                "namespace": "http://www.kiesraad.nl/extensions",
                                "max_occurs": 14,
                            },
                        )
                    )
                    uncounted_votes: list[UncountedVotesType] = field(
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
                        initial_valid_votes: Optional[InitialValidVotes] = (
                            field(
                                default=None,
                                metadata={
                                    "name": "InitialValidVotes",
                                    "type": "Element",
                                    "namespace": "http://www.kiesraad.nl/extensions",
                                },
                            )
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
