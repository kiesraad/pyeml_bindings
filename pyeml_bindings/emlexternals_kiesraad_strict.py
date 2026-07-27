from dataclasses import dataclass, field
from typing import Any

from pyeml_bindings.x_al_kiesraad_strict import AddressDetails
from pyeml_bindings.x_nl_kiesraad_strict import (
    NameDetails1,
    PersonName,
)

__NAMESPACE__ = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class AuthorityAddressStructure(AddressDetails):
    pass


@dataclass(kw_only=True)
class ElectoralAddressStructure(AddressDetails):
    pass


@dataclass(kw_only=True)
class MailingAddressStructure(AddressDetails):
    pass


@dataclass(kw_only=True)
class OfficialAddressStructure(AddressDetails):
    pass


@dataclass(kw_only=True)
class PersonNameStructure(NameDetails1):
    """
    :ivar name_line: Define name as a free format text. Use this when
        the type of the entity (person or organisation) is unknown, or
        not broken into individual elements or is beyond the provided
        types.
    :ivar joint_person_name:
    :ivar organisation_name_details:
    :ivar other_attributes:
    :ivar person_name:
    """

    name_line: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    joint_person_name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    organisation_name_details: Any = field(
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
    person_name: PersonName = field(
        metadata={
            "name": "PersonName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xNL:2.0",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PhysicalAddressStructure(AddressDetails):
    pass


@dataclass(kw_only=True)
class PostalLocationStructure(AddressDetails):
    pass


@dataclass(kw_only=True)
class ProxyAddressStructure(AddressDetails):
    pass


@dataclass(kw_only=True)
class QualifyingAddressStructure(AddressDetails):
    pass
