from .exceptions import (NoIndexError)
from .constants import (FIGURE_PROPERTIES, GRAPH_PROPERTIES, FILE_PROPERTIES)


class Properties:
    """Class Properties is used to store current properties of graph

    Properties
    ----------
        figure_properties : dict
            properties of graph figure
        graph_properties : dict
            properties of graph axes
        file_properties : dict
            input and output properties
        graphs : dict
            properties of curtain graph

    Raises
    ------
        NoIndexError
            if graph properties do not have an index
    """

    def __init__(self, **kwargs):
        self.__figure_properties: dict = {key: kwargs.get("FigureProperties", kwargs)[key]
                                          for key in kwargs.get("FigureProperties", kwargs) if key in FIGURE_PROPERTIES}
        self.__graph_properties: dict = {key: kwargs[key] for key in kwargs if key in GRAPH_PROPERTIES}
        self.__file_properties: dict = {key: kwargs.get("FileProperties", kwargs)[key]
                                        for key in kwargs.get("FileProperties", kwargs) if key in FILE_PROPERTIES}

        self.__graphs: dict = {}
        for graph in [Properties(**pr) for pr in kwargs.get("Graphs", [])]:
            if graph.file_properties.get("index") is None:
                raise NoIndexError()
            self.__graphs[graph.file_properties.get("index")] = graph

    @property
    def figure_properties(self) -> dict:
        """Property that returns properties of graph figure

        Returns
        -------
            dict
                properties of graph figure
        """

        return self.__figure_properties

    @property
    def graph_properties(self) -> dict:
        """Property that returns properties of graph axes

        Returns
        -------
            dict
                properties of graph axes
        """

        return self.__graph_properties

    @property
    def file_properties(self) -> dict:
        """Property that returns input and output properties of graph

        Returns
        -------
            dict
                input and output properties of graph
        """

        return self.__file_properties

    @property
    def graphs(self) -> dict:
        """Property that returns properties of curtain graph

        Returns
        -------
            dict
                properties of curtain graph
        """

        return self.__graphs
