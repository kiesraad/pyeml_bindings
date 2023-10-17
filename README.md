# Python bindings for the EML_NL Standard
Data bindings for the EML_NL Standard to load EML_NL files into Python [dataclasses](https://docs.python.org/3/library/dataclasses.html) with correct structure, datatypes and typehints following the [EML_NL Xml Schema Definitions](https://www.kiesraad.nl/adviezen-en-publicaties/formulieren/2016/osv/eml-bestanden/eml_nl_1_2_1-xsd). Type hints can be staticically checked using [mypy](https://mypy-lang.org/) or [pyright](https://github.com/microsoft/pyright).

## Requirements
- At least Python version 3.10 for the [KW_ONLY](https://docs.python.org/3/library/dataclasses.html#dataclasses.KW_ONLY) type annotations for dataclasses. This is so that non-nullable fields can be marked as mandatory (see [here](https://xsdata.readthedocs.io/en/latest/faq/why-non-nullable-fields-are-marked-as-optional.html)).
- [xsData](https://github.com/tefra/xsdata) for parsing using these databindings (`pip install xsdata`)

## Codegen
These bindings are mostly generated using [xsData](https://xsdata.readthedocs.io) with some minor changes where needed. See commit history for these changes.

## Usage
Make sure that xsData is installed. Using example file [`Telling_PS2023_Flevoland_gemeente_Almere.eml.xml`](https://data.overheid.nl/dataset/verkiezingsuitslag-provinciale-staten-2023#panel-resources) which has EML id 510b:

```python
from pathlib import Path
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from pyeml_bindings import Eml510, NAMESPACE

# Create a parser object, can optionally be given extra config, see xsData docs
parser = XmlParser()

# Parse the eml file, specifying the dataclass to parse to.
eml = parser.from_path(Path("Telling_PS2023_Flevoland_gemeente_Almere.eml.xml"), Eml510)

# We can now access the data using standard Python syntax
# prints "Provinciale Staten Flevoland 2023"
print(eml.count.election.election_identifier.election_name)

# Or change some of the fields
eml.count.election.contests.contest[0].total_votes.cast = 1234

# And write back to EML using a serializer
serializer = XmlSerializer()

with open(Path("output.xml"), "w") as out_file:
    # We can optionally pass the NAMESPACE from the bindings to the write function
    # to use the same namespace prefixes.
    # If we don't, we still get back valid EML but with ns0, ns1 etc.
    serializer.write(out=out_file, obj=eml, ns_map=NAMESPACE)
```
