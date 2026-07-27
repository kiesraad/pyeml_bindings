from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Optional, Union

from xsdata.models.datatype import XmlDate, XmlDateTime

from pyeml_bindings.emlcore_kiesraad_strict import (
    AffiliationIdentifierStructure,
    AgentIdentifier,
    AuthorityIdentifierStructure,
    CandidateIdentifierStructure,
    ContestIdentifierStructure,
    Gender,
    ReportingUnitIdentifierStructure,
    TransactionId,
)
from pyeml_bindings.emlexternals_kiesraad_strict import (
    AuthorityAddressStructure,
    PersonNameStructure,
)
from pyeml_bindings.external.xmldsig_core_schema import CanonicalizationMethod
from pyeml_bindings.kiesraad_eml_extensions import (
    AffiliationType,
    CreatedByAuthority,
    CreationDateTime,
    DateOfBirthAnnex,
    ElectionCategoryType,
    ElectionDate,
    ElectionDomain,
    ElectionSubcategory,
    GenderAnnex,
    ListData,
    LivingAddress,
    NationalIdentificationNumber,
    NominationDate,
    Schema,
)
from pyeml_bindings.x_al_kiesraad_strict import (
    AddressDetails,
    GenericCountryType,
    GenericLocalityType,
)

__NAMESPACE__ = "urn:oasis:names:tc:evs:schema:eml"


class AgentStructureKrRole(Enum):
    H10 = "H10"
    H10A = "H10a"


@dataclass(kw_only=True)
class AddressStructureRestrictedKr(AddressDetails):
    """
    Due to deficiencies in XML schema, everyting except attributes is removed from
    the original type.

    :ivar postal_service_elements: Postal authorities use specific
        postal service data to expedient delivery of mail
    :ivar address:
    :ivar address_lines: Container for Address lines
    :ivar country: Specification of a country
    :ivar administrative_area:
    :ivar locality:
    :ivar thoroughfare:
    :ivar other_element:
    :ivar other_attributes:
    """

    class Meta:
        name = "AddressStructureRestrictedKR"

    postal_service_elements: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    address: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    address_lines: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    country: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    administrative_area: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    locality: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    thoroughfare: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    other_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    other_attributes: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(kw_only=True)
class AffiliationIdentifierStructureKr(AffiliationIdentifierStructure):
    """
    Only attribute optionally used is Id.
    """

    class Meta:
        name = "AffiliationIdentifierStructureKR"


@dataclass(kw_only=True)
class AuthorityIdentifierStructureKr(AuthorityIdentifierStructure):
    """
    Id Attribute mandatory, content restricted.
    """

    class Meta:
        name = "AuthorityIdentifierStructureKR"

    id: str = field(
        metadata={
            "name": "Id",
            "type": "Attribute",
            "required": True,
            "pattern": r"CSB|((HSB|SB)\d+)|(\d{4})",
        }
    )


@dataclass(kw_only=True)
class CandidateIdentifierStructureKr(CandidateIdentifierStructure):
    """
    Only CandidateName and ShortCode (Element or Attribute) allowed, Id Attribute
    mandatory.
    """

    class Meta:
        name = "CandidateIdentifierStructureKR"

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


@dataclass(kw_only=True)
class ContestIdentifierStructureKr(ContestIdentifierStructure):
    """
    Id Attribute mandatory, content restricted.
    """

    class Meta:
        name = "ContestIdentifierStructureKR"


@dataclass(kw_only=True)
class ElectionIdentifierStructureKr:
    """
    Mandatory ElectionCategory, and some additional Elements.
    """

    class Meta:
        name = "ElectionIdentifierStructureKR"

    election_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ElectionName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    election_category: ElectionCategoryType = field(
        metadata={
            "name": "ElectionCategory",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
            "required": True,
        }
    )
    election_subcategory: list[ElectionSubcategory] = field(
        default_factory=list,
        metadata={
            "name": "ElectionSubcategory",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/extensions",
            "max_occurs": 4,
        },
    )
    election_domain: list[ElectionDomain] = field(
        default_factory=list,
        metadata={
            "name": "ElectionDomain",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/extensions",
            "max_occurs": 4,
        },
    )
    election_date: list[ElectionDate] = field(
        default_factory=list,
        metadata={
            "name": "ElectionDate",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/extensions",
            "max_occurs": 4,
        },
    )
    nomination_date: list[NominationDate] = field(
        default_factory=list,
        metadata={
            "name": "NominationDate",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/extensions",
            "max_occurs": 4,
        },
    )
    id: str = field(
        metadata={
            "name": "Id",
            "type": "Attribute",
            "required": True,
            "pattern": r"(EP|EK|TK|GR|BC|GC|ER|PS|AB|NR|PR|LR|IR|KC)2\d\d\d(\d\d\d\d)?(_[\w_-]*)?",
        }
    )


