from pathlib import Path
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import XmlSerializer
from pyeml_bindings import Eml110a, Eml230, Eml510, Eml520
from pyeml_bindings.namespace import NAMESPACE
import xml.etree.ElementTree as ET
from formencode.doctest_xml_compare import xml_compare
from sys import stdout
import pytest
import itertools
import glob
import re


def parsing_roundtrip_same(parser, serializer, reporter, path_to_eml, type) -> bool:
    xml_in_string = Path(path_to_eml).read_text(encoding="utf-8")
    parsed = parser.from_string(xml_in_string, type)
    xml_out_string = serializer.render(parsed, ns_map=NAMESPACE)

    # Compare the strings by comparing the elementtrees
    xml_in_tree = ET.fromstring(xml_in_string)
    xml_out_tree = ET.fromstring(xml_out_string)

    return xml_compare(xml_in_tree, xml_out_tree, reporter)


parser = XmlParser(ParserConfig(fail_on_unknown_properties=False))
serializer = XmlSerializer()
reporter = lambda x: stdout.write(x + "\n")
files = glob.glob(f"data/**/*.eml.xml", recursive=True)

test_cases = zip(
    itertools.repeat(parser),
    itertools.repeat(serializer),
    itertools.repeat(reporter),
    files,
)

p_110a = re.compile(r"[Vv]erkiezingsdefinitie_")
p_230 = re.compile(r"[Kk]andidatenlijsten_")
p_510 = re.compile(r"[Tt]elling|[Tt]otaaltelling_")
p_520 = re.compile(r"[Rr]esultaat_")


@pytest.mark.parametrize(
    "parser, serializer, reporter, file",
    test_cases,
)
def test_roundtrip(parser, serializer, reporter, file):
    name = Path(file).name
    if p_110a.match(name):
        assert parsing_roundtrip_same(parser, serializer, reporter, file, Eml110a)
    elif p_230.match(name):
        assert parsing_roundtrip_same(parser, serializer, reporter, file, Eml230)
    elif p_510.match(name):
        assert parsing_roundtrip_same(parser, serializer, reporter, file, Eml510)
    elif p_520.match(name):
        assert parsing_roundtrip_same(parser, serializer, reporter, file, Eml520)
    else:
        pytest.skip("EML type not implemented")
