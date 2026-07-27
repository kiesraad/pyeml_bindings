from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

__NAMESPACE__ = "http://www.kiesraad.nl/extensions"


class AffiliationType(Enum):
    """
    Restricts the basic type to the allowed values for the affiliation type.
    """

    LIJSTENGROEP = "lijstengroep"
    STEL_GELIJKLUIDENDE_LIJSTEN = "stel gelijkluidende lijsten"
    OP_ZICHZELF_STAANDE_LIJST = "op zichzelf staande lijst"


class CommitteeCategoryType(Enum):
    CSB = "CSB"
    HSB = "HSB"
    PROV_SB = "PROV_SB"
    PSB = "PSB"


@dataclass(kw_only=True)
class Contest:
    class Meta:
        namespace = "http://www.kiesraad.nl/extensions"

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
            "pattern": r"[1-9]\d*|geen|alle|M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})",
        }
    )


class CountingMethodMethodCode(Enum):
    CENTRALE_STEMOPNEMING = "centrale stemopneming"
    DECENTRALE_STEMOPNEMING = "decentrale stemopneming"


@dataclass(kw_only=True)
class CreatedByAuthority:
    """
    Instance which created a data set on behalf of another (only if different!)
    """

    class Meta:
        namespace = "http://www.kiesraad.nl/extensions"

    id: str = field(
        metadata={
            "name": "Id",
            "type": "Attribute",
            "required": True,
            "min_length": 3,
            "pattern": r"CSB|((HSB|SB)\d+)|(\d{4})",
        }
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
class CreationDateTime:
    """
    Date and time of the last modification of the data which was used to create the
    EML file.
    """

    class Meta:
        namespace = "http://www.kiesraad.nl/extensions"

    value: XmlDateTime = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class DateOfBirthAnnex:
    """
    Use this instead of DateOfBirth when day, month and/or year is unknown, e.g.
    XX-05-1976, XX-XX-1964, XX-XX-XXXX.
    """

    class Meta:
        namespace = "http://www.kiesraad.nl/extensions"

    value: str = field(
        default="",
        metadata={
            "pattern": r"(XX-(XX|\d[1-9]|[1-9]0)-([1-9]\d{3}|\d[1-9]\d\d|\d\d[1-9]\d|\d{3}[1-9])|XX-XX-XXXX)",
        },
    )


class ElectionCategoryType(Enum):
    """
    Restricts the basic type to the allowed values for the election category
    (election type abreviation)
    """

    EK = "EK"
    TK = "TK"
    EP = "EP"
    PS = "PS"
    AB = "AB"
    GR = "GR"
    BC = "BC"
    GC = "GC"
    ER = "ER"
    NR = "NR"
    PR = "PR"
    LR = "LR"
    IR = "IR"
    KC = "KC"


@dataclass(kw_only=True)
class ElectionDate:
    """
    Election date.
    """

    class Meta:
        namespace = "http://www.kiesraad.nl/extensions"

    value: XmlDate = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ElectionDomain:
    """The (top level) region where the election takes place.

    Optional. Only needed if the ElectionDomain is part of the election
    name, e.g. election of the council of a municipality or province.
    Not needed e.g. for Tweede Kamer or European Parliament.
    """

    class Meta:
        namespace = "http://www.kiesraad.nl/extensions"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "pattern": r"\d{4}|([12]?[0-9])",
        },
    )


