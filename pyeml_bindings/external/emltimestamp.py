"""This file was generated by xsdata, v23.8, on 2023-10-17 11:34:35

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "urn:oasis:names:tc:evs:schema:eml:ts"


@dataclass(kw_only=True)
class AccuracyType:
    seconds: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
        }
    )
    millis: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
        }
    )
    micros: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
        }
    )


@dataclass(kw_only=True)
class CanonicalizationMethodType:
    algorithm: str = field(
        metadata={
            "name": "Algorithm",
            "type": "Attribute",
            "required": True,
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass(kw_only=True)
class DsakeyValueType:
    class Meta:
        name = "DSAKeyValueType"

    p: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "P",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
            "format": "base64",
        }
    )
    q: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Q",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
            "format": "base64",
        }
    )
    j: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "J",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
            "format": "base64",
        }
    )
    g: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "G",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
            "format": "base64",
        }
    )
    y: bytes = field(
        metadata={
            "name": "Y",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
            "required": True,
            "format": "base64",
        }
    )
    seed: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Seed",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
            "format": "base64",
        }
    )
    pgen_counter: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "PgenCounter",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
            "format": "base64",
        }
    )


@dataclass(kw_only=True)
class DigestMethodType:
    algorithm: str = field(
        metadata={
            "name": "Algorithm",
            "type": "Attribute",
            "required": True,
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass(kw_only=True)
class DigestValue:
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml:ts"

    value: bytes = field(
        metadata={
            "required": True,
            "format": "base64",
        }
    )


@dataclass(kw_only=True)
class DocumentationReferencesType:
    documentation_reference: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DocumentationReference",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class EntityNameType:
    friendly_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "FriendlyName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
        }
    )
    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
        }
    )


@dataclass(kw_only=True)
class KeyName:
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml:ts"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class MgmtData:
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml:ts"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PgpdataType:
    class Meta:
        name = "PGPDataType"

    pgpkey_id: bytes = field(
        metadata={
            "name": "PGPKeyID",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
            "required": True,
            "format": "base64",
        }
    )
    pgpkey_packet: List[bytes] = field(
        default_factory=list,
        metadata={
            "name": "PGPKeyPacket",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
            "max_occurs": 2,
            "format": "base64",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )


class QualifierType(Enum):
    OIDAS_URI = "OIDAsURI"
    OIDAS_URN = "OIDAsURN"


@dataclass(kw_only=True)
class RsakeyValueType:
    class Meta:
        name = "RSAKeyValueType"

    modulus: bytes = field(
        metadata={
            "name": "Modulus",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
            "required": True,
            "format": "base64",
        }
    )
    exponent: bytes = field(
        metadata={
            "name": "Exponent",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
            "required": True,
            "format": "base64",
        }
    )


@dataclass(kw_only=True)
class SpkidataType:
    class Meta:
        name = "SPKIDataType"

    spkisexp: List[bytes] = field(
        default_factory=list,
        metadata={
            "name": "SPKISexp",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
            "min_occurs": 1,
            "sequence": 1,
            "format": "base64",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "sequence": 1,
        }
    )


@dataclass(kw_only=True)
class SignatureMethodType:
    algorithm: str = field(
        metadata={
            "name": "Algorithm",
            "type": "Attribute",
            "required": True,
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "HMACOutputLength",
                    "type": int,
                    "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
                },
            ),
        }
    )


@dataclass(kw_only=True)
class SignatureOrTstvalueType:
    class Meta:
        name = "SignatureOrTSTValueType"

    value: bytes = field(
        metadata={
            "required": True,
            "format": "base64",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class TransformType:
    algorithm: str = field(
        metadata={
            "name": "Algorithm",
            "type": "Attribute",
            "required": True,
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "XPath",
                    "type": str,
                    "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
                },
            ),
        }
    )


@dataclass(kw_only=True)
class X509IssuerSerialType:
    x509_issuer_name: str = field(
        metadata={
            "name": "X509IssuerName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
            "required": True,
        }
    )
    x509_serial_number: int = field(
        metadata={
            "name": "X509SerialNumber",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CanonicalizationMethod(CanonicalizationMethodType):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml:ts"


@dataclass(kw_only=True)
class DsakeyValue(DsakeyValueType):
    class Meta:
        name = "DSAKeyValue"
        namespace = "urn:oasis:names:tc:evs:schema:eml:ts"


@dataclass(kw_only=True)
class DigestMethod(DigestMethodType):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml:ts"


@dataclass(kw_only=True)
class IdentifierType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    qualifier: Optional[QualifierType] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class Pgpdata(PgpdataType):
    class Meta:
        name = "PGPData"
        namespace = "urn:oasis:names:tc:evs:schema:eml:ts"


@dataclass(kw_only=True)
class RsakeyValue(RsakeyValueType):
    class Meta:
        name = "RSAKeyValue"
        namespace = "urn:oasis:names:tc:evs:schema:eml:ts"


@dataclass(kw_only=True)
class Spkidata(SpkidataType):
    class Meta:
        name = "SPKIData"
        namespace = "urn:oasis:names:tc:evs:schema:eml:ts"


@dataclass(kw_only=True)
class SignatureOrTstmethod(SignatureMethodType):
    class Meta:
        name = "SignatureOrTSTMethod"
        namespace = "urn:oasis:names:tc:evs:schema:eml:ts"


@dataclass(kw_only=True)
class SignatureOrTstvalue(SignatureOrTstvalueType):
    class Meta:
        name = "SignatureOrTSTValue"
        namespace = "urn:oasis:names:tc:evs:schema:eml:ts"


@dataclass(kw_only=True)
class Transform(TransformType):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml:ts"


@dataclass(kw_only=True)
class X509DataType:
    x509_issuer_serial: List[X509IssuerSerialType] = field(
        default_factory=list,
        metadata={
            "name": "X509IssuerSerial",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
            "sequence": 1,
        }
    )
    x509_ski: List[bytes] = field(
        default_factory=list,
        metadata={
            "name": "X509SKI",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
            "sequence": 1,
            "format": "base64",
        }
    )
    x509_subject_name: List[str] = field(
        default_factory=list,
        metadata={
            "name": "X509SubjectName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
            "sequence": 1,
        }
    )
    x509_certificate: List[bytes] = field(
        default_factory=list,
        metadata={
            "name": "X509Certificate",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
            "sequence": 1,
            "format": "base64",
        }
    )
    x509_crl: List[bytes] = field(
        default_factory=list,
        metadata={
            "name": "X509CRL",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
            "sequence": 1,
            "format": "base64",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "sequence": 1,
        }
    )


@dataclass(kw_only=True)
class KeyValueType:
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "DSAKeyValue",
                    "type": DsakeyValue,
                    "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
                },
                {
                    "name": "RSAKeyValue",
                    "type": RsakeyValue,
                    "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
                },
            ),
        }
    )


@dataclass(kw_only=True)
class ObjectIdentifierType:
    identifier: IdentifierType = field(
        metadata={
            "name": "Identifier",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
            "required": True,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
        }
    )
    documentation_references: Optional[DocumentationReferencesType] = field(
        default=None,
        metadata={
            "name": "DocumentationReferences",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
        }
    )


@dataclass(kw_only=True)
class TransformsType:
    transform: List[Transform] = field(
        default_factory=list,
        metadata={
            "name": "Transform",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class X509Data(X509DataType):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml:ts"


@dataclass(kw_only=True)
class KeyValue(KeyValueType):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml:ts"


@dataclass(kw_only=True)
class RetrievalMethodType:
    transforms: Optional[TransformsType] = field(
        default=None,
        metadata={
            "name": "Transforms",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
        }
    )
    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Attribute",
        }
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class TstxmlinfoType:
    class Meta:
        name = "TSTXMLInfoType"

    version: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
            "required": True,
        }
    )
    policy: ObjectIdentifierType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
            "required": True,
        }
    )
    serial_number: Decimal = field(
        metadata={
            "name": "serialNumber",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
            "required": True,
        }
    )
    gen_time: XmlDateTime = field(
        metadata={
            "name": "genTime",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
            "required": True,
        }
    )
    accuracy: Optional[AccuracyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
        }
    )
    ordering: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
        }
    )
    nonce: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
        }
    )
    tsa: Optional[EntityNameType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
        }
    )
    id: str = field(
        metadata={
            "name": "Id",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Transforms(TransformsType):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml:ts"


@dataclass(kw_only=True)
class ObjectType:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )
    mime_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "MimeType",
            "type": "Attribute",
        }
    )
    encoding: Optional[str] = field(
        default=None,
        metadata={
            "name": "Encoding",
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "TSTXMLInfo",
                    "type": TstxmlinfoType,
                    "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
                },
            ),
        }
    )


@dataclass(kw_only=True)
class ReferenceType:
    transforms: Optional[Transforms] = field(
        default=None,
        metadata={
            "name": "Transforms",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
        }
    )
    digest_method: DigestMethod = field(
        metadata={
            "name": "DigestMethod",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
            "required": True,
        }
    )
    digest_value: bytes = field(
        metadata={
            "name": "DigestValue",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
            "required": True,
            "format": "base64",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )
    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Attribute",
        }
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class RetrievalMethod(RetrievalMethodType):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml:ts"


@dataclass(kw_only=True)
class KeyInfoType:
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "KeyName",
                    "type": str,
                    "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
                },
                {
                    "name": "KeyValue",
                    "type": KeyValue,
                    "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
                },
                {
                    "name": "RetrievalMethod",
                    "type": RetrievalMethod,
                    "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
                },
                {
                    "name": "X509Data",
                    "type": X509Data,
                    "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
                },
                {
                    "name": "PGPData",
                    "type": Pgpdata,
                    "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
                },
                {
                    "name": "SPKIData",
                    "type": Spkidata,
                    "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
                },
                {
                    "name": "MgmtData",
                    "type": str,
                    "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
                },
            ),
        }
    )


@dataclass(kw_only=True)
class Object(ObjectType):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml:ts"


@dataclass(kw_only=True)
class Reference(ReferenceType):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml:ts"


@dataclass(kw_only=True)
class TstxmlinfoReference(ReferenceType):
    class Meta:
        name = "TSTXMLInfoReference"
        namespace = "urn:oasis:names:tc:evs:schema:eml:ts"


@dataclass(kw_only=True)
class KeyInfo(KeyInfoType):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml:ts"


@dataclass(kw_only=True)
class TimestampedInfoType:
    canonicalization_method: CanonicalizationMethod = field(
        metadata={
            "name": "CanonicalizationMethod",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
            "required": True,
        }
    )
    signature_or_tstmethod: SignatureOrTstmethod = field(
        metadata={
            "name": "SignatureOrTSTMethod",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
            "required": True,
        }
    )
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
            "required": True,
        }
    )
    tstxmlinfo_reference: Optional[TstxmlinfoReference] = field(
        default=None,
        metadata={
            "name": "TSTXMLInfoReference",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class TimestampedInfo(TimestampedInfoType):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml:ts"


@dataclass(kw_only=True)
class TimestampType:
    timestamped_info: TimestampedInfo = field(
        metadata={
            "name": "TimestampedInfo",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
            "required": True,
        }
    )
    signature_or_tstvalue: SignatureOrTstvalue = field(
        metadata={
            "name": "SignatureOrTSTValue",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
            "required": True,
        }
    )
    key_info: Optional[KeyInfo] = field(
        default=None,
        metadata={
            "name": "KeyInfo",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
        }
    )
    object_value: Object = field(
        metadata={
            "name": "Object",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:evs:schema:eml:ts",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class Timestamp(TimestampType):
    class Meta:
        namespace = "urn:oasis:names:tc:evs:schema:eml:ts"
