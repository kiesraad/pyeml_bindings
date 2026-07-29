from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from pyeml_bindings.emlcore_kiesraad_strict import Emlstructure
from pyeml_bindings.kiesraad_eml_extensions import (
    CreationDateTime,
    ElectionDate,
    ElectionSubcategory,
    ElectionTree,
    Schema,
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


@dataclass(kw_only=True)
class ReferendumOptionIdentifierStructure630:
    value: str = field(default="")
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
class Emlstructure630(Emlstructure, EmlstructureKr):
    """
    only TransactionId and IssueDate needed, CanoncalizationMethod added.
    """

    class Meta:
        name = "EMLstructure630"

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
    mandatory ElectionCategory, and some additional Elements.
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
    election_date: list[ElectionDate] = field(
        default_factory=list,
        metadata={
            "name": "ElectionDate",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/extensions",
            "min_occurs": 2,
            "max_occurs": 3,
        },
    )


@dataclass(kw_only=True)
class ProposalStructure630:
    proposal_identifier: None | ProposalIdentifierStructure630 = field(
        default=None,
        metadata={
            "name": "ProposalIdentifier",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml",
        },
    )
    options: None | ProposalStructure630.Options = field(
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

        referendum_option_identifier: list[ReferendumOptionIdentifierStructure630] = (
            field(
                default_factory=list,
                metadata={
                    "name": "ReferendumOptionIdentifier",
                    "type": "Element",
                    "namespace": "urn:oasis:names:tc:evs:schema:eml",
                    "min_occurs": 1,
                },
            )
        )


@dataclass(kw_only=True)
class OptionsList:
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml"

    election: OptionsList.Election = field(
        metadata={
            "name": "Election",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Election:
        election_identifier: ElectionIdentifierStructure630 = field(
            metadata={
                "name": "ElectionIdentifier",
                "type": "Element",
            }
        )
        proposal: ProposalStructure630 = field(
            metadata={
                "name": "Proposal",
                "type": "Element",
            }
        )
        election_tree: None | ElectionTree = field(
            default=None,
            metadata={
                "name": "ElectionTree",
                "type": "Element",
                "namespace": "http://www.kiesraad.nl/extensions",
            },
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
        }
    )
