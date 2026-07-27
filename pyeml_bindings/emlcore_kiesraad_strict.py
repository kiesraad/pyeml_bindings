from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum

from xsdata.models.datatype import XmlDate, XmlDateTime

from pyeml_bindings.emlexternals_kiesraad_strict import (
    AuthorityAddressStructure,
    ElectoralAddressStructure,
    MailingAddressStructure,
    OfficialAddressStructure,
    PersonNameStructure,
    PhysicalAddressStructure,
    PostalLocationStructure,
    ProxyAddressStructure,
    QualifyingAddressStructure,
)
from pyeml_bindings.external.emltimestamp import Timestamp
from pyeml_bindings.external.xmldsig_core_schema import Signature

__NAMESPACE__ = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class AffiliationIdentifierStructure:
    registered_name: str = field(
        metadata={
            "name": "RegisteredName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    display_order: None | int = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        },
    )
    short_code: None | str = field(
        default=None,
        metadata={
            "name": "ShortCode",
            "type": "Attribute",
        },
    )
    expected_confirmation_reference: None | str = field(
        default=None,
        metadata={
            "name": "ExpectedConfirmationReference",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class AreaStructure:
    """
    The geographical area (and its type, such as County) covered by a
    contest.
    """

    value: str = field(default="")
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    display_order: None | int = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class AuthorityIdentifierStructure:
    value: str = field(default="")
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    display_order: None | int = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class BallotIdentifierStructure:
    ballot_name: None | str = field(
        default=None,
        metadata={
            "name": "BallotName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    id: str = field(
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )
    display_order: None | int = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        },
    )


class BinaryFormat(Enum):
    BMP = "bmp"
    GIF = "gif"
    JPEG = "jpeg"
    PNG = "png"
    TIFF = "tiff"


@dataclass(kw_only=True)
class ComplexDateRangeStructure:
    single_date: None | XmlDate | XmlDateTime = field(
        default=None,
        metadata={
            "name": "SingleDate",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    end: None | XmlDate | XmlDateTime = field(
        default=None,
        metadata={
            "name": "End",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    start: None | XmlDate | XmlDateTime = field(
        default=None,
        metadata={
            "name": "Start",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    type_value: str = field(
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class ContestIdentifierStructure:
    contest_name: None | str = field(
        default=None,
        metadata={
            "name": "ContestName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    id: str = field(
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )
    display_order: None | int = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        },
    )
    short_code: None | str = field(
        default=None,
        metadata={
            "name": "ShortCode",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class CountMetricStructure:
    value: Decimal = field()
    type_value: str = field(
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    algorithm_id: None | str = field(
        default=None,
        metadata={
            "name": "AlgorithmId",
            "type": "Attribute",
        },
    )
    position_xpath: None | str = field(
        default=None,
        metadata={
            "name": "PositionXPath",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class CountingAlgorithm:
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"

    value: str = field(default="")


@dataclass(kw_only=True)
class DocumentIdentifierStructure:
    value: str = field(default="")
    href: str = field(
        metadata={
            "name": "Href",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class ElectionGroupStructure:
    value: str = field(default="")
    id: str = field(
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class EventQualifierStructure:
    value: str = field(default="")
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


class GenderType(Enum):
    MALE = "male"
    FEMALE = "female"
    UNKNOWN = "unknown"


@dataclass(kw_only=True)
class MaxVotes:
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"

    value: int = field(default=1)


@dataclass(kw_only=True)
class MessageType:
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"

    value: str = field(default="")


@dataclass(kw_only=True)
class MessagesStructure:
    message: list[MessagesStructure.Message] = field(
        default_factory=list,
        metadata={
            "name": "Message",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
            "min_occurs": 1,
        },
    )
    display_order: None | int = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class Message:
        format: None | str = field(
            default=None,
            metadata={
                "name": "Format",
                "type": "Attribute",
            },
        )
        type_value: None | str = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            },
        )
        lang: None | str = field(
            default=None,
            metadata={
                "name": "Lang",
                "type": "Attribute",
            },
        )
        content: list[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            },
        )


@dataclass(kw_only=True)
class MinVotes:
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"

    value: int = field(default=0)


@dataclass(kw_only=True)
class NumberInSequence:
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"

    value: int = field()


@dataclass(kw_only=True)
class NumberOfPositions:
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"

    value: int = field(default=1)


class PeriodStructurePermanent(Enum):
    YES = "yes"


@dataclass(kw_only=True)
class PollingDistrictStructure:
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    association: list[PollingDistrictStructure.Association] = field(
        default_factory=list,
        metadata={
            "name": "Association",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    display_order: None | int = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class Association:
        value: str = field(default="")
        id: None | str = field(
            default=None,
            metadata={
                "name": "Id",
                "type": "Attribute",
            },
        )


@dataclass(kw_only=True)
class PositionStructure:
    value: str = field(default="")
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    display_order: None | int = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        },
    )


class ProcessingUnitStructureRole(Enum):
    NEXT_RECEIVER = "next receiver"
    PREVIOUS_SENDER = "previous sender"
    RECEIVER = "receiver"
    SENDER = "sender"
    VALUE = ""


@dataclass(kw_only=True)
class ProposalIdentifierStructure:
    proposal_name: None | str = field(
        default=None,
        metadata={
            "name": "ProposalName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    display_order: None | int = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        },
    )
    short_code: None | str = field(
        default=None,
        metadata={
            "name": "ShortCode",
            "type": "Attribute",
        },
    )
    expected_confirmation_reference: None | str = field(
        default=None,
        metadata={
            "name": "ExpectedConfirmationReference",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ProposalItemStructure:
    proposal_text: None | str = field(
        default=None,
        metadata={
            "name": "ProposalText",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    selection_text: None | str = field(
        default=None,
        metadata={
            "name": "SelectionText",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    referendum_option_identifier: None | str = field(
        default=None,
        metadata={
            "name": "ReferendumOptionIdentifier",
            "type": "Attribute",
        },
    )
    proposal_identifier: None | str = field(
        default=None,
        metadata={
            "name": "ProposalIdentifier",
            "type": "Attribute",
        },
    )
    lang: None | str = field(
        default=None,
        metadata={
            "name": "Lang",
            "type": "Attribute",
        },
    )


class ProposerStructureCategory(Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"
    OTHER = "other"


@dataclass(kw_only=True)
class ReferendumOptionIdentifierStructure:
    value: str = field(default="")
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    display_order: None | int = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        },
    )
    short_code: None | str = field(
        default=None,
        metadata={
            "name": "ShortCode",
            "type": "Attribute",
        },
    )
    expected_confirmation_reference: None | str = field(
        default=None,
        metadata={
            "name": "ExpectedConfirmationReference",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ReportingUnitIdentifierStructure:
    value: str = field(default="")
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    display_order: None | int = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ResultsReportedStructure:
    status: ResultsReportedStructure.Status = field(
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        }
    )
    current_status: None | str = field(
        default=None,
        metadata={
            "name": "CurrentStatus",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class Status:
        channel_id: None | str = field(
            default=None,
            metadata={
                "name": "ChannelID",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:evs:schema:eml",
            },
        )
        notes: None | str = field(
            default=None,
            metadata={
                "name": "Notes",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:evs:schema:eml",
            },
        )
        date_time: None | XmlDateTime = field(
            default=None,
            metadata={
                "name": "DateTime",
                "type": "Attribute",
            },
        )
        type_value: None | str = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            },
        )


@dataclass(kw_only=True)
class ScrutinyRequirementStructure:
    value: str = field(default="")


@dataclass(kw_only=True)
class SequenceNumber:
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"

    value: int = field()


@dataclass(kw_only=True)
class SimpleDateRangeStructure:
    start: XmlDate | XmlDateTime = field(
        metadata={
            "name": "Start",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        }
    )
    end: XmlDate | XmlDateTime = field(
        metadata={
            "name": "End",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        }
    )


@dataclass(kw_only=True)
class SupporterIdentifierStructure:
    supporter_name: str = field(
        metadata={
            "name": "SupporterName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        }
    )
    supporter_abbreviation: str = field(
        metadata={
            "name": "SupporterAbbreviation",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        }
    )
    registered_full_name: str = field(
        metadata={
            "name": "RegisteredFullName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        }
    )
    alternative_name: str = field(
        metadata={
            "name": "AlternativeName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    display_order: None | int = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class TransactionId:
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"

    value: str = field(default="")


@dataclass(kw_only=True)
class VtokenStructure:
    class Meta:
        name = "VTokenStructure"

    component: list[VtokenStructure.Component] = field(
        default_factory=list,
        metadata={
            "name": "Component",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class Component:
        content: list[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            },
        )


class VoterInformationStructureGender(Enum):
    MALE = "male"
    FEMALE = "female"
    UNKNOWN = "unknown"


class VotingChannelType(Enum):
    SMS = "SMS"
    WAP = "WAP"
    DIGITAL_TV = "digitalTV"
    INTERNET = "internet"
    KIOSK = "kiosk"
    POLLING = "polling"
    POSTAL = "postal"
    TELEPHONE = "telephone"
    OTHER = "other"


class VotingMethodType(Enum):
    AMS = "AMS"
    FPP = "FPP"
    IRV = "IRV"
    NOR = "NOR"
    OPV = "OPV"
    RCV = "RCV"
    SPV = "SPV"
    STV = "STV"
    CUMULATIVE = "cumulative"
    APPROVAL = "approval"
    BLOCK = "block"
    SUPPORTERLIST = "supporterlist"
    PARTISAN = "partisan"
    SUPPLEMENTARYVOTE = "supplementaryvote"
    OTHER = "other"


class WriteInType(Enum):
    ALLOWED = "allowed"
    NONE = "none"
    STRIKEOUT = "strikeout"
    OTHER = "other"


class YesNoType(Enum):
    NO = "no"
    YES = "yes"


@dataclass(kw_only=True)
class Accepted:
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"

    value: YesNoType = field()


@dataclass(kw_only=True)
class AffiliationIdentifier(AffiliationIdentifierStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class AgentIdentifierStructure:
    agent_name: PersonNameStructure = field(
        metadata={
            "name": "AgentName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    display_order: None | int = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Area(AreaStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class AuthorityIdentifier(AuthorityIdentifierStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class BallotIdentifier(BallotIdentifierStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class BallotIdentifierRangeStructure:
    start: BallotIdentifierStructure = field(
        metadata={
            "name": "Start",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        }
    )
    end: BallotIdentifierStructure = field(
        metadata={
            "name": "End",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        }
    )
    colour: None | str = field(
        default=None,
        metadata={
            "name": "Colour",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class BinaryItemStructure:
    url: None | str = field(
        default=None,
        metadata={
            "name": "URL",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    binary: None | BinaryItemStructure.Binary = field(
        default=None,
        metadata={
            "name": "Binary",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    display_order: None | int = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        },
    )
    item_type: None | str = field(
        default=None,
        metadata={
            "name": "ItemType",
            "type": "Attribute",
        },
    )
    verified: None | YesNoType = field(
        default=None,
        metadata={
            "name": "Verified",
            "type": "Attribute",
        },
    )
    problem: None | YesNoType = field(
        default=None,
        metadata={
            "name": "Problem",
            "type": "Attribute",
        },
    )
    notes: None | str = field(
        default=None,
        metadata={
            "name": "Notes",
            "type": "Attribute",
        },
    )
    role: None | str = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class Binary:
        value: bytes = field(
            default=b"",
            metadata={
                "format": "base64",
            },
        )
        format: BinaryFormat = field(
            metadata={
                "name": "Format",
                "type": "Attribute",
            }
        )


@dataclass(kw_only=True)
class CandidateIdentifierStructure:
    candidate_name: None | str = field(
        default=None,
        metadata={
            "name": "CandidateName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
            "max_length": 70,
        },
    )
    known_as: None | str = field(
        default=None,
        metadata={
            "name": "KnownAs",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    candidate_gender: None | GenderType = field(
        default=None,
        metadata={
            "name": "CandidateGender",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    short_code: None | str = field(
        default=None,
        metadata={
            "name": "ShortCode",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    display_order: None | int = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        },
    )
    short_code_attribute: None | str = field(
        default=None,
        metadata={
            "name": "ShortCode",
            "type": "Attribute",
        },
    )
    expected_confirmation_reference: None | str = field(
        default=None,
        metadata={
            "name": "ExpectedConfirmationReference",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ContestIdentifier(ContestIdentifierStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class CountMetric(CountMetricStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class CountQualifierStructure:
    simulation: None | YesNoType = field(
        default=None,
        metadata={
            "name": "Simulation",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    final: None | YesNoType = field(
        default=None,
        metadata={
            "name": "Final",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    extrapolation: None | YesNoType = field(
        default=None,
        metadata={
            "name": "Extrapolation",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    partial: None | YesNoType = field(
        default=None,
        metadata={
            "name": "Partial",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    previous: None | YesNoType = field(
        default=None,
        metadata={
            "name": "Previous",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )


@dataclass(kw_only=True)
class DocumentIdentifier(DocumentIdentifierStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class ElectionIdentifierStructure:
    election_name: None | str = field(
        default=None,
        metadata={
            "name": "ElectionName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    election_group: None | ElectionGroupStructure = field(
        default=None,
        metadata={
            "name": "ElectionGroup",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    election_category: None | str = field(
        default=None,
        metadata={
            "name": "ElectionCategory",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    id: str = field(
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )
    display_order: None | int = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        },
    )
    short_code: None | str = field(
        default=None,
        metadata={
            "name": "ShortCode",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ElectionStatement(MessagesStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class EmailStructure:
    value: str = field(
        default="",
        metadata={
            "max_length": 129,
            "pattern": r"[^@]+@[^@]+",
        },
    )
    preferred: None | YesNoType = field(
        default=None,
        metadata={
            "name": "Preferred",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class EventIdentifierStructure:
    event_name: None | str = field(
        default=None,
        metadata={
            "name": "EventName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    event_qualifier: None | EventQualifierStructure = field(
        default=None,
        metadata={
            "name": "EventQualifier",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    display_order: None | int = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class EventQualifier(EventQualifierStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class Gender:
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"

    value: GenderType = field()


@dataclass(kw_only=True)
class PersonName(PersonNameStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class PollingDistrict(PollingDistrictStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class Position(PositionStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class PreviousElectoralAddress(ElectoralAddressStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class ProcessingUnitStructure:
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    id: str = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        }
    )
    role: ProcessingUnitStructureRole = field(
        metadata={
            "name": "Role",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class Profile(MessagesStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class ProposalIdentifier(ProposalIdentifierStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class ProposalItem(ProposalItemStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class ReferendumOptionIdentifier(ReferendumOptionIdentifierStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class ReportingUnitIdentifier(ReportingUnitIdentifierStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class ScrutinyRequirement(ScrutinyRequirementStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class SealStructure:
    signature: None | Signature = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    timestamp: None | Timestamp = field(
        default=None,
        metadata={
            "name": "Timestamp",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
        },
    )
    other_seal: None | SealStructure.OtherSeal = field(
        default=None,
        metadata={
            "name": "OtherSeal",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )

    @dataclass(kw_only=True)
    class OtherSeal:
        other_element: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "##other",
            },
        )
        type_value: str = field(
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )


@dataclass(kw_only=True)
class SupporterIdentifier(SupporterIdentifierStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class TelephoneStructure:
    number: str = field(
        metadata={
            "name": "Number",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
            "min_length": 1,
            "max_length": 35,
            "pattern": r"\+?[0-9\(\)\-\s]{1,35}",
        }
    )
    extension: None | str = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
            "min_length": 1,
            "max_length": 6,
            "pattern": r"[0-9]{1,6}",
        },
    )
    preferred: None | YesNoType = field(
        default=None,
        metadata={
            "name": "Preferred",
            "type": "Attribute",
        },
    )
    mobile: None | YesNoType = field(
        default=None,
        metadata={
            "name": "Mobile",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Vtoken(VtokenStructure):
    class Meta:
        name = "VToken"
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class VoterName(PersonNameStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class VotingChannel:
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"

    value: VotingChannelType = field()


@dataclass(kw_only=True)
class VotingMethod:
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"

    value: VotingMethodType = field()


@dataclass(kw_only=True)
class WriteIn:
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"

    value: WriteInType = field()


@dataclass(kw_only=True)
class AgentIdentifier(AgentIdentifierStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class AuditInformationStructure:
    voting_channel: None | VotingChannel = field(
        default=None,
        metadata={
            "name": "VotingChannel",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    processing_units: None | AuditInformationStructure.ProcessingUnits = field(
        default=None,
        metadata={
            "name": "ProcessingUnits",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )

    @dataclass(kw_only=True)
    class ProcessingUnits:
        originating_device: None | ProcessingUnitStructure = field(
            default=None,
            metadata={
                "name": "OriginatingDevice",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:evs:schema:eml",
            },
        )
        gateway: None | ProcessingUnitStructure = field(
            default=None,
            metadata={
                "name": "Gateway",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:evs:schema:eml",
            },
        )
        voting_system: None | ProcessingUnitStructure = field(
            default=None,
            metadata={
                "name": "VotingSystem",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:evs:schema:eml",
            },
        )
        counting_system: None | ProcessingUnitStructure = field(
            default=None,
            metadata={
                "name": "CountingSystem",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:evs:schema:eml",
            },
        )
        vtoken_logging_system: None | ProcessingUnitStructure = field(
            default=None,
            metadata={
                "name": "VTokenLoggingSystem",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:evs:schema:eml",
            },
        )
        seal_logging_system: None | ProcessingUnitStructure = field(
            default=None,
            metadata={
                "name": "SealLoggingSystem",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:evs:schema:eml",
            },
        )
        other: list[AuditInformationStructure.ProcessingUnits.Other] = field(
            default_factory=list,
            metadata={
                "name": "Other",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:evs:schema:eml",
            },
        )

        @dataclass(kw_only=True)
        class Other(ProcessingUnitStructure):
            type_value: str = field(
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )


@dataclass(kw_only=True)
class BallotIdentifierRange(BallotIdentifierRangeStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class CandidateIdentifier(CandidateIdentifierStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class ContactDetailsStructure:
    mailing_address: None | MailingAddressStructure = field(
        default=None,
        metadata={
            "name": "MailingAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    email: list[EmailStructure] = field(
        default_factory=list,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    telephone: list[TelephoneStructure] = field(
        default_factory=list,
        metadata={
            "name": "Telephone",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    fax: list[TelephoneStructure] = field(
        default_factory=list,
        metadata={
            "name": "Fax",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    preferred_contact: None | str = field(
        default=None,
        metadata={
            "name": "PreferredContact",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    display_order: None | int = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class CountQualifier(CountQualifierStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class ElectionIdentifier(ElectionIdentifierStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class EventIdentifier(EventIdentifierStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class LogoStructure(BinaryItemStructure):
    pass


@dataclass(kw_only=True)
class PollingPlaceStructure:
    physical_location: None | PollingPlaceStructure.PhysicalLocation = field(
        default=None,
        metadata={
            "name": "PhysicalLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    postal_location: None | PollingPlaceStructure.PostalLocation = field(
        default=None,
        metadata={
            "name": "PostalLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    electronic_location: None | PollingPlaceStructure.ElectronicLocation = (
        field(
            default=None,
            metadata={
                "name": "ElectronicLocation",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:evs:schema:eml",
            },
        )
    )
    other_location: None | PollingPlaceStructure.OtherLocation = field(
        default=None,
        metadata={
            "name": "OtherLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    time_available: list[PollingPlaceStructure.TimeAvailable] = field(
        default_factory=list,
        metadata={
            "name": "TimeAvailable",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    results_reported: list[ResultsReportedStructure] = field(
        default_factory=list,
        metadata={
            "name": "ResultsReported",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    channel: VotingChannelType = field(
        metadata={
            "name": "Channel",
            "type": "Attribute",
        }
    )
    display_order: None | int = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class TimeAvailable:
        start: XmlDateTime = field(
            metadata={
                "name": "Start",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:evs:schema:eml",
            }
        )
        end: XmlDateTime = field(
            metadata={
                "name": "End",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:evs:schema:eml",
            }
        )

    @dataclass(kw_only=True)
    class PhysicalLocation:
        address: PhysicalAddressStructure = field(
            metadata={
                "name": "Address",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:evs:schema:eml",
            }
        )
        polling_station: list[
            PollingPlaceStructure.PhysicalLocation.PollingStation
        ] = field(
            default_factory=list,
            metadata={
                "name": "PollingStation",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:evs:schema:eml",
            },
        )
        map: None | BinaryItemStructure = field(
            default=None,
            metadata={
                "name": "Map",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:evs:schema:eml",
            },
        )
        id: None | str = field(
            default=None,
            metadata={
                "name": "Id",
                "type": "Attribute",
            },
        )

        @dataclass(kw_only=True)
        class PollingStation:
            value: str = field(default="")
            id: None | str = field(
                default=None,
                metadata={
                    "name": "Id",
                    "type": "Attribute",
                },
            )

    @dataclass(kw_only=True)
    class PostalLocation(PostalLocationStructure):
        id: None | str = field(
            default=None,
            metadata={
                "name": "Id",
                "type": "Attribute",
            },
        )
        display_order: None | int = field(
            default=None,
            metadata={
                "name": "DisplayOrder",
                "type": "Attribute",
            },
        )

    @dataclass(kw_only=True)
    class ElectronicLocation:
        value: str = field(default="")
        id: None | str = field(
            default=None,
            metadata={
                "name": "Id",
                "type": "Attribute",
            },
        )
        display_order: None | int = field(
            default=None,
            metadata={
                "name": "DisplayOrder",
                "type": "Attribute",
            },
        )

    @dataclass(kw_only=True)
    class OtherLocation:
        value: str = field(default="")
        id: None | str = field(
            default=None,
            metadata={
                "name": "Id",
                "type": "Attribute",
            },
        )
        display_order: None | int = field(
            default=None,
            metadata={
                "name": "DisplayOrder",
                "type": "Attribute",
            },
        )


@dataclass(kw_only=True)
class ProposalStructure:
    proposal_identifier: None | ProposalIdentifier = field(
        default=None,
        metadata={
            "name": "ProposalIdentifier",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    description: None | MessagesStructure = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    options: None | ProposalStructure.Options = field(
        default=None,
        metadata={
            "name": "Options",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    proposal_item: None | ProposalItem = field(
        default=None,
        metadata={
            "name": "ProposalItem",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class Options:
        referendum_option_identifier: list[ReferendumOptionIdentifier] = field(
            default_factory=list,
            metadata={
                "name": "ReferendumOptionIdentifier",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:evs:schema:eml",
                "min_occurs": 1,
            },
        )


@dataclass(kw_only=True)
class Seal(SealStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class VtokenQualifiedStructure(VtokenStructure):
    class Meta:
        name = "VTokenQualifiedStructure"

    reason: VtokenQualifiedStructure.Reason = field(
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        }
    )
    vtoken: None | Vtoken = field(
        default=None,
        metadata={
            "name": "VToken",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )

    @dataclass(kw_only=True)
    class Reason:
        value: str = field(default="")
        type_value: str = field(
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )


@dataclass(kw_only=True)
class AuditInformation(AuditInformationStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class ContactDetails(ContactDetailsStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class InternalGenericCommunicationStructure:
    from_value: None | InternalGenericCommunicationStructure.From = field(
        default=None,
        metadata={
            "name": "From",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    to: None | InternalGenericCommunicationStructure.To = field(
        default=None,
        metadata={
            "name": "To",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    event_identifier: None | EventIdentifier = field(
        default=None,
        metadata={
            "name": "EventIdentifier",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    election_identifier: None | ElectionIdentifier = field(
        default=None,
        metadata={
            "name": "ElectionIdentifier",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    contest_identifier: None | ContestIdentifier = field(
        default=None,
        metadata={
            "name": "ContestIdentifier",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    messages: None | MessagesStructure = field(
        default=None,
        metadata={
            "name": "Messages",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )

    @dataclass(kw_only=True)
    class From:
        target_namespace_element: list[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##targetNamespace",
            },
        )

    @dataclass(kw_only=True)
    class To:
        target_namespace_element: list[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##targetNamespace",
            },
        )


@dataclass(kw_only=True)
class Logo(LogoStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class NominatingOfficerStructure:
    name: PersonNameStructure = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        }
    )
    contact: ContactDetailsStructure = field(
        metadata={
            "name": "Contact",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
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
class PeriodStructure:
    dates: None | PeriodStructure.Dates = field(
        default=None,
        metadata={
            "name": "Dates",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    event: list[PeriodStructure.Event] = field(
        default_factory=list,
        metadata={
            "name": "Event",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    permanent: None | PeriodStructurePermanent = field(
        default=None,
        metadata={
            "name": "Permanent",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )

    @dataclass(kw_only=True)
    class Dates:
        start: None | XmlDate = field(
            default=None,
            metadata={
                "name": "Start",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:evs:schema:eml",
            },
        )
        end: XmlDate = field(
            metadata={
                "name": "End",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:evs:schema:eml",
            }
        )

    @dataclass(kw_only=True)
    class Event:
        event_identifier: EventIdentifier = field(
            metadata={
                "name": "EventIdentifier",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:evs:schema:eml",
            }
        )
        election_identifier: list[ElectionIdentifier] = field(
            default_factory=list,
            metadata={
                "name": "ElectionIdentifier",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:evs:schema:eml",
            },
        )


@dataclass(kw_only=True)
class PollingPlace(PollingPlaceStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class Proposal(ProposalStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class ProposerStructure:
    name: PersonNameStructure = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        }
    )
    contact: None | ContactDetailsStructure = field(
        default=None,
        metadata={
            "name": "Contact",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    job_title: None | str = field(
        default=None,
        metadata={
            "name": "JobTitle",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    date_of_birth: None | XmlDate = field(
        default=None,
        metadata={
            "name": "DateOfBirth",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    category: None | ProposerStructureCategory = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ResponsibleOfficerStructure:
    responsibility: None | str = field(
        default=None,
        metadata={
            "name": "Responsibility",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    name: None | PersonNameStructure = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    contact: None | ContactDetailsStructure = field(
        default=None,
        metadata={
            "name": "Contact",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class VtokenQualified(VtokenQualifiedStructure):
    class Meta:
        name = "VTokenQualified"
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class AffiliationStructure:
    affiliation_identifier: AffiliationIdentifier = field(
        metadata={
            "name": "AffiliationIdentifier",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        }
    )
    type_value: str = field(
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        }
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    logo: list[Logo] = field(
        default_factory=list,
        metadata={
            "name": "Logo",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )


@dataclass(kw_only=True)
class NominatingOfficer(NominatingOfficerStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class Period(PeriodStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class Proposer(ProposerStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class ResponsibleOfficer(ResponsibleOfficerStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class SupporterStructure:
    supporter_identifier: SupporterIdentifier = field(
        metadata={
            "name": "SupporterIdentifier",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        }
    )
    logo: list[Logo] = field(
        default_factory=list,
        metadata={
            "name": "Logo",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )


@dataclass(kw_only=True)
class VoterIdentificationStructure:
    """
    :ivar voter_name:
    :ivar electoral_address: This is the address that gives the voter
        the right to vote
    :ivar previous_electoral_address:
    :ivar vtoken:
    :ivar vtoken_qualified:
    :ivar voter_id:
    :ivar voter_signature:
    :ivar other_element:
    :ivar display_order:
    :ivar id:
    """

    voter_name: None | VoterName = field(
        default=None,
        metadata={
            "name": "VoterName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    electoral_address: None | ElectoralAddressStructure = field(
        default=None,
        metadata={
            "name": "ElectoralAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    previous_electoral_address: None | ElectoralAddressStructure = field(
        default=None,
        metadata={
            "name": "PreviousElectoralAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    vtoken: None | Vtoken = field(
        default=None,
        metadata={
            "name": "VToken",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    vtoken_qualified: None | VtokenQualified = field(
        default=None,
        metadata={
            "name": "VTokenQualified",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    voter_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "VoterId",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    voter_signature: None | BinaryItemStructure = field(
        default=None,
        metadata={
            "name": "VoterSignature",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    display_order: None | int = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        },
    )
    id: None | object = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Affiliation(AffiliationStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class ChannelStructure:
    preferred_channel: list[ChannelStructure.PreferredChannel] = field(
        default_factory=list,
        metadata={
            "name": "PreferredChannel",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    period: None | Period = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )

    @dataclass(kw_only=True)
    class PreferredChannel:
        value: VotingChannelType = field()
        fixed: None | YesNoType = field(
            default=None,
            metadata={
                "name": "Fixed",
                "type": "Attribute",
            },
        )


@dataclass(kw_only=True)
class Endorsement(SupporterStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class ManagingAuthorityStructure:
    authority_identifier: AuthorityIdentifier = field(
        metadata={
            "name": "AuthorityIdentifier",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        }
    )
    authority_address: AuthorityAddressStructure = field(
        metadata={
            "name": "AuthorityAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        }
    )
    responsible_officer: list[ResponsibleOfficer] = field(
        default_factory=list,
        metadata={
            "name": "ResponsibleOfficer",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    logo: None | Logo = field(
        default=None,
        metadata={
            "name": "Logo",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )


@dataclass(kw_only=True)
class AgentStructure:
    agent_identifier: AgentIdentifier = field(
        metadata={
            "name": "AgentIdentifier",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        }
    )
    affiliation: None | Affiliation = field(
        default=None,
        metadata={
            "name": "Affiliation",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    official_address: None | OfficialAddressStructure = field(
        default=None,
        metadata={
            "name": "OfficialAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    contact: None | ContactDetailsStructure = field(
        default=None,
        metadata={
            "name": "Contact",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    display_order: None | int = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        },
    )
    role: None | str = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Channel(ChannelStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class ManagingAuthority(ManagingAuthorityStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class Agent(AgentStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class Emlstructure:
    class Meta:
        name = "EMLstructure"

    transaction_id: TransactionId = field(
        metadata={
            "name": "TransactionId",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        }
    )
    sequence_number: None | SequenceNumber = field(
        default=None,
        metadata={
            "name": "SequenceNumber",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    number_in_sequence: None | NumberInSequence = field(
        default=None,
        metadata={
            "name": "NumberInSequence",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    sequenced_element_name: None | str = field(
        default=None,
        metadata={
            "name": "SequencedElementName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    additional_validation: None | Emlstructure.AdditionalValidation = field(
        default=None,
        metadata={
            "name": "AdditionalValidation",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    message_language: None | str = field(
        default=None,
        metadata={
            "name": "MessageLanguage",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    requested_response_language: None | str = field(
        default=None,
        metadata={
            "name": "RequestedResponseLanguage",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    managing_authority: None | ManagingAuthority = field(
        default=None,
        metadata={
            "name": "ManagingAuthority",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    issue_date: None | XmlDate | XmlDateTime = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    display: list[Emlstructure.Display] = field(
        default_factory=list,
        metadata={
            "name": "Display",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    seal: None | Seal = field(
        default=None,
        metadata={
            "name": "Seal",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    id: str = field(
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )
    schema_version: str = field(
        metadata={
            "name": "SchemaVersion",
            "type": "Attribute",
        }
    )

    @dataclass(kw_only=True)
    class AdditionalValidation:
        location: str = field(
            metadata={
                "name": "Location",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:evs:schema:eml",
            }
        )
        type_value: str = field(
            metadata={
                "name": "Type",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:evs:schema:eml",
            }
        )

    @dataclass(kw_only=True)
    class Display:
        stylesheet: list[Emlstructure.Display.Stylesheet] = field(
            default_factory=list,
            metadata={
                "name": "Stylesheet",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:evs:schema:eml",
                "min_occurs": 1,
            },
        )
        format: None | str = field(
            default=None,
            metadata={
                "name": "Format",
                "type": "Attribute",
            },
        )

        @dataclass(kw_only=True)
        class Stylesheet:
            value: str = field(default="")
            type_value: str = field(
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )


@dataclass(kw_only=True)
class ProxyStructure:
    position: None | str = field(
        default=None,
        metadata={
            "name": "Position",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    name: None | PersonNameStructure = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    address: None | ProxyAddressStructure = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    date_of_birth: None | XmlDate = field(
        default=None,
        metadata={
            "name": "DateOfBirth",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    qualification: None | str = field(
        default=None,
        metadata={
            "name": "Qualification",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    reason: None | str = field(
        default=None,
        metadata={
            "name": "Reason",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    period: None | Period = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    proxy_agrees: None | YesNoType = field(
        default=None,
        metadata={
            "name": "ProxyAgrees",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    preferred_language: None | str = field(
        default=None,
        metadata={
            "name": "PreferredLanguage",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    channel: list[Channel] = field(
        default_factory=list,
        metadata={
            "name": "Channel",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    vtoken: None | Vtoken = field(
        default=None,
        metadata={
            "name": "VToken",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    vtoken_qualified: None | VtokenQualified = field(
        default=None,
        metadata={
            "name": "VTokenQualified",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    display_order: None | int = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class CandidateStructure:
    candidate_identifier: None | CandidateIdentifier = field(
        default=None,
        metadata={
            "name": "CandidateIdentifier",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    candidate_full_name: None | PersonNameStructure = field(
        default=None,
        metadata={
            "name": "CandidateFullName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    date_of_birth: None | XmlDate = field(
        default=None,
        metadata={
            "name": "DateOfBirth",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    age: None | int = field(
        default=None,
        metadata={
            "name": "Age",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    gender: None | Gender = field(
        default=None,
        metadata={
            "name": "Gender",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    qualifying_address: None | QualifyingAddressStructure = field(
        default=None,
        metadata={
            "name": "QualifyingAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    contact: None | ContactDetailsStructure = field(
        default=None,
        metadata={
            "name": "Contact",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    affiliation: None | Affiliation = field(
        default=None,
        metadata={
            "name": "Affiliation",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    logo: list[Logo] = field(
        default_factory=list,
        metadata={
            "name": "Logo",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    profession: None | str = field(
        default=None,
        metadata={
            "name": "Profession",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    agent: list[Agent] = field(
        default_factory=list,
        metadata={
            "name": "Agent",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    photo: None | BinaryItemStructure = field(
        default=None,
        metadata={
            "name": "Photo",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    profile: None | Profile = field(
        default=None,
        metadata={
            "name": "Profile",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    election_statement: None | ElectionStatement = field(
        default=None,
        metadata={
            "name": "ElectionStatement",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    proposal_item: None | ProposalItem = field(
        default=None,
        metadata={
            "name": "ProposalItem",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    display_order: None | int = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        },
    )
    independent: None | YesNoType = field(
        default=None,
        metadata={
            "name": "Independent",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Proxy(ProxyStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class Candidate(CandidateStructure):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class IncomingGenericCommunicationStructure:
    voter: IncomingGenericCommunicationStructure.Voter = field(
        metadata={
            "name": "Voter",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        }
    )
    recipient: None | ResponsibleOfficerStructure = field(
        default=None,
        metadata={
            "name": "Recipient",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    event_identifier: None | EventIdentifier = field(
        default=None,
        metadata={
            "name": "EventIdentifier",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    election_identifier: None | ElectionIdentifier = field(
        default=None,
        metadata={
            "name": "ElectionIdentifier",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    contest_identifier: None | ContestIdentifier = field(
        default=None,
        metadata={
            "name": "ContestIdentifier",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    messages: None | MessagesStructure = field(
        default=None,
        metadata={
            "name": "Messages",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )

    @dataclass(kw_only=True)
    class Voter:
        voter_identification: VoterIdentificationStructure = field(
            metadata={
                "name": "VoterIdentification",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:evs:schema:eml",
            }
        )
        voter_contact: ContactDetailsStructure = field(
            metadata={
                "name": "VoterContact",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:evs:schema:eml",
            }
        )
        proxy: None | Proxy = field(
            default=None,
            metadata={
                "name": "Proxy",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:evs:schema:eml",
            },
        )


@dataclass(kw_only=True)
class OutgoingGenericCommunicationStructure:
    """
    Note that this can include multiple voters to allow communication with
    a distributor.
    """

    voter: list[OutgoingGenericCommunicationStructure.Voter] = field(
        default_factory=list,
        metadata={
            "name": "Voter",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
            "min_occurs": 1,
        },
    )
    event_identifier: None | EventIdentifier = field(
        default=None,
        metadata={
            "name": "EventIdentifier",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    election_identifier: None | ElectionIdentifier = field(
        default=None,
        metadata={
            "name": "ElectionIdentifier",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    contest_identifier: None | ContestIdentifier = field(
        default=None,
        metadata={
            "name": "ContestIdentifier",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    return_to: None | ResponsibleOfficerStructure = field(
        default=None,
        metadata={
            "name": "ReturnTo",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    messages: None | MessagesStructure = field(
        default=None,
        metadata={
            "name": "Messages",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )

    @dataclass(kw_only=True)
    class Voter:
        voter_identification: VoterIdentificationStructure = field(
            metadata={
                "name": "VoterIdentification",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:evs:schema:eml",
            }
        )
        voter_contact: ContactDetailsStructure = field(
            metadata={
                "name": "VoterContact",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:evs:schema:eml",
            }
        )
        proxy: None | Proxy = field(
            default=None,
            metadata={
                "name": "Proxy",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:evs:schema:eml",
            },
        )


@dataclass(kw_only=True)
class VoterInformationStructure:
    """
    :ivar contact:
    :ivar date_of_birth:
    :ivar place_of_birth:
    :ivar effective_date_added:
    :ivar effective_date_removed:
    :ivar preferred_language:
    :ivar channel:
    :ivar qualifier: e.g. military or other factor that may affect right
        to vote or how votes are managed
    :ivar check_box:
    :ivar eligibility: The election types for which the voter is
        eligible.
    :ivar polling_district:
    :ivar polling_place:
    :ivar affiliation:
    :ivar gender:
    :ivar nationality:
    :ivar ethnicity:
    :ivar special_request:
    :ivar proxy:
    :ivar further_information:
    :ivar other_element:
    :ivar id:
    :ivar display_order:
    """

    contact: list[VoterInformationStructure.Contact] = field(
        default_factory=list,
        metadata={
            "name": "Contact",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    date_of_birth: None | XmlDate = field(
        default=None,
        metadata={
            "name": "DateOfBirth",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    place_of_birth: None | str = field(
        default=None,
        metadata={
            "name": "PlaceOfBirth",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    effective_date_added: None | XmlDate = field(
        default=None,
        metadata={
            "name": "EffectiveDateAdded",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    effective_date_removed: None | XmlDate = field(
        default=None,
        metadata={
            "name": "EffectiveDateRemoved",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    preferred_language: None | str = field(
        default=None,
        metadata={
            "name": "PreferredLanguage",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    channel: list[Channel] = field(
        default_factory=list,
        metadata={
            "name": "Channel",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    qualifier: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    check_box: list[VoterInformationStructure.CheckBox] = field(
        default_factory=list,
        metadata={
            "name": "CheckBox",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    eligibility: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Eligibility",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    polling_district: None | PollingDistrict = field(
        default=None,
        metadata={
            "name": "PollingDistrict",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    polling_place: list[PollingPlace] = field(
        default_factory=list,
        metadata={
            "name": "PollingPlace",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    affiliation: None | str = field(
        default=None,
        metadata={
            "name": "Affiliation",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    gender: None | VoterInformationStructureGender = field(
        default=None,
        metadata={
            "name": "Gender",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    nationality: None | str = field(
        default=None,
        metadata={
            "name": "Nationality",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    ethnicity: None | str = field(
        default=None,
        metadata={
            "name": "Ethnicity",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    special_request: list[str] = field(
        default_factory=list,
        metadata={
            "name": "SpecialRequest",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    proxy: list[Proxy] = field(
        default_factory=list,
        metadata={
            "name": "Proxy",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    further_information: None | MessagesStructure = field(
        default=None,
        metadata={
            "name": "FurtherInformation",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    display_order: None | int = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class Contact(ContactDetailsStructure):
        election_id: None | str = field(
            default=None,
            metadata={
                "name": "ElectionId",
                "type": "Attribute",
            },
        )

    @dataclass(kw_only=True)
    class CheckBox:
        value: YesNoType = field()
        type_value: str = field(
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
