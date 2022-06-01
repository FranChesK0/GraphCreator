from abc import ABC, abstractmethod

from matplotlib import pyplot as plt

from .exceptions import (DpiError)


class Graph:
    """Class Graph is used to store the graph

    Properties
    ----------
        figure : matplotlib.pyplot.Figure
            graph figure
        axes : matplotlib.pyplot.Axes
            graph axes
    """

    def __init__(self):
        self._fig: plt.Figure
        self._ax: plt.Axes
        self._fig, self._ax = plt.subplots()

    @property
    def figure(self) -> plt.Figure:
        """Property that returns graph figure

        Returns
        -------
            matplotlib.pyplot.Figure
                graph figure
        """

        return self._fig

    @property
    def axes(self) -> plt.Axes:
        """Property that returns graph axes

        Returns
        -------
            matplotlib.pyplot.Axes
                graph axes
        """

        return self._ax


class SaveGraph:
    """Class SaveGraph is used for saving picture of graph

    Note: Singleton class

    Methods
    -------
        save(graph: Graph, path: str, dpi: int) : None
            method that save graph
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @staticmethod
    def save(graph: Graph, path: str, dpi: int | None = None) -> None:
        """Method that is used for saving picture of graph

        Arguments
        ---------
            graph : Graph
                graph that will be saved
            path : str
                path to the file where graph will be saved
            dpi : int
                dpi of the picture of the graph

        Raises
        ------
            TypeError
                if graph is not instance Graph
                if dpi is not instance integer
            DpiError
                if dpi lower than 0 or higher than 1000
        """

        graph = SaveGraph.__check_graph(graph)
        dpi = SaveGraph.__check_dpi(dpi or 400)
        graph.figure.savefig(path, dpi=dpi)

    @classmethod
    def __check_graph(cls, graph) -> Graph:
        if not isinstance(graph, Graph):
            raise TypeError(f"graph must be a Graph object")
        return graph

    @classmethod
    def __check_dpi(cls, dpi) -> int:
        if not isinstance(dpi, int):
            raise TypeError(f"dpi must be integer")
        if dpi <= 0:
            raise DpiError("dpi must be higher than 0")
        if dpi > 1000:
            raise DpiError("dpi must be lower than 1000")
        return dpi


class Property(ABC):
    """Abstract class that is used to define new axes property

    Methods
    -------
        set(ax: matplotlib.pyplot.Axes, properties: dict)
    """

    @abstractmethod
    def set(self, ax: plt.Axes, properties: dict):
        """Abstract method that set axes property

        Arguments
        ---------
            ax : matplotlib.pyplot.Axes
                graph axes where set property
            properties : dict
                properties where current property is checked
        """

        raise NotImplementedError


class XLabel(Property):
    def set(self, ax: plt.Axes, properties: dict):
        if "xlabel" in properties:
            ax.set_label(properties["xlabel"])


class YLabel(Property):
    def set(self, ax: plt.Axes, properties: dict):
        if "ylabel" in properties:
            ax.set_ylabel(properties["ylabel"])


class Grid(Property):
    def set(self, ax: plt.Axes, properties: dict):
        if "grid" in properties:
            ax.grid(**properties["grid"]) if isinstance(properties["grid"], dict) else ax.grid()


class Legend(Property):
    def set(self, ax: plt.Axes, properties: dict):
        if "legend" in properties:
            ax.legend()


class Title(Property):
    def set(self, ax: plt.Axes, properties: dict):
        if "title" in properties:
            ax.set_title(properties["title"])


class SetGraph:
    """Class SetGraph is used to set graph axes properties

    Methods
    -------
        add_property(pr: Property)
            add property to list
        set(ax: matplotlib.pyplot.Axes, properties: dict)
            set properties from list to graph axes
    """

    def __init__(self):
        self._properties: list = []

    def add_property(self, pr: Property):
        """Method that add properties to list

        Arguments
        ---------
            pr : Property
                property that will be added to list
        """

        self._properties.append(pr)

    def set(self, graph: Graph, properties: dict):
        """Method that set properties from list to graph axes

        Arguments
        ---------
            graph : Graph
                graph axes where will be set properties
            properties : dict
                properties where added properties are searched for
        """
        for pr in self._properties:
            pr.set(graph.axes, properties)
