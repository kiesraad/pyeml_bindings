"""This file was generated by xsdata, v23.8, on 2023-10-17 11:34:35

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from pyeml_bindings.emlcore_kiesraad_strict import Emlstructure, YesNoType
from pyeml_bindings.emlexternals_kiesraad_strict import PersonNameStructure
from pyeml_bindings.kiesraad_eml_restrictions import (
    AffiliationIdentifierStructureKr,
    CandidateIdentifierStructureKr,
    CandidateStructureKr,
    ContestIdentifierStructureKr,
    EmlstructureKr,
    ElectionIdentifierStructureKr,
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
    """
    Id Attribute mandatory.
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
class CandidateStructure520(CandidateStructureKr):
    """Only CandidateIdentifier.

    Gender, and QualifyingAddress allowed, the latter made mandatory
    """

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
class Emlstructure520(Emlstructure, EmlstructureKr):
    """
    Only TransactionId and IssueDate needed, CanoncalizationMethod added.
    """

    class Meta:
        name = "EMLstructure520"

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
    other_element: List[object] = field(
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
        contest: List["Result.Election.Contest"] = field(
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
            selection: List["Result.Election.Contest.Selection"] = field(
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
                ranking: Optional[SelectionRanking] = field(
                    default=None,
                    metadata={
                        "name": "Ranking",
                        "type": "Element",
                    },
                )
                elected: List[YesNoType] = field(
                    default_factory=list,
                    metadata={
                        "name": "Elected",
                        "type": "Element",
                        "min_occurs": 2,
                        "max_occurs": 2,
                        "sequence": 1,
                    },
                )


@dataclass(kw_only=True)
class Eml(Emlstructure520):
    class Meta:
        name = "EML"
        namespace = "urn:oasis:names:tc:evs:schema:eml"

    result: Result = field(
        metadata={
            "name": "Result",
            "type": "Element",
            "required": True,
        }
    )