@dataclass(kw_only=True)
class ReportingUnitIdentifierStructureKr(ReportingUnitIdentifierStructure):
    """
    Id Attribute mandatory, content restricted.
    """

    class Meta:
        name = "ReportingUnitIdentifierStructureKR"

    id: str = field(
        metadata={
            "name": "Id",
            "type": "Attribute",
            "required": True,
            "pattern": r"(HSB\d+)|((HSB\d+::)?\d{4})|(((HSB\d+::)?\d{4}::)?SB\d+)|(HSB\d+::SB\d+)",
        }
    )


@dataclass(kw_only=True)
class AffiliationStructureKr:
    """
    Only mandatory elements allowed, Type restricted to 3 defined values.
    """

    class Meta:
        name = "AffiliationStructureKR"

    affiliation_identifier: AffiliationIdentifierStructureKr = field(
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
class GenericMailingAddressStructureKr(AddressStructureRestrictedKr):
    """
    Due to deficiencies in XML schema, the result type is built by extension.
    """

    class Meta:
        name = "GenericMailingAddressStructureKR"

    locality: Optional[GenericLocalityType] = field(
        default=None,
        metadata={
            "name": "Locality",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        },
    )
    country: Optional[GenericCountryType] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        },
    )


@dataclass(kw_only=True)
class GenericQualifyingAddressStructureKr(AddressStructureRestrictedKr):
    """
    Due to deficiencies in XML schema, the result type is built by extension.
    """

    class Meta:
        name = "GenericQualifyingAddressStructureKR"

    locality: Optional[GenericLocalityType] = field(
        default=None,
        metadata={
            "name": "Locality",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        },
    )
    country: Optional[GenericCountryType] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        },
    )


@dataclass(kw_only=True)
class ManagingAuthorityStructureKr:
    """
    Only AuthorityIdentifier and AuthorityAddress allowed, as well as the new
    Element CreatedByAuthority.
    """

    class Meta:
        name = "ManagingAuthorityStructureKR"

    authority_identifier: AuthorityIdentifierStructureKr = field(
        metadata={
            "name": "AuthorityIdentifier",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
            "required": True,
        }
    )
    authority_address: AuthorityAddressStructure = field(
        metadata={
            "name": "AuthorityAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
            "required": True,
        }
    )
    created_by_authority: Optional[CreatedByAuthority] = field(
        default=None,
        metadata={
            "name": "CreatedByAuthority",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/extensions",
        },
    )


