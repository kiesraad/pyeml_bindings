"""This file was generated by xsdata, v23.8, on 2023-11-02 13:39:42

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlDate, XmlDateTime
from pyeml_bindings.emlcore_kiesraad_strict import Emlstructure, VotingMethodType
from pyeml_bindings.kiesraad_eml_extensions import (
    ElectionSubcategoryType,
    ElectionTree,
    RegisteredParties,
)
from pyeml_bindings.kiesraad_eml_restrictions import (
    ContestIdentifierStructureKr,
    EmlstructureKr,
    ElectionIdentifierStructureKr,
)
from pyeml_bindings.x_al_kiesraad_strict import Address

__NAMESPACE__ = "urn:oasis:names:tc:evs:schema:eml"


class PollingPlaceStructure110Channel(Enum):
    POLLING = "polling"
    POSTAL = "postal"


@dataclass(kw_only=True)
class ContestIdentifierStructure110A(ContestIdentifierStructureKr):
    """
    Id content further restricted, contest name omitted.
    """

    class Meta:
        name = "ContestIdentifierStructure110a"


@dataclass(kw_only=True)
class Emlstructure110(Emlstructure, EmlstructureKr):
    """
    Only TransactionId and IssueDate needed, CanoncalizationMethod added.
    """

    class Meta:
        name = "EMLstructure110"

    creation_date_time: XmlDateTime = field(
        metadata={
            "name": "CreationDateTime",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/extensions",
            "required": True,
        }
    )
    id: str = field(
        init=False,
        default="110a",
        metadata={
            "name": "Id",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ElectionIdentifierStructure110A(ElectionIdentifierStructureKr):
    """
    Mandatory ElectionCategory, and some additional Elements.
    """

    class Meta:
        name = "ElectionIdentifierStructure110a"

    election_name: str = field(
        metadata={
            "name": "ElectionName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
            "required": True,
        }
    )
    election_subcategory: Optional[ElectionSubcategoryType] = field(
        default=None,
        metadata={
            "name": "ElectionSubcategory",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/extensions",
        },
    )
    nomination_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NominationDate",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/extensions",
        },
    )


@dataclass(kw_only=True)
class PollingPlaceStructure110:
    """
    Id content further restricted, contest name omitted.
    """

    physical_location: "PollingPlaceStructure110.PhysicalLocation" = field(
        metadata={
            "name": "PhysicalLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
            "required": True,
        }
    )
    channel: PollingPlaceStructure110Channel = field(
        metadata={
            "name": "Channel",
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass(kw_only=True)
    class PhysicalLocation:
        address: "PollingPlaceStructure110.PhysicalLocation.Address" = field(
            metadata={
                "name": "Address",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:evs:schema:eml",
                "required": True,
            }
        )
        polling_station: "PollingPlaceStructure110.PhysicalLocation.PollingStation" = (
            field(
                metadata={
                    "name": "PollingStation",
                    "type": "Element",
                    "namespace": "urn:oasis:names:tc:evs:schema:eml",
                    "required": True,
                }
            )
        )

        @dataclass(kw_only=True)
        class Address:
            address: Address = field(
                metadata={
                    "name": "Address",
                    "type": "Element",
                    "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
                    "required": True,
                }
            )

        @dataclass(kw_only=True)
        class PollingStation:
            value: str = field(
                default="",
                metadata={
                    "required": True,
                    "pattern": r"\d+",
                },
            )
            id: str = field(
                metadata={
                    "name": "Id",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"\d+",
                }
            )


@dataclass(kw_only=True)
class ElectionEvent:
    """
    Data (payload)
    """

    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"

    event_identifier: Optional[object] = field(
        default=None,
        metadata={
            "name": "EventIdentifier",
            "type": "Element",
        },
    )
    election: "ElectionEvent.Election" = field(
        metadata={
            "name": "Election",
            "type": "Element",
            "required": True,
        }
    )

    @dataclass(kw_only=True)
    class Election:
        """
        :ivar election_identifier:
        :ivar contest:
        :ivar number_of_seats:
        :ivar preference_threshold:
        :ivar election_tree:
        :ivar registered_parties: Registered political groupings
        """

        election_identifier: ElectionIdentifierStructure110A = field(
            metadata={
                "name": "ElectionIdentifier",
                "type": "Element",
                "required": True,
            }
        )
        contest: "ElectionEvent.Election.Contest" = field(
            metadata={
                "name": "Contest",
                "type": "Element",
                "required": True,
            }
        )
        number_of_seats: Optional[int] = field(
            default=None,
            metadata={
                "name": "NumberOfSeats",
                "type": "Element",
                "namespace": "http://www.kiesraad.nl/extensions",
            },
        )
        preference_threshold: Optional[int] = field(
            default=None,
            metadata={
                "name": "PreferenceThreshold",
                "type": "Element",
                "namespace": "http://www.kiesraad.nl/extensions",
            },
        )
        election_tree: Optional[ElectionTree] = field(
            default=None,
            metadata={
                "name": "ElectionTree",
                "type": "Element",
                "namespace": "http://www.kiesraad.nl/extensions",
            },
        )
        registered_parties: Optional[RegisteredParties] = field(
            default=None,
            metadata={
                "name": "RegisteredParties",
                "type": "Element",
                "namespace": "http://www.kiesraad.nl/extensions",
            },
        )

        @dataclass(kw_only=True)
        class Contest:
            contest_identifier: ContestIdentifierStructure110A = field(
                metadata={
                    "name": "ContestIdentifier",
                    "type": "Element",
                    "required": True,
                }
            )
            voting_method: VotingMethodType = field(
                metadata={
                    "name": "VotingMethod",
                    "type": "Element",
                    "required": True,
                }
            )
            max_votes: Optional[int] = field(
                default=None,
                metadata={
                    "name": "MaxVotes",
                    "type": "Element",
                    "required": False,
                },
            )


@dataclass(kw_only=True)
class Eml(Emlstructure110):
    class Meta:
        name = "EML"
        namespace = "urn:oasis:names:tc:evs:schema:eml"

    election_event: ElectionEvent = field(
        metadata={
            "name": "ElectionEvent",
            "type": "Element",
            "required": True,
        }
    )
