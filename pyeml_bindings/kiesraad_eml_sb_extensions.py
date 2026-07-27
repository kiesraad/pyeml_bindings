from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

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
    """
    Building usage type according to the BAG. (see
    https://www.amsterdam.nl/stelselpedia/bag-index/handboek-inwinnen/introductie-bag/registratie/gebruiksdoel/).
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

    value: str = field(default="")


@dataclass(kw_only=True)
class MunicipalityElectionSite:
    class Meta:
        namespace = "http://www.kiesraad.nl/sb-extensions"

    value: str = field(
        default="",
        metadata={
            "pattern": r"https?://.+",
        },
    )


@dataclass(kw_only=True)
class AccessibilityPropertiesType:
    accessible_public_transport: None | bool = field(
        default=None,
        metadata={
            "name": "AccessiblePublicTransport",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/sb-extensions",
        },
    )
    accessible_toilet: None | bool = field(
        default=None,
        metadata={
            "name": "AccessibleToilet",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/sb-extensions",
        },
    )
    host_present: None | bool = field(
        default=None,
        metadata={
            "name": "HostPresent",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/sb-extensions",
        },
    )
    guidelines: None | AccessibilityPropertiesTypeGuidelines = field(
        default=None,
        metadata={
            "name": "Guidelines",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/sb-extensions",
        },
    )
    voting_template: None | bool = field(
        default=None,
        metadata={
            "name": "VotingTemplate",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/sb-extensions",
        },
    )
    braille_candidate_list: None | bool = field(
        default=None,
        metadata={
            "name": "BrailleCandidateList",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/sb-extensions",
        },
    )
    large_lettered_candidate_list: None | bool = field(
        default=None,
        metadata={
            "name": "LargeLetteredCandidateList",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/sb-extensions",
        },
    )
    sign_language_interpreter: (
        None | AccessibilityPropertiesTypeSignLanguageInterpreter
    ) = field(
        default=None,
        metadata={
            "name": "SignLanguageInterpreter",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/sb-extensions",
        },
    )
    sign_language_polling_station_member: None | bool = field(
        default=None,
        metadata={
            "name": "SignLanguagePollingStationMember",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/sb-extensions",
        },
    )
    acoustics_for_hearing_impaired: None | bool = field(
        default=None,
        metadata={
            "name": "AcousticsForHearingImpaired",
            "type": "Element",
            "namespace": "http://www.kiesraad.nl/sb-extensions",
        },
    )
    low_stimulus_environment: None | bool = field(
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

    bagid: None | str = field(
        default=None,
        metadata={
            "name": "BAGId",
            "type": "Element",
            "pattern": r"\d{16}",
        },
    )
    street_name: None | str = field(
        default=None,
        metadata={
            "name": "StreetName",
            "type": "Element",
        },
    )
    number: None | int = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Element",
        },
    )
    letter: None | str = field(
        default=None,
        metadata={
            "name": "Letter",
            "type": "Element",
        },
    )
    number_addition: None | str = field(
        default=None,
        metadata={
            "name": "NumberAddition",
            "type": "Element",
        },
    )
    postal_code: None | str = field(
        default=None,
        metadata={
            "name": "PostalCode",
            "type": "Element",
            "pattern": r"\d{4} [A-Z]{2}",
        },
    )
    city: None | str = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Element",
        },
    )
    additional_address_information: None | str = field(
        default=None,
        metadata={
            "name": "AdditionalAddressInformation",
            "type": "Element",
        },
    )
    building_usage: None | BuildingUsageType = field(
        default=None,
        metadata={
            "name": "BuildingUsage",
            "type": "Element",
        },
    )
    district_name: None | str = field(
        default=None,
        metadata={
            "name": "DistrictName",
            "type": "Element",
        },
    )
    district_code: None | str = field(
        default=None,
        metadata={
            "name": "DistrictCode",
            "type": "Element",
            "pattern": r"WK\d{6}",
        },
    )
    neighbourhood_name: None | str = field(
        default=None,
        metadata={
            "name": "NeighbourhoodName",
            "type": "Element",
        },
    )
    neighbourhood_code: None | str = field(
        default=None,
        metadata={
            "name": "NeighbourhoodCode",
            "type": "Element",
            "pattern": r"BU\d{8}",
        },
    )
    website: None | str = field(
        default=None,
        metadata={
            "name": "Website",
            "type": "Element",
            "pattern": r"https?://.+",
        },
    )
    open_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "OpenTime",
            "type": "Element",
        },
    )
    closing_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "ClosingTime",
            "type": "Element",
        },
    )
    rdx: None | str = field(
        default=None,
        metadata={
            "name": "RDx",
            "type": "Element",
            "pattern": r"\d{1,6}(.\d{1,})?",
        },
    )
    rdy: None | str = field(
        default=None,
        metadata={
            "name": "RDy",
            "type": "Element",
            "pattern": r"\d{1,6}(.\d{1,})?",
        },
    )
    latitude: None | str = field(
        default=None,
        metadata={
            "name": "Latitude",
            "type": "Element",
            "pattern": r"\d{1,2}\.\d{4,}",
        },
    )
    longitude: None | str = field(
        default=None,
        metadata={
            "name": "Longitude",
            "type": "Element",
            "pattern": r"\d{1,2}\.\d{4,}",
        },
    )
    counting_location: None | bool = field(
        default=None,
        metadata={
            "name": "CountingLocation",
            "type": "Element",
        },
    )
    accessibility: None | Location.Accessibility = field(
        default=None,
        metadata={
            "name": "Accessibility",
            "type": "Element",
        },
    )
    other_info: None | str = field(
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
            }
        )
        accessibility_properties: None | AccessibilityPropertiesType = field(
            default=None,
            metadata={
                "name": "AccessibilityProperties",
                "type": "Element",
            },
        )