class ElectionSubcategoryType(Enum):
    """
    :cvar PS1: Provinciale Staaten, one electoral district
    :cvar PS2: Provinciale Staaten, more than one electoral district
    :cvar AB1: Water council elections, less than 19 seats
    :cvar AB2: Water council elections, 19 seats or more
    :cvar GR1: gemeenteraad, less than 19 seats
    :cvar GR2: gemeenteraad, 19 seats or more
    :cvar BC: bestuurscommissie (Amsterdam)
    :cvar GC: gebiedscommissie (Rotterdam)
    :cvar ER1: eilandsraad, has always less than 19 seats
    :cvar KCCN: kiescolleges Caribisch Nederland
    :cvar KCNI: kiescollege Niet-Ingezetenen
    :cvar TK:
    :cvar EK:
    :cvar EP:
    :cvar NR:
    :cvar PR:
    :cvar LR:
    :cvar IR:
    """

    PS1 = "PS1"
    PS2 = "PS2"
    AB1 = "AB1"
    AB2 = "AB2"
    GR1 = "GR1"
    GR2 = "GR2"
    BC = "BC"
    GC = "GC"
    ER1 = "ER1"
    KCCN = "KCCN"
    KCNI = "KCNI"
    TK = "TK"
    EK = "EK"
    EP = "EP"
    NR = "NR"
    PR = "PR"
    LR = "LR"
    IR = "IR"


class GenderAnnexValue(Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


@dataclass(kw_only=True)
class InitialCast:
    """The initial 'cast' element which has been corrected.

    Should only appear for changed values of 'cast' in correction files
    """

    class Meta:
        namespace = "http://www.kiesraad.nl/extensions"

    value: int = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class InitialTotalCounted:
    """The initial total amount of counted valid votes.

    Should only appear for changed values of TotalCounted in correction
    files
    """

    class Meta:
        namespace = "http://www.kiesraad.nl/extensions"

    value: int = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class InitialValidVotes:
    """The initial votecount for a candidate or party which has been corrected.

    Should only appear for changed values of ValidVotes in correction
    files
    """

    class Meta:
        namespace = "http://www.kiesraad.nl/extensions"

    value: int = field(
        metadata={
            "required": True,
        }
    )


class InvestigationReasonCode(Enum):
    ONDERZOCHT_VANWEGE_ONVERKLAARD_VERSCHIL = (
        "onderzocht vanwege onverklaard verschil"
    )
    ONDERZOCHT_VANWEGE_ANDERE_FOUT = "onderzocht vanwege andere fout"
    UITSLAG_GECORRIGEERD = "uitslag gecorrigeerd"
    TOEGELATEN_KIEZERS_OPNIEUW_VASTGESTELD = (
        "toegelaten kiezers opnieuw vastgesteld"
    )
    ONDERZOCHT_VANWEGE_ANDERE_REDEN = "onderzocht vanwege andere reden"
    STEMBILJETTEN_DEELS_HERTELD = "stembiljetten deels herteld"


@dataclass(kw_only=True)
class LivingAddressType:
    locality_name: str = field(
        metadata={
            "name": "LocalityName",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/extensions",
            "required": True,
        }
    )
    country_name_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CountryNameCode",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/extensions",
        },
    )


@dataclass(kw_only=True)
class NationalIdentificationNumber:
    """Number identifying a person in the National administration.

    For the Netherlands, this is the Burgerservicenummer (BSN).
    """

    class Meta:
        namespace = "http://www.kiesraad.nl/extensions"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class NominationDate:
    """
    Date of the proposition of the candidate list (filing of the candidate list at
    the electoral committee)
    """

    class Meta:
        namespace = "http://www.kiesraad.nl/extensions"

    value: XmlDate = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class NumberOfSeats:
    class Meta:
        namespace = "http://www.kiesraad.nl/extensions"

    value: int = field(
        metadata={
            "required": True,
        }
    )


class PhasePhaseCode(Enum):
    EERSTE_ZITTING = "eerste zitting"
    CORRIGENDUM = "corrigendum"


@dataclass(kw_only=True)
class PreferenceThreshold:
    """
    Electoral quota in % a candidate will be prefered.
    """

    class Meta:
        namespace = "http://www.kiesraad.nl/extensions"

    value: int = field(
        metadata={
            "required": True,
        }
    )


class PublicationLanguageType(Enum):
    NL = "nl"
    FY = "fy"


