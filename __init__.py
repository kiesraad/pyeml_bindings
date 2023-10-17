"""This file was generated by xsdata, v23.8, on 2023-10-17 11:34:35

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from pyeml_bindings.emlcore_kiesraad_strict import (
    Accepted,
    Affiliation,
    AffiliationIdentifier,
    AffiliationIdentifierStructure,
    AffiliationStructure,
    Agent,
    AgentIdentifier,
    AgentIdentifierStructure,
    AgentStructure,
    Area,
    AreaStructure,
    AuditInformation,
    AuditInformationStructure,
    AuthorityIdentifier,
    AuthorityIdentifierStructure,
    BallotIdentifier,
    BallotIdentifierRange,
    BallotIdentifierRangeStructure,
    BallotIdentifierStructure,
    BinaryItemStructure,
    BinaryFormat,
    Candidate,
    CandidateIdentifier,
    CandidateIdentifierStructure,
    CandidateStructure,
    Channel,
    ChannelStructure,
    ComplexDateRangeStructure,
    ContactDetails,
    ContactDetailsStructure,
    ContestIdentifier,
    ContestIdentifierStructure,
    CountMetric,
    CountMetricStructure,
    CountQualifier,
    CountQualifierStructure,
    CountingAlgorithm,
    DocumentIdentifier,
    DocumentIdentifierStructure,
    Emlstructure,
    ElectionGroupStructure,
    ElectionIdentifier,
    ElectionIdentifierStructure,
    ElectionStatement,
    EmailStructure,
    Endorsement,
    EventIdentifier,
    EventIdentifierStructure,
    EventQualifier,
    EventQualifierStructure,
    Gender,
    GenderType,
    IncomingGenericCommunicationStructure,
    InternalGenericCommunicationStructure,
    Logo,
    LogoStructure,
    ManagingAuthority,
    ManagingAuthorityStructure,
    MaxVotes,
    MessageType,
    MessagesStructure,
    MinVotes,
    NominatingOfficer,
    NominatingOfficerStructure,
    NumberInSequence,
    NumberOfPositions,
    OutgoingGenericCommunicationStructure,
    Period,
    PeriodStructure,
    PeriodStructurePermanent,
    PersonName as EmlcorePersonName,
    PollingDistrict,
    PollingDistrictStructure,
    PollingPlace,
    PollingPlaceStructure,
    Position,
    PositionStructure,
    PreviousElectoralAddress,
    ProcessingUnitStructure,
    ProcessingUnitStructureRole,
    Profile,
    Proposal,
    ProposalIdentifier,
    ProposalIdentifierStructure,
    ProposalItem,
    ProposalItemStructure,
    ProposalStructure,
    Proposer,
    ProposerStructure,
    ProposerStructureCategory,
    Proxy,
    ProxyStructure,
    ReferendumOptionIdentifier,
    ReferendumOptionIdentifierStructure,
    ReportingUnitIdentifier,
    ReportingUnitIdentifierStructure,
    ResponsibleOfficer,
    ResponsibleOfficerStructure,
    ResultsReportedStructure,
    ScrutinyRequirement,
    Seal,
    SealStructure,
    SequenceNumber,
    SimpleDateRangeStructure,
    SupporterIdentifier,
    SupporterIdentifierStructure,
    SupporterStructure,
    TelephoneStructure,
    TransactionId,
    Vtoken,
    VtokenQualified,
    VtokenQualifiedStructure,
    VtokenStructure,
    VoterIdentificationStructure,
    VoterInformationStructure,
    VoterInformationStructureGender,
    VoterName,
    VotingChannel,
    VotingChannelType,
    VotingMethod,
    VotingMethodType,
    WriteIn,
    WriteInType,
    YesNoType,
)
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
from pyeml_bindings.kiesraad_eml_extensions import (
    AffiliationType,
    Committee,
    CommitteeCategoryType,
    Contest,
    Contests,
    CreatedByAuthority,
    CreationDateTime,
    DateOfBirthAnnex,
    ElectionCategoryType,
    ElectionDate,
    ElectionDomain,
    ElectionSubcategory,
    ElectionSubcategoryType,
    ElectionTree,
    ListData,
    LivingAddress,
    LivingAddressType,
    NationalIdentificationNumber,
    NominationDate,
    NumberOfSeats,
    PreferenceThreshold,
    PublicationLanguageType,
    Region,
    RegionCategoryType,
    RegionName,
    RegisteredAppellation,
    RegisteredBy,
    RegisteredParties,
    RegisteredParty,
)
from pyeml_bindings.kiesraad_eml_restrictions import (
    AddressStructureRestrictedKr,
    AffiliationIdentifierStructureKr,
    AffiliationStructureKr,
    AgentStructureKr,
    AgentStructureKrRole,
    AuthorityIdentifierStructureKr,
    CandidateIdentifierStructureKr,
    CandidateStructureKr,
    ContactDetailsStructureKr,
    ContestIdentifierStructureKr,
    EmlstructureKr,
    ElectionIdentifierStructureKr,
    GenericMailingAddressStructureKr,
    GenericQualifyingAddressStructureKr,
    MailingAddressStructureKr,
    ManagingAuthorityStructureKr,
    MinimalQualifyingAddressStructureKr,
    QualifyingAddressStructureKr,
    ReportingUnitIdentifierStructureKr,
)
from pyeml_bindings.mod_210_nomination_kiesraad_strict import (
    AffiliationIdentifierStructure210,
    AffiliationStructure210,
    CandidateIdentifierStructure210,
    CandidateStructure210,
    ContestIdentifierStructure210,
    Emlstructure210,
    ElectionIdentifierStructure210,
    Nomination,
    ProposerStructureKr,
    ProposerStructureRestricted,
    ProposerStructureRestrictedJobTitle,
)
from pyeml_bindings.mod_230_candidatelist_kiesraad_strict import (
    CandidateList,
    Emlstructure230,
    Emlstructure230Id,
    ElectionIdentifierStructure230,
)
from pyeml_bindings.mod_510_count_kiesraad_strict import (
    AffiliationIdentifierStructure510,
    CandidateIdentifierStructure510,
    CandidateStructure510,
    Count,
    Emlstructure510,
    ElectionIdentifierStructure510,
    RejectedVotesReasonCode,
    ReportingUnitVotes,
    UncountedVotesReasonCode,
)
from pyeml_bindings.mod_520_result_kiesraad_strict import (
    AffiliationIdentifierStructure520,
    CandidateIdentifierStructure520,
    CandidateStructure520,
    Emlstructure520,
    ElectionIdentifierStructure520,
    Result,
    SelectionRanking,
)
from pyeml_bindings.x_al_kiesraad_strict import (
    Address,
    AddressDetails,
    AddressLine,
    AddressLinesType,
    AdministrativeArea,
    BuildingNameType,
    BuildingNameTypeTypeOccurrence,
    Country,
    CountryName,
    CountryNameCodeType,
    CountryType,
    Department,
    DependentLocalityNumberNameNumberOccurrence,
    DependentLocalityType,
    FirmType,
    GenericCountryType,
    GenericLocalityType,
    LargeMailUserType,
    Locality,
    LocalityNameType,
    LocalityType,
    LocalityType110,
    LocalityTypeUsageType,
    MailStopType,
    MinimalCountryType,
    MinimalLocalityType,
    PostBox,
    PostOffice,
    PostOfficeNumberIndicatorOccurrence,
    PostalCode,
    PostalRouteType,
    Premise,
    PremiseNameTypeOccurrence,
    PremiseNumber,
    PremiseNumberPrefix,
    PremiseNumberRangeIndicatorOccurence,
    PremiseNumberRangeNumberRangeOccurence,
    PremiseNumberSuffix,
    PremiseNumberIndicatorOccurrence,
    PremiseNumberNumberType,
    PremiseNumberNumberTypeOccurrence,
    SubPremiseNameTypeOccurrence,
    SubPremiseNumberIndicatorOccurrence,
    SubPremiseNumberNumberTypeOccurrence,
    SubPremiseType,
    Thoroughfare,
    ThoroughfareLeadingTypeType,
    ThoroughfareNameType,
    ThoroughfareNumber,
    ThoroughfareNumberPrefix,
    ThoroughfareNumberRangeIndicatorOccurrence,
    ThoroughfareNumberRangeNumberRangeOccurrence,
    ThoroughfareNumberRangeRangeType,
    ThoroughfareNumberSuffix,
    ThoroughfareNumberIndicatorOccurrence,
    ThoroughfareNumberNumberOccurrence,
    ThoroughfareNumberNumberType,
    ThoroughfarePostDirectionType,
    ThoroughfarePreDirectionType,
    ThoroughfareTrailingTypeType,
    ThoroughfareDependentThoroughfares,
    XAl,
)
from pyeml_bindings.x_nl_kiesraad_strict import (
    Function,
    JointPersonName,
    NameDetails,
    NameDetails1,
    NameLineType,
    OrganisationNameDetails,
    OrganisationNameDetails1,
    PersonName as XNlPersonName,
    XNl,
)
from pyeml_bindings.ns_map import NAMESPACE

__all__ = [
    "Accepted",
    "Affiliation",
    "AffiliationIdentifier",
    "AffiliationIdentifierStructure",
    "AffiliationStructure",
    "Agent",
    "AgentIdentifier",
    "AgentIdentifierStructure",
    "AgentStructure",
    "Area",
    "AreaStructure",
    "AuditInformation",
    "AuditInformationStructure",
    "AuthorityIdentifier",
    "AuthorityIdentifierStructure",
    "BallotIdentifier",
    "BallotIdentifierRange",
    "BallotIdentifierRangeStructure",
    "BallotIdentifierStructure",
    "BinaryItemStructure",
    "BinaryFormat",
    "Candidate",
    "CandidateIdentifier",
    "CandidateIdentifierStructure",
    "CandidateStructure",
    "Channel",
    "ChannelStructure",
    "ComplexDateRangeStructure",
    "ContactDetails",
    "ContactDetailsStructure",
    "ContestIdentifier",
    "ContestIdentifierStructure",
    "CountMetric",
    "CountMetricStructure",
    "CountQualifier",
    "CountQualifierStructure",
    "CountingAlgorithm",
    "DocumentIdentifier",
    "DocumentIdentifierStructure",
    "Emlstructure",
    "ElectionGroupStructure",
    "ElectionIdentifier",
    "ElectionIdentifierStructure",
    "ElectionStatement",
    "EmailStructure",
    "Endorsement",
    "EventIdentifier",
    "EventIdentifierStructure",
    "EventQualifier",
    "EventQualifierStructure",
    "Gender",
    "GenderType",
    "IncomingGenericCommunicationStructure",
    "InternalGenericCommunicationStructure",
    "Logo",
    "LogoStructure",
    "ManagingAuthority",
    "ManagingAuthorityStructure",
    "MaxVotes",
    "MessageType",
    "MessagesStructure",
    "MinVotes",
    "NominatingOfficer",
    "NominatingOfficerStructure",
    "NumberInSequence",
    "NumberOfPositions",
    "OutgoingGenericCommunicationStructure",
    "Period",
    "PeriodStructure",
    "PeriodStructurePermanent",
    "EmlcorePersonName",
    "PollingDistrict",
    "PollingDistrictStructure",
    "PollingPlace",
    "PollingPlaceStructure",
    "Position",
    "PositionStructure",
    "PreviousElectoralAddress",
    "ProcessingUnitStructure",
    "ProcessingUnitStructureRole",
    "Profile",
    "Proposal",
    "ProposalIdentifier",
    "ProposalIdentifierStructure",
    "ProposalItem",
    "ProposalItemStructure",
    "ProposalStructure",
    "Proposer",
    "ProposerStructure",
    "ProposerStructureCategory",
    "Proxy",
    "ProxyStructure",
    "ReferendumOptionIdentifier",
    "ReferendumOptionIdentifierStructure",
    "ReportingUnitIdentifier",
    "ReportingUnitIdentifierStructure",
    "ResponsibleOfficer",
    "ResponsibleOfficerStructure",
    "ResultsReportedStructure",
    "ScrutinyRequirement",
    "Seal",
    "SealStructure",
    "SequenceNumber",
    "SimpleDateRangeStructure",
    "SupporterIdentifier",
    "SupporterIdentifierStructure",
    "SupporterStructure",
    "TelephoneStructure",
    "TransactionId",
    "Vtoken",
    "VtokenQualified",
    "VtokenQualifiedStructure",
    "VtokenStructure",
    "VoterIdentificationStructure",
    "VoterInformationStructure",
    "VoterInformationStructureGender",
    "VoterName",
    "VotingChannel",
    "VotingChannelType",
    "VotingMethod",
    "VotingMethodType",
    "WriteIn",
    "WriteInType",
    "YesNoType",
    "AuthorityAddressStructure",
    "ElectoralAddressStructure",
    "MailingAddressStructure",
    "OfficialAddressStructure",
    "PersonNameStructure",
    "PhysicalAddressStructure",
    "PostalLocationStructure",
    "ProxyAddressStructure",
    "QualifyingAddressStructure",
    "AffiliationType",
    "Committee",
    "CommitteeCategoryType",
    "Contest",
    "Contests",
    "CreatedByAuthority",
    "CreationDateTime",
    "DateOfBirthAnnex",
    "ElectionCategoryType",
    "ElectionDate",
    "ElectionDomain",
    "ElectionSubcategory",
    "ElectionSubcategoryType",
    "ElectionTree",
    "ListData",
    "LivingAddress",
    "LivingAddressType",
    "NationalIdentificationNumber",
    "NominationDate",
    "NumberOfSeats",
    "PreferenceThreshold",
    "PublicationLanguageType",
    "Region",
    "RegionCategoryType",
    "RegionName",
    "RegisteredAppellation",
    "RegisteredBy",
    "RegisteredParties",
    "RegisteredParty",
    "AddressStructureRestrictedKr",
    "AffiliationIdentifierStructureKr",
    "AffiliationStructureKr",
    "AgentStructureKr",
    "AgentStructureKrRole",
    "AuthorityIdentifierStructureKr",
    "CandidateIdentifierStructureKr",
    "CandidateStructureKr",
    "ContactDetailsStructureKr",
    "ContestIdentifierStructureKr",
    "EmlstructureKr",
    "ElectionIdentifierStructureKr",
    "GenericMailingAddressStructureKr",
    "GenericQualifyingAddressStructureKr",
    "MailingAddressStructureKr",
    "ManagingAuthorityStructureKr",
    "MinimalQualifyingAddressStructureKr",
    "QualifyingAddressStructureKr",
    "ReportingUnitIdentifierStructureKr",
    "AffiliationIdentifierStructure210",
    "AffiliationStructure210",
    "CandidateIdentifierStructure210",
    "CandidateStructure210",
    "ContestIdentifierStructure210",
    "Emlstructure210",
    "ElectionIdentifierStructure210",
    "Nomination",
    "ProposerStructureKr",
    "ProposerStructureRestricted",
    "ProposerStructureRestrictedJobTitle",
    "CandidateList",
    "Emlstructure230",
    "Emlstructure230Id",
    "ElectionIdentifierStructure230",
    "AffiliationIdentifierStructure510",
    "CandidateIdentifierStructure510",
    "CandidateStructure510",
    "Count",
    "Emlstructure510",
    "ElectionIdentifierStructure510",
    "RejectedVotesReasonCode",
    "ReportingUnitVotes",
    "UncountedVotesReasonCode",
    "AffiliationIdentifierStructure520",
    "CandidateIdentifierStructure520",
    "CandidateStructure520",
    "Emlstructure520",
    "ElectionIdentifierStructure520",
    "Result",
    "SelectionRanking",
    "Address",
    "AddressDetails",
    "AddressLine",
    "AddressLinesType",
    "AdministrativeArea",
    "BuildingNameType",
    "BuildingNameTypeTypeOccurrence",
    "Country",
    "CountryName",
    "CountryNameCodeType",
    "CountryType",
    "Department",
    "DependentLocalityNumberNameNumberOccurrence",
    "DependentLocalityType",
    "FirmType",
    "GenericCountryType",
    "GenericLocalityType",
    "LargeMailUserType",
    "Locality",
    "LocalityNameType",
    "LocalityType",
    "LocalityType110",
    "LocalityTypeUsageType",
    "MailStopType",
    "MinimalCountryType",
    "MinimalLocalityType",
    "PostBox",
    "PostOffice",
    "PostOfficeNumberIndicatorOccurrence",
    "PostalCode",
    "PostalRouteType",
    "Premise",
    "PremiseNameTypeOccurrence",
    "PremiseNumber",
    "PremiseNumberPrefix",
    "PremiseNumberRangeIndicatorOccurence",
    "PremiseNumberRangeNumberRangeOccurence",
    "PremiseNumberSuffix",
    "PremiseNumberIndicatorOccurrence",
    "PremiseNumberNumberType",
    "PremiseNumberNumberTypeOccurrence",
    "SubPremiseNameTypeOccurrence",
    "SubPremiseNumberIndicatorOccurrence",
    "SubPremiseNumberNumberTypeOccurrence",
    "SubPremiseType",
    "Thoroughfare",
    "ThoroughfareLeadingTypeType",
    "ThoroughfareNameType",
    "ThoroughfareNumber",
    "ThoroughfareNumberPrefix",
    "ThoroughfareNumberRangeIndicatorOccurrence",
    "ThoroughfareNumberRangeNumberRangeOccurrence",
    "ThoroughfareNumberRangeRangeType",
    "ThoroughfareNumberSuffix",
    "ThoroughfareNumberIndicatorOccurrence",
    "ThoroughfareNumberNumberOccurrence",
    "ThoroughfareNumberNumberType",
    "ThoroughfarePostDirectionType",
    "ThoroughfarePreDirectionType",
    "ThoroughfareTrailingTypeType",
    "ThoroughfareDependentThoroughfares",
    "XAl",
    "Function",
    "JointPersonName",
    "NameDetails",
    "NameDetails1",
    "NameLineType",
    "OrganisationNameDetails",
    "OrganisationNameDetails1",
    "XNlPersonName",
    "XNl",
    "NAMESPACE",
]
