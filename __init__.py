"""
:authors: FranChesKo
:license: Apache License, Version 2.0, see LICENSE file

:copyright: (c) 2022 FranChesKo
"""

from .graphcreator import (create_graph)
from .iofile import (File, IFile, OFile, ICsv, OCsv, IJson, OJson)
from .graph import (Graph, SaveGraph, SetGraph, Property, XLabel, YLabel, Grid, Title, Legend)
from .properties import (Properties)
from .constants import (ENCODINGS, FIGURE_PROPERTIES, GRAPH_PROPERTIES, FILE_PROPERTIES)
from .exceptions import (FileError, DataError, EncodingError, NoIndexError, DpiError)

__author__ = 'FranChesKo'
__version__ = '1.1.1.5'
__email__ = 'khl_doss@mail.ru'
