from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Optional, Union

from xsdata.models.datatype import XmlDate, XmlDateTime

from pyeml_bindings.emlexternals_kiesraad_strict import PersonNameStructure
from pyeml_bindings.kiesraad_eml_extensions import (
    AffiliationType,
    CreationDateTime,
    ListData,
    LivingAddress,
    NominationDate,
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
    Only empty content allowed, Id Attribute mandatory.
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
class CandidateStructure210(CandidateStructureKr):
    """
    Only CandidateIdentifier, CandidateFullName, DateOfBirth, Gender,
    QualifyingAddress, and Agent allowed.
    """

    candidate_full_name: PersonNameStructure = field(
        metadata={
            "name": "CandidateFullName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
            "required": True,
        }
    )
    qualifying_address: QualifyingAddressStructureKr = field(
        metadata={
            "name": "QualifyingAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ContestIdentifierStructure210(ContestIdentifierStructureKr):
    """
    Mandatory ContestName.
    """

    contest_name: str = field(
        metadata={
            "name": "ContestName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Emlstructure210(EmlstructureKr):
    """
    Only TransactionId and IssueDate needed, CanoncalizationMethod added.
    """

    class Meta:
        name = "EMLstructure210"

    issue_date: Union[XmlDate, XmlDateTime] = field(
        metadata={
            "name": "IssueDate",
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
    Mandatory ElectionCategory, and some additional Elements.
    """

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
    Due to the anonymous definition of the original Id, a removal by restriction
    was necessary.
    """

    name: PersonNameStructure = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
            "required": True,
        }
    )
    contact: ContactDetailsStructureKr = field(
        metadata={
            "name": "Contact",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
            "required": True,
        }
    )
    job_title: ProposerStructureRestrictedJobTitle = field(
        metadata={
            "name": "JobTitle",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
            "required": True,
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
            "required": True,
        }
    )
    type_value: AffiliationType = field(
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
            "required": True,
        }
    )
    list_data: list[ListData] = field(
        default_factory=list,
        metadata={
            "name": "ListData",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/extensions",
            "max_occurs": 2,
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
    Due to the anonymous definition of the original Id, a repeated definition by
    extension was necessary.

    :ivar id: mandatory if it is a deputy
    :ivar living_address:
    """

    class Meta:
        name = "ProposerStructureKR"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    living_address: Optional[LivingAddress] = field(
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
            "required": True,
        }
    )
    contest_identifier: ContestIdentifierStructure210 = field(
        metadata={
            "name": "ContestIdentifier",
            "type": "Element",
            "required": True,
        }
    )
    affiliation: "Nomination.Affiliation" = field(
        metadata={
            "name": "Affiliation",
            "type": "Element",
            "required": True,
        }
    )
    nominate: "Nomination.Nominate" = field(
        metadata={
            "name": "Nominate",
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
