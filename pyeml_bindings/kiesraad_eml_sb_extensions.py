from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.kiesraad.nl/sb-extensions"


class AccessibilityPropertiesTypeGuidelines(Enum):
    INSIDE_AND_OUTSIDE = "inside and outside"
    OUTSIDE = "outside"
    INSIDE = "inside"
    NOT_PRESENT = "not present"


class AccessibilityPropertiesTypeSignLanguageInterpreter(Enum):
    AT_LOCATION = "at location"
    REMOTE = "remote"
    NOT_PRESENT = "not present"


class BuildingUsageType(Enum):
    """Building usage type according to the BAG.

    (see
    https://www.amsterdam.nl/stelselpedia/bag-index/handboek-inwinnen/introductie-bag/registratie/gebruiksdoel/)
    """

    WONEN = "Wonen"
    BIJEENKOMST = "Bijeenkomst"
    WINKEL = "Winkel"
    GEZONDHEIDSZORG = "Gezondheidszorg"
    KANTOOR = "Kantoor"
    LOGIES = "Logies"
    INDUSTRIE = "Industrie"
    ONDERWIJS = "Onderwijs"
    SPORT = "Sport"
    OVERIG = "Overig"
    CEL = "Cel"


@dataclass(kw_only=True)
class MunicipalityContactDetails:
    class Meta:
        namespace = "http://www.kiesraad.nl/sb-extensions"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class MunicipalityElectionSite:
    class Meta:
        namespace = "http://www.kiesraad.nl/sb-extensions"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"https?://.+",
        },
    )


@dataclass(kw_only=True)
class AccessibilityPropertiesType:
    accessible_public_transport: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AccessiblePublicTransport",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/sb-extensions",
        },
    )
    accessible_toilet: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AccessibleToilet",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/sb-extensions",
        },
    )
    host_present: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HostPresent",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/sb-extensions",
        },
    )
    guidelines: Optional[AccessibilityPropertiesTypeGuidelines] = field(
        default=None,
        metadata={
            "name": "Guidelines",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/sb-extensions",
        },
    )
    voting_template: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VotingTemplate",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/sb-extensions",
        },
    )
    braille_candidate_list: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BrailleCandidateList",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/sb-extensions",
        },
    )
    large_lettered_candidate_list: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LargeLetteredCandidateList",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/sb-extensions",
        },
    )
    sign_language_interpreter: Optional[
        AccessibilityPropertiesTypeSignLanguageInterpreter
    ] = field(
        default=None,
        metadata={
            "name": "SignLanguageInterpreter",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/sb-extensions",
        },
    )
    sign_language_polling_station_member: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SignLanguagePollingStationMember",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/sb-extensions",
        },
    )
    acoustics_for_hearing_impaired: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AcousticsForHearingImpaired",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/sb-extensions",
        },
    )
    low_stimulus_environment: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LowStimulusEnvironment",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/sb-extensions",
        },
    )
    other: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Other",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/sb-extensions",
        },
    )


@dataclass(kw_only=True)
class Location:
    class Meta:
        namespace = "http://www.kiesraad.nl/sb-extensions"

    bagid: Optional[str] = field(
        default=None,
        metadata={
            "name": "BAGId",
            "type": "Element",
            "pattern": r"\d{16}",
        },
    )
    street_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "StreetName",
            "type": "Element",
        },
    )
    number: Optional[int] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Element",
        },
    )
    letter: Optional[str] = field(
        default=None,
        metadata={
            "name": "Letter",
            "type": "Element",
        },
    )
    number_addition: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumberAddition",
            "type": "Element",
        },
    )
    postal_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PostalCode",
            "type": "Element",
            "pattern": r"\d{4} [A-Z]{2}",
        },
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Element",
        },
    )
    additional_address_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdditionalAddressInformation",
            "type": "Element",
        },
    )
    building_usage: Optional[BuildingUsageType] = field(
        default=None,
        metadata={
            "name": "BuildingUsage",
            "type": "Element",
        },
    )
    district_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "DistrictName",
            "type": "Element",
        },
    )
    district_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "DistrictCode",
            "type": "Element",
            "pattern": r"WK\d{6}",
        },
    )
    neighbourhood_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "NeighbourhoodName",
            "type": "Element",
        },
    )
    neighbourhood_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "NeighbourhoodCode",
            "type": "Element",
            "pattern": r"BU\d{8}",
        },
    )
    website: Optional[str] = field(
        default=None,
        metadata={
            "name": "Website",
            "type": "Element",
            "pattern": r"https?://.+",
        },
    )
    open_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "OpenTime",
            "type": "Element",
        },
    )
    closing_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ClosingTime",
            "type": "Element",
        },
    )
    rdx: Optional[str] = field(
        default=None,
        metadata={
            "name": "RDx",
            "type": "Element",
            "pattern": r"\d{1,6}(.\d{1,})?",
        },
    )
    rdy: Optional[str] = field(
        default=None,
        metadata={
            "name": "RDy",
            "type": "Element",
            "pattern": r"\d{1,6}(.\d{1,})?",
        },
    )
    latitude: Optional[str] = field(
        default=None,
        metadata={
            "name": "Latitude",
            "type": "Element",
            "pattern": r"\d{1,2}\.\d{4,}",
        },
    )
    longitude: Optional[str] = field(
        default=None,
        metadata={
            "name": "Longitude",
            "type": "Element",
            "pattern": r"\d{1,2}\.\d{4,}",
        },
    )
    counting_location: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CountingLocation",
            "type": "Element",
        },
    )
    accessibility: Optional["Location.Accessibility"] = field(
        default=None,
        metadata={
            "name": "Accessibility",
            "type": "Element",
        },
    )
    other_info: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherInfo",
            "type": "Element",
        },
    )

    @dataclass(kw_only=True)
    class Accessibility:
        accessible: bool = field(
            metadata={
                "name": "Accessible",
                "type": "Element",
                "required": True,
            }
        )
        accessibility_properties: Optional[AccessibilityPropertiesType] = (
            field(
                default=None,
                metadata={
                    "name": "AccessibilityProperties",
                    "type": "Element",
                },
            )
        )
