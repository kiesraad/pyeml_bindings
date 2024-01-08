# Python bindings for the EML_NL Standard
Data bindings for the EML_NL Standard to load EML_NL files into Python [dataclasses](https://docs.python.org/3/library/dataclasses.html) with correct structure, datatypes and typehints following the [EML_NL Xml Schema Definitions](https://www.kiesraad.nl/adviezen-en-publicaties/formulieren/2016/osv/eml-bestanden/eml_nl_1_2_1-xsd). Type hints can be statically checked using [mypy](https://mypy-lang.org/) or [pyright](https://github.com/microsoft/pyright).

## Requirements
- At least Python version 3.10 for the [KW_ONLY](https://docs.python.org/3/library/dataclasses.html#dataclasses.KW_ONLY) type annotations for dataclasses. This is so that non-nullable fields can be marked as mandatory (refer to [xsdata documentation](https://xsdata.readthedocs.io/en/latest/faq/why-non-nullable-fields-are-marked-as-optional.html)).
- [xsData](https://github.com/tefra/xsdata) for parsing using these data bindings.

For running tests, additionally:
- [pytest](https://docs.pytest.org/) for the test framework.
- [formencode](http://www.formencode.org/) for XML comparison.

## Testing
The bindings are tested on over 2500 different EML files from different type of Dutch elections, all downloaded from [data.overheid.nl](https://data.overheid.nl/community/organization/kiesraad) using a roundtrip serialization test. To run the tests, install the test dependencies (see above), put EML files into a `data` folder and run `pytest` in the root folder.

See the [test report](pyeml_bindings_testreport.html)

## Usage
Make sure that xsData is installed. Using example file [`Telling_PS2023_Flevoland_gemeente_Almere.eml.xml`](https://data.overheid.nl/dataset/verkiezingsuitslag-provinciale-staten-2023#panel-resources) which has EML id 510b:

```python
from pathlib import Path
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from pyeml_bindings import Eml510
from pyeml_bindings.namespace import NAMESPACE


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
serializer = XmlSerializer(config=SerializerConfig(xml_declaration=False))

with open(Path("output.xml"), "w") as out_file:
    # We can optionally pass the NAMESPACE from the bindings to the write function
    # to use the same namespace prefixes.
    # If we don't, we still get back valid EML but with ns0, ns1 etc.
    serializer.write(out=out_file, obj=eml, ns_map=NAMESPACE)
```

## Building
To build the package yourself instead of installing the `.whl`, simply clone the repository and then in the root folder run. 
```
python -m build
```

## Codegen
These bindings are mostly generated using [xsData](https://xsdata.readthedocs.io) with some minor changes where needed. See commit history for these changes.