@dataclass(kw_only=True)
class ContactDetailsStructureKr:
    """only MailingAddress allowed - and mandatory"""

    class Meta:
        name = "ContactDetailsStructureKR"

    mailing_address: GenericMailingAddressStructureKr = field(
        metadata={
            "name": "MailingAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class EmlstructureKr:
    """
    Only TransactionId, ManagingAuthority, and IssueDate needed,
    CanoncalizationMethod added.
    """

    class Meta:
        name = "EMLstructureKR"

    transaction_id: TransactionId = field(
        metadata={
            "name": "TransactionId",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
            "required": True,
        }
    )
    managing_authority: Optional[ManagingAuthorityStructureKr] = field(
        default=None,
        metadata={
            "name": "ManagingAuthority",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    issue_date: Optional[Union[XmlDate, XmlDateTime]] = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    schema: list[Schema] = field(
        default_factory=list,
        metadata={
            "name": "Schema",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/extensions",
            "max_occurs": 3,
        },
    )
    creation_date_time: list[CreationDateTime] = field(
        default_factory=list,
        metadata={
            "name": "CreationDateTime",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/extensions",
            "max_occurs": 3,
        },
    )
    canonicalization_method: list[CanonicalizationMethod] = field(
        default_factory=list,
        metadata={
            "name": "CanonicalizationMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "max_occurs": 3,
        },
    )
    id: str = field(
        metadata={
            "name": "Id",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class MailingAddressStructureKr(GenericMailingAddressStructureKr):
    """
    Full address.

    :ivar postal_service_elements: Postal authorities use specific
        postal service data to expedient delivery of mail
    :ivar address:
    :ivar address_lines: Container for Address lines
    :ivar administrative_area:
    :ivar thoroughfare:
    :ivar other_element:
    :ivar other_attributes:
    """

    class Meta:
        name = "MailingAddressStructureKR"

    postal_service_elements: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    address: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    address_lines: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    administrative_area: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    thoroughfare: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    other_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    other_attributes: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(kw_only=True)
class MinimalQualifyingAddressStructureKr(GenericQualifyingAddressStructureKr):
    """
    Minimal address.

    :ivar postal_service_elements: Postal authorities use specific
        postal service data to expedient delivery of mail
    :ivar address:
    :ivar address_lines: Container for Address lines
    :ivar administrative_area:
    :ivar thoroughfare:
    :ivar other_element:
    :ivar other_attributes:
    """

    class Meta:
        name = "MinimalQualifyingAddressStructureKR"

    postal_service_elements: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    address: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    address_lines: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    administrative_area: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    thoroughfare: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    other_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    other_attributes: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(kw_only=True)
class QualifyingAddressStructureKr(GenericQualifyingAddressStructureKr):
    """
    Full address.

    :ivar postal_service_elements: Postal authorities use specific
        postal service data to expedient delivery of mail
    :ivar address:
    :ivar address_lines: Container for Address lines
    :ivar administrative_area:
    :ivar thoroughfare:
    :ivar other_element:
    :ivar other_attributes:
    """

    class Meta:
        name = "QualifyingAddressStructureKR"

    postal_service_elements: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    address: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    address_lines: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    administrative_area: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    thoroughfare: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    other_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    other_attributes: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(kw_only=True)
class AgentStructureKr:
    """only AgentIdentifier, Contact and ##other allowed - and mandatory"""

    class Meta:
        name = "AgentStructureKR"

    agent_identifier: AgentIdentifier = field(
        metadata={
            "name": "AgentIdentifier",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
            "required": True,
        }
    )
    contact: Optional[ContactDetailsStructureKr] = field(
        default=None,
        metadata={
            "name": "Contact",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    living_address: LivingAddress = field(
        metadata={
            "name": "LivingAddress",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/extensions",
            "required": True,
        }
    )
    role: Optional[AgentStructureKrRole] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class CandidateStructureKr:
    """
    Only CandidateIdentifier, CandidateFullName, Gender,  QualifyingAddress,
    Contact, Agent, kr:DateOfBirthAnnex and kr:NationalIdentificationNumber
    allowed; re-defined without inheritance because of inflexible rules of
    restriction.
    """

    class Meta:
        name = "CandidateStructureKR"

    candidate_identifier: CandidateIdentifierStructureKr = field(
        metadata={
            "name": "CandidateIdentifier",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
            "required": True,
        }
    )
    candidate_full_name: Optional[PersonNameStructure] = field(
        default=None,
        metadata={
            "name": "CandidateFullName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    date_of_birth: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DateOfBirth",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    gender: Optional[Gender] = field(
        default=None,
        metadata={
            "name": "Gender",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    gender_annex: Optional[GenderAnnex] = field(
        default=None,
        metadata={
            "name": "GenderAnnex",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/extensions",
        },
    )
    qualifying_address: Optional[GenericQualifyingAddressStructureKr] = field(
        default=None,
        metadata={
            "name": "QualifyingAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    contact: Optional[ContactDetailsStructureKr] = field(
        default=None,
        metadata={
            "name": "Contact",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    agent: Optional[AgentStructureKr] = field(
        default=None,
        metadata={
            "name": "Agent",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    date_of_birth_annex: Optional[DateOfBirthAnnex] = field(
        default=None,
        metadata={
            "name": "DateOfBirthAnnex",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/extensions",
        },
    )
    national_identification_number: Optional[NationalIdentificationNumber] = (
        field(
            default=None,
            metadata={
                "name": "NationalIdentificationNumber",
                "type": "Element",
                "namespace": "http://www.kiesraad.nl/extensions",
            },
        )
    )
