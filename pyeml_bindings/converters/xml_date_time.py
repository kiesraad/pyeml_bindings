from typing import Any, Optional

from xsdata.formats.converter import Converter
from xsdata.models.datatype import XmlDateTime
from xsdata.utils.dates import format_date, format_offset


def custom_format_time(
    hour: int, minute: int, second: int, fractional_second: int
) -> str:
    """Serializes a time according to ISO 8601.

    Args:
        hour (int): The hour to serialize
        minute (int): The minute to serialize
        second (int): The second to serialize
        fractional_second (int): The fractional second to serialize. Can be either nano- micro- or milliseconds.

    Returns:
        str: The time formatted according to ISO 8601 (example: 14:14:33.000)
    """
    microsecond, nano = divmod(fractional_second, 1000)
    if nano:
        return f"{hour:02d}:{minute:02d}:{second:02d}.{fractional_second:09d}"

    milli, micro = divmod(microsecond, 1000)
    if micro:
        return f"{hour:02d}:{minute:02d}:{second:02d}.{microsecond:06d}"

    return f"{hour:02d}:{minute:02d}:{second:02d}.{milli:03d}"


class FullPrecisionXmlDateTimeConverter(Converter):
    """Override the default XmlDateTimeConverter to preserve full precision when serializing datetimes

    Args:
        Converter (xsdata.formats.converter.Converter): Abstract converter class
    """

    def deserialize(self, value: Any, **kwargs: Any) -> Any:
        return XmlDateTime.from_string(value)

    def serialize(self, value: Any, **kwargs: Any) -> Optional[str]:
        if isinstance(value, XmlDateTime):
            return "{}T{}{}".format(
                format_date(value.year, value.month, value.day),
                custom_format_time(
                    value.hour, value.minute, value.second, value.fractional_second
                ),
                format_offset(value.offset),
            )
