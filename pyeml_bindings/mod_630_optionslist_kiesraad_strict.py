from dataclasses import dataclass, field
from typing import Any, Optional

from pyeml_bindings.kiesraad_eml_extensions import (
    CreationDateTime,
    ElectionSubcategory,
    ElectionTree,
)
from pyeml_bindings.kiesraad_eml_restrictions import (
    ElectionIdentifierStructureKr,
    EmlstructureKr,
)

__NAMESPACE__ = "urn:oasis:names:tc:evs:schema:eml"


@dataclass(kw_only=True)
class ProposalIdentifierStructure630:
    """
    :ivar proposal_name: The question text of the referendum.
    :ivar id:
    :ivar display_order:
    :ivar short_code:
    """

    proposal_name: str = field(
        metadata={
            "name": "ProposalName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    display_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        },
    )
    short_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShortCode",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ReferendumOptionIdentifierStructure630:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    id: str = field(
        metadata={
            "name": "Id",
            "type": "Attribute",
            "required": True,
        }
    )
    display_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
        },
    )
    short_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShortCode",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Emlstructure630(EmlstructureKr):
    """
    Only TransactionId and IssueDate needed, CanoncalizationMethod added.
    """

    class Meta:
        name = "EMLstructure630"

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
        default="630",
        metadata={
            "name": "Id",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ElectionIdentifierStructure630(ElectionIdentifierStructureKr):
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
    election_name: str = field(
        metadata={
            "name": "ElectionName",
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
            "min_occurs": 2,
            "max_occurs": 3,
        },
    )


@dataclass(kw_only=True)
class ProposalStructure630:
    proposal_identifier: Optional[ProposalIdentifierStructure630] = field(
        default=None,
        metadata={
            "name": "ProposalIdentifier",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    options: Optional["ProposalStructure630.Options"] = field(
        default=None,
        metadata={
            "name": "Options",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )

    @dataclass(kw_only=True)
    class Options:
        """
        :ivar referendum_option_identifier: Its value contains an answer
            text to the referendum question.
        """

        referendum_option_identifier: list[
            ReferendumOptionIdentifierStructure630
        ] = field(
            default_factory=list,
            metadata={
                "name": "ReferendumOptionIdentifier",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:evs:schema:eml",
                "min_occurs": 1,
            },
        )


@dataclass(kw_only=True)
class OptionsList:
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"

    election: "OptionsList.Election" = field(
        metadata={
            "name": "Election",
            "type": "Element",
            "required": True,
        }
    )

    @dataclass(kw_only=True)
    class Election:
        election_identifier: ElectionIdentifierStructure630 = field(
            metadata={
                "name": "ElectionIdentifier",
                "type": "Element",
                "required": True,
            }
        )
        proposal: ProposalStructure630 = field(
            metadata={
                "name": "Proposal",
                "type": "Element",
                "required": True,
            }
        )
        election_tree: ElectionTree = field(
            metadata={
                "name": "ElectionTree",
                "type": "Element",
                "namespace": "http://www.kiesraad.nl/extensions",
                "required": True,
            }
        )


@dataclass(kw_only=True)
class Eml(Emlstructure630):
    class Meta:
        name = "EML"
        namespace = "urn:oasis:names:tc:evs:schema:eml"

    options_list: OptionsList = field(
        metadata={
            "name": "OptionsList",
            "type": "Element",
            "required": True,
        }
    )
