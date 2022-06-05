import numpy as np

from .iofile import (ICsv, IJson)
from .properties import (Properties)
from .graph import (Graph, SaveGraph, SetGraph, XLabel, YLabel, Grid, Legend, Title)


def create_graph(data_file: str, properties_file: str, encoding: str | None = None) -> Graph | list:
    """Makes graph/graphs and then save it/them

    If argument encoding is not set, "utf-8" is used as encoding

    Parameters
    ----------
        data_file : str
            Csv file with data for making graph/graphs
        properties_file : str
            Json with properties for making and saving graph/graphs
        encoding : str
            Encoding of the files. Default="utf-8"

    Returns
    -------
        Graph
            object of Graph class
        list
            list of objects of Graph class
    """

    json_reader: IJson = IJson(properties_file, encoding=encoding)
    properties: Properties = Properties(**json_reader.get())

    setter: SetGraph = SetGraph()
    saver: SaveGraph = SaveGraph()

    csv_reader: ICsv = ICsv(data_file, encoding=encoding, delimiter=properties.file_properties.get("delimiter"))
    data: np.ndarray = csv_reader.get()

    x: np.ndarray = data[:, 0]
    ys: list = [data[:, i] for i in range(1, data.shape[1])]

    if properties.file_properties.get("MultipleOutput", False):
        out: list = []

        for i, y in enumerate(ys, start=1):
            graph: Graph = Graph()

            cur_prop: Properties = properties.graphs.get(i, Properties())
            cur_prop.graph_properties.setdefault("label", str(i))

            graph.axes.plot(x, y, **cur_prop.graph_properties)
            [setter.add_property(pr) for pr in (XLabel(), YLabel(), Grid(), Legend(), Title())]
            setter.set(graph, properties.figure_properties)

            if cur_prop.file_properties.get("save", properties.file_properties.get("save", True)):
                saver.save(graph=graph,
                           path=cur_prop.file_properties.get("OutputPath",
                                                             properties.file_properties.get("OutputPath",
                                                                                            "") + f"\\{i}.png"),
                           dpi=cur_prop.file_properties.get("dpi", properties.file_properties.get("dpi")))

            out.append(graph)
    else:
        out: Graph = Graph()

        for i, y in enumerate(ys, start=1):
            cur_prop: Properties = properties.graphs.get(i, Properties())
            cur_prop.graph_properties.setdefault("label", str(i))
            out.axes.plot(x, y, **cur_prop.graph_properties)

        [setter.add_property(pr) for pr in (XLabel(), YLabel(), Grid(), Legend(), Title())]
        setter.set(out, properties.figure_properties)

        if properties.file_properties.get("save", True):
            saver.save(graph=out, path=properties.file_properties.get("OutputPath", "Graph.png"),
                       dpi=properties.file_properties.get("dpi"))

    return out
