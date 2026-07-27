from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Optional

from pyeml_bindings.emlcore_kiesraad_strict import YesNoType
from pyeml_bindings.emlexternals_kiesraad_strict import PersonNameStructure
from pyeml_bindings.kiesraad_eml_extensions import CreationDateTime
from pyeml_bindings.kiesraad_eml_restrictions import (
    AffiliationIdentifierStructureKr,
    CandidateIdentifierStructureKr,
    CandidateStructureKr,
    ContestIdentifierStructureKr,
    ElectionIdentifierStructureKr,
    EmlstructureKr,
    ManagingAuthorityStructureKr,
    MinimalQualifyingAddressStructureKr,
)

__NAMESPACE__ = "urn:oasis:names:tc:evs:schema:eml"


class SelectionRanking(Enum):
    VALUE_1 = 1
    VALUE_2 = 2


@dataclass(kw_only=True)
class AffiliationIdentifierStructure520(AffiliationIdentifierStructureKr):
    """
    Id mandatory.
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
class CandidateIdentifierStructure520(CandidateIdentifierStructureKr):
    """Id Attribute mandatory.

    Does not refer to candidate number but the order in which the
    candidates are elected
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
    short_code: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    id: str = field(
        metadata={
            "name": "Id",
            "type": "Attribute",
            "required": True,
            "pattern": r"[1-9]\d*",
        }
    )


@dataclass(kw_only=True)
class CandidateStructure520(CandidateStructureKr):
    """Only CandidateIdentifier.

    Gender, and QualifyingAddress allowed, the latter made mandatory
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
    candidate_full_name: PersonNameStructure = field(
        metadata={
            "name": "CandidateFullName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
            "required": True,
        }
    )
    qualifying_address: MinimalQualifyingAddressStructureKr = field(
        metadata={
            "name": "QualifyingAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Emlstructure520(EmlstructureKr):
    """
    Only TransactionId and IssueDate needed, CanoncalizationMethod added.
    """

    class Meta:
        name = "EMLstructure520"

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
    id: str = field(
        init=False,
        default="520",
        metadata={
            "name": "Id",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ElectionIdentifierStructure520(ElectionIdentifierStructureKr):
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
class Result:
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"

    election: "Result.Election" = field(
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
        election_identifier: ElectionIdentifierStructure520 = field(
            metadata={
                "name": "ElectionIdentifier",
                "type": "Element",
                "required": True,
            }
        )
        contest: list["Result.Election.Contest"] = field(
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
            selection: list["Result.Election.Contest.Selection"] = field(
                default_factory=list,
                metadata={
                    "name": "Selection",
                    "type": "Element",
                    "min_occurs": 1,
                },
            )

            @dataclass(kw_only=True)
            class Selection:
                candidate: Optional[CandidateStructure520] = field(
                    default=None,
                    metadata={
                        "name": "Candidate",
                        "type": "Element",
                    },
                )
                affiliation_identifier: Optional[
                    AffiliationIdentifierStructure520
                ] = field(
                    default=None,
                    metadata={
                        "name": "AffiliationIdentifier",
                        "type": "Element",
                    },
                )
                votes: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "Votes",
                        "type": "Element",
                    },
                )
                ranking: SelectionRanking = field(
                    metadata={
                        "name": "Ranking",
                        "type": "Element",
                        "required": True,
                    }
                )
                elected: list[YesNoType] = field(
                    default_factory=list,
                    metadata={
                        "name": "Elected",
                        "type": "Element",
                        "min_occurs": 2,
                        "max_occurs": 2,
                        "sequence": 1,
                    },
                )