class RegionCategoryType(Enum):
    DEELGEMEENTE = "DEELGEMEENTE"
    GEMEENTE = "GEMEENTE"
    KIESKRING = "KIESKRING"
    PROVINCIE = "PROVINCIE"
    PROVINCIAAL_KIESKRING = "PROVINCIAAL_KIESKRING"
    PROVINCIAAL_STEMBUREAU = "PROVINCIAAL_STEMBUREAU"
    STAAT = "STAAT"
    STEMBUREAU = "STEMBUREAU"
    WATERSCHAP = "WATERSCHAP"
    WATERSCHAP_KIESKRING = "WATERSCHAP_KIESKRING"
    WATERSCHAP_GEMEENTE = "WATERSCHAP_GEMEENTE"
    KIESCOLLEGE = "KIESCOLLEGE"


@dataclass(kw_only=True)
class RegionName:
    """
    Region name.
    """

    class Meta:
        namespace = "http://www.kiesraad.nl/extensions"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class RegisteredAppellation:
    """
    Registered appellation of the political grouping.
    """

    class Meta:
        namespace = "http://www.kiesraad.nl/extensions"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class RegisteredBy:
    """
    Person, who registered this appellation.
    """

    class Meta:
        namespace = "http://www.kiesraad.nl/extensions"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


class RejectedVotesTypeReasonCode(Enum):
    BLANCO = "blanco"
    ONGELDIG = "ongeldig"


class ReportingUnitTypeValue(Enum):
    """
    The type of reporting unit, either FixedLocation, Mobile, or 'Special'.
    """

    FIXED_LOCATION = "FixedLocation"
    MOBILE = "Mobile"
    SPECIAL = "Special"


