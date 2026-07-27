from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any

from xsdata.models.datatype import XmlDate, XmlDateTime

from pyeml_bindings.emlexternals_kiesraad_strict import PersonNameStructure
from pyeml_bindings.kiesraad_eml_extensions import (
    AffiliationType,
    CreationDateTime,
    ElectionDate,
    ListData,
    LivingAddress,
    NominationDate,
    Schema,
)
from pyeml_bindings.kiesraad_eml_restrictions import (
    AffiliationIdentifierStructureKr,
    CandidateIdentifierStructureKr,
    CandidateStructureKr,
    ContactDetailsStructureKr,
    ContestIdentifierStructureKr,
    ElectionIdentifierStructureKr,
    EmlstructureKr,
    QualifyingAddressStructureKr,
)

__NAMESPACE__ = "urn:oasis:names:tc:evs:schema:eml"


class ProposerStructureRestrictedJobTitle(Enum):
    INLEVERAAR = "inleveraar"
    PLAATSVERVANGER_VAN_DE_INLEVERAAR = "plaatsvervanger van de inleveraar"
    GEMACHTIGDE_VOOR_HET_AANGAAN_VAN_LIJSTENCOMBINATIES = (
        "gemachtigde voor het aangaan van lijstencombinaties"
    )
    PLAATSVERVANGER_VOOR_HET_AANGAAN_VAN_LIJSTENCOMBINATIES = (
        "plaatsvervanger voor het aangaan van lijstencombinaties"
    )


@dataclass(kw_only=True)
class AffiliationIdentifierStructure210(AffiliationIdentifierStructureKr):
    """
    Id prohibited.
    """

    id: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(kw_only=True)
class CandidateIdentifierStructure210(CandidateIdentifierStructureKr):
    """
    only empty content allowed, Id Attribute mandatory.
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
            "pattern": r"[1-9]\d*",
        }
    )


@dataclass(kw_only=True)
class CandidateStructure210(CandidateStructureKr):
    """
    only CandidateIdentifier, CandidateFullName, DateOfBirth, Gender,
    QualifyingAddress, and Agent allowed.
    """

    candidate_full_name: PersonNameStructure = field(
        metadata={
            "name": "CandidateFullName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        }
    )
    qualifying_address: QualifyingAddressStructureKr = field(
        metadata={
            "name": "QualifyingAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        }
    )


@dataclass(kw_only=True)
class ContestIdentifierStructure210(ContestIdentifierStructureKr):
    """
    mandatory ContestName.
    """

    contest_name: str = field(
        metadata={
            "name": "ContestName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        }
    )


@dataclass(kw_only=True)
class Emlstructure210(EmlstructureKr):
    """
    only TransactionId and IssueDate needed, CanoncalizationMethod added.
    """

    class Meta:
        name = "EMLstructure210"

    issue_date: XmlDate | XmlDateTime = field(
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        }
    )
    schema: list[Schema] = field(
        default_factory=list,
        metadata={
            "name": "Schema",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/extensions",
            "min_occurs": 2,
            "max_occurs": 3,
        },
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
        default="210",
        metadata={
            "name": "Id",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ElectionIdentifierStructure210(ElectionIdentifierStructureKr):
    """
    mandatory ElectionCategory, and some additional Elements.
    """

    election_date: list[ElectionDate] = field(
        default_factory=list,
        metadata={
            "name": "ElectionDate",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/extensions",
            "min_occurs": 2,
            "max_occurs": 4,
        },
    )
    nomination_date: list[NominationDate] = field(
        default_factory=list,
        metadata={
            "name": "NominationDate",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/extensions",
            "min_occurs": 2,
            "max_occurs": 4,
        },
    )


@dataclass(kw_only=True)
class ProposerStructureRestricted:
    """
    due to the anonymous definition of the original Id, a removal by
    restriction was necessary.
    """

    name: PersonNameStructure = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        }
    )
    contact: ContactDetailsStructureKr = field(
        metadata={
            "name": "Contact",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        }
    )
    job_title: ProposerStructureRestrictedJobTitle = field(
        metadata={
            "name": "JobTitle",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        }
    )


@dataclass(kw_only=True)
class AffiliationStructure210:
    """
    Type restricted to 3 defined values.
    """

    affiliation_identifier: AffiliationIdentifierStructure210 = field(
        metadata={
            "name": "AffiliationIdentifier",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        }
    )
    type_value: AffiliationType = field(
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        }
    )
    list_data: None | ListData = field(
        default=None,
        metadata={
            "name": "ListData",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/extensions",
        },
    )
    kiesraad_nl_reportgenerator_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://www.kiesraad.nl/reportgenerator",
        },
    )


@dataclass(kw_only=True)
class ProposerStructureKr(ProposerStructureRestricted):
    """
    due to the anonymous definition of the original Id, a repeated
    definition by extension was necessary.

    :ivar id: mandatory if it is a deputy
    :ivar living_address:
    """

    class Meta:
        name = "ProposerStructureKR"

    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    living_address: None | LivingAddress = field(
        default=None,
        metadata={
            "name": "LivingAddress",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/extensions",
        },
    )


@dataclass(kw_only=True)
class Nomination:
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"

    election_identifier: ElectionIdentifierStructure210 = field(
        metadata={
            "name": "ElectionIdentifier",
            "type": "Element",
        }
    )
    contest_identifier: ContestIdentifierStructure210 = field(
        metadata={
            "name": "ContestIdentifier",
            "type": "Element",
        }
    )
    affiliation: Nomination.Affiliation = field(
        metadata={
            "name": "Affiliation",
            "type": "Element",
        }
    )
    nominate: Nomination.Nominate = field(
        metadata={
            "name": "Nominate",
            "type": "Element",
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
    class Affiliation(AffiliationStructure210):
        candidate: list[CandidateStructure210] = field(
            default_factory=list,
            metadata={
                "name": "Candidate",
                "type": "Element",
                "min_occurs": 1,
            },
        )

    @dataclass(kw_only=True)
    class Nominate:
        proposer: list[ProposerStructureKr] = field(
            default_factory=list,
            metadata={
                "name": "Proposer",
                "type": "Element",
                "min_occurs": 2,
            },
        )


@dataclass(kw_only=True)
class Eml(Emlstructure210):
    class Meta:
        name = "EML"
        namespace = "urn:oasis:names:tc:evs:schema:eml"

    nomination: Nomination = field(
        metadata={
            "name": "Nomination",
            "type": "Element",
            "required": True,
        }
    )