@dataclass(kw_only=True)
class Schema:
    """The EML_NL schema version.

    Note that this differs from the OASIS EML schema version (5) on
    which EML_NL is based
    """

    class Meta:
        namespace = "http://www.kiesraad.nl/extensions"

    version: str = field(
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SharedLocation:
    """
    Boolean element, true if a given reporting unit shares this location with
    another reporting unit.
    """

    class Meta:
        namespace = "http://www.kiesraad.nl/extensions"

    value: bool = field(
        metadata={
            "required": True,
        }
    )


class UncountedVotesTypeReasonCode(Enum):
    GELDIGE_STEMPASSEN = "geldige stempassen"
    GELDIGE_VOLMACHTBEWIJZEN = "geldige volmachtbewijzen"
    GELDIGE_KIEZERSPASSEN = "geldige kiezerspassen"
    TOEGELATEN_KIEZERS = "toegelaten kiezers"
    MEER_GETELDE_STEMBILJETTEN = "meer getelde stembiljetten"
    MINDER_GETELDE_STEMBILJETTEN = "minder getelde stembiljetten"
    MEEGENOMEN_STEMBILJETTEN = "meegenomen stembiljetten"
    TE_WEINIG_UITGEREIKTE_STEMBILJETTEN = "te weinig uitgereikte stembiljetten"
    TE_VEEL_UITGEREIKTE_STEMBILJETTEN = "te veel uitgereikte stembiljetten"
    GEEN_BRIEFSTEMBILJETTEN = "geen briefstembiljetten"
    TE_VEEL_BRIEFSTEMBILJETTEN = "te veel briefstembiljetten"
    KWIJTGERAAKTE_STEMBILJETTEN = "kwijtgeraakte stembiljetten"
    GEEN_VERKLARING = "geen verklaring"
    ANDERE_VERKLARING = "andere verklaring"


@dataclass(kw_only=True)
class Committee:
    """
    Committee (e.g. central electoral committee)

    :ivar committee_category:
    :ivar committee_name: If not set, use region name
    :ivar accept_central_submissions:
    """

    class Meta:
        namespace = "http://www.kiesraad.nl/extensions"

    committee_category: CommitteeCategoryType = field(
        metadata={
            "name": "CommitteeCategory",
            "type": "Attribute",
            "required": True,
        }
    )
    committee_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CommitteeName",
            "type": "Attribute",
        },
    )
    accept_central_submissions: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AcceptCentralSubmissions",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Contests:
    """Information in addition to the eml:ContestIdentifier.

    For submission to multiple contests (provinces for EK elections,
    electoral districts for PS, TK and EP).
    """

    class Meta:
        namespace = "http://www.kiesraad.nl/extensions"

    contest: list[Contest] = field(
        default_factory=list,
        metadata={
            "name": "Contest",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class CountingMethod:
    """The way in which the votes were counted.

    Restricted to valid counting methods in Ducth electoral law.
    """

    class Meta:
        namespace = "http://www.kiesraad.nl/extensions"

    method_code: CountingMethodMethodCode = field(
        metadata={
            "name": "MethodCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ElectionSubcategory:
    """defines a subcategory to the ElectionCategory: PS1 (one electoral district), PS2 (more than one electoral district), AB1 (less than 19 seats), AB2 (19 seats or more), GR1 (less than 19 seats), GR2 (19 seats or more), TK, EK, BC, GC, and EP (not sub-categorized)"""

    class Meta:
        namespace = "http://www.kiesraad.nl/extensions"

    value: ElectionSubcategoryType = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class GenderAnnex:
    """Restricts the base EML gender type to not allow 'unknown', replacing it with
    'other'.

    Prefer using this over the original 'Gender' element.
    """

    class Meta:
        namespace = "http://www.kiesraad.nl/extensions"

    value: GenderAnnexValue = field()


@dataclass(kw_only=True)
class LivingAddress(LivingAddressType):
    class Meta:
        namespace = "http://www.kiesraad.nl/extensions"


@dataclass(kw_only=True)
class Phase:
    """The 'phase' of a count.

    PhaseCodes correspond to the names of the proces-verbaal
    """

    class Meta:
        namespace = "http://www.kiesraad.nl/extensions"

    phase_code: PhasePhaseCode = field(
        metadata={
            "name": "PhaseCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RegisteredParty:
    """
    Registered political grouping.
    """

    class Meta:
        namespace = "http://www.kiesraad.nl/extensions"

    registered_appellation: RegisteredAppellation = field(
        metadata={
            "name": "RegisteredAppellation",
            "type": "Element",
            "required": True,
        }
    )
    registered_by: Optional[RegisteredBy] = field(
        default=None,
        metadata={
            "name": "RegisteredBy",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class RejectedVotesType:
    value: int = field(
        metadata={
            "required": True,
        }
    )
    reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reason",
            "type": "Attribute",
        },
    )
    reason_code: RejectedVotesTypeReasonCode = field(
        metadata={
            "name": "ReasonCode",
            "type": "Attribute",
            "required": True,
        }
    )
    vote_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "VoteType",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ReportingUnitInvestigations:
    class Meta:
        namespace = "http://www.kiesraad.nl/extensions"

    investigation: list["ReportingUnitInvestigations.Investigation"] = field(
        default_factory=list,
        metadata={
            "name": "Investigation",
            "type": "Element",
            "max_occurs": 3,
        },
    )

    @dataclass(kw_only=True)
    class Investigation:
        value: bool = field(
            metadata={
                "required": True,
            }
        )
        reason_code: InvestigationReasonCode = field(
            metadata={
                "name": "ReasonCode",
                "type": "Attribute",
                "required": True,
            }
        )


@dataclass(kw_only=True)
class ReportingUnitType:
    """
    :ivar value: The type of reporting unit, either FixedLocation,
        Mobile, or 'Special'
    """

    class Meta:
        namespace = "http://www.kiesraad.nl/extensions"

    value: ReportingUnitTypeValue = field()


@dataclass(kw_only=True)
class UncountedVotesType:
    value: int = field(
        metadata={
            "required": True,
        }
    )
    reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "Reason",
            "type": "Attribute",
        },
    )
    reason_code: UncountedVotesTypeReasonCode = field(
        metadata={
            "name": "ReasonCode",
            "type": "Attribute",
            "required": True,
        }
    )
    vote_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "VoteType",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class InitialRejectedVotes(RejectedVotesType):
    """The initial RejectedVotes for a reporting unit or main unit which has been
    corrected.

    Should only appear for changed values in correction files
    """

    class Meta:
        namespace = "http://www.kiesraad.nl/extensions"


@dataclass(kw_only=True)
class InitialUncountedVotes(UncountedVotesType):
    """The initial Uncountedvotes (metadata) for a reporting unit or main unit
    which has been corrected.

    Should only appear for changed values in correction files
    """

    class Meta:
        namespace = "http://www.kiesraad.nl/extensions"


@dataclass(kw_only=True)
class ListData:
    """
    Additional OSV data for the candidate list.

    :ivar contests:
    :ivar publish_gender: denotes if the gender information shall be
        displayed in all documents
    :ivar publication_language: denotes if the language for publication,
        especially of the female gender: nl -&gt; v, fy -&gt; f
    :ivar belongs_to_set: list set number if there are several sets
        within a list group
    :ivar belongs_to_combination: list combination letter set by program
        3 (only 230b and 230c)
    """

    class Meta:
        namespace = "http://www.kiesraad.nl/extensions"

    contests: Optional[Contests] = field(
        default=None,
        metadata={
            "name": "Contests",
            "type": "Element",
        },
    )
    publish_gender: bool = field(
        metadata={
            "name": "PublishGender",
            "type": "Attribute",
            "required": True,
        }
    )
    publication_language: Optional[PublicationLanguageType] = field(
        default=None,
        metadata={
            "name": "PublicationLanguage",
            "type": "Attribute",
        },
    )
    belongs_to_set: Optional[int] = field(
        default=None,
        metadata={
            "name": "BelongsToSet",
            "type": "Attribute",
        },
    )
    belongs_to_combination: Optional[str] = field(
        default=None,
        metadata={
            "name": "BelongsToCombination",
            "type": "Attribute",
            "length": 1,
            "pattern": r"[a-z|A-Z]",
        },
    )


@dataclass(kw_only=True)
class Region:
    class Meta:
        namespace = "http://www.kiesraad.nl/extensions"

    region_name: RegionName = field(
        metadata={
            "name": "RegionName",
            "type": "Element",
            "required": True,
        }
    )
    committee: list[Committee] = field(
        default_factory=list,
        metadata={
            "name": "Committee",
            "type": "Element",
            "max_occurs": 3,
        },
    )
    region_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "RegionNumber",
            "type": "Attribute",
        },
    )
    region_category: RegionCategoryType = field(
        metadata={
            "name": "RegionCategory",
            "type": "Attribute",
            "required": True,
        }
    )
    roman_numerals: bool = field(
        default=False,
        metadata={
            "name": "RomanNumerals",
            "type": "Attribute",
        },
    )
    frysian_export_allowed: bool = field(
        default=False,
        metadata={
            "name": "FrysianExportAllowed",
            "type": "Attribute",
        },
    )
    superior_region_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "SuperiorRegionNumber",
            "type": "Attribute",
        },
    )
    superior_region_category: Optional[RegionCategoryType] = field(
        default=None,
        metadata={
            "name": "SuperiorRegionCategory",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class RegisteredParties:
    """
    All registered names of political groupings.
    """

    class Meta:
        namespace = "http://www.kiesraad.nl/extensions"

    registered_party: list[RegisteredParty] = field(
        default_factory=list,
        metadata={
            "name": "RegisteredParty",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ElectionTree:
    class Meta:
        namespace = "http://www.kiesraad.nl/extensions"

    region: list[Region] = field(
        default_factory=list,
        metadata={
            "name": "Region",
            "type": "Element",
            "min_occurs": 1,
        },
    )
