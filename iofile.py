import csv
import json
from abc import ABC, abstractmethod
from encodings import normalize_encoding

import numpy as np

from constants import ENCODINGS
from exceptions import FileError, EncodingError, DataError


class File(ABC):
    @classmethod
    def _check_string(cls, value: str) -> str:
        if not isinstance(value, str):
            raise TypeError(f"{value} must be a string")
        return value

    @classmethod
    def _check_path(cls, path: str, file_type: str) -> str:
        if not path.endswith(file_type):
            raise FileError(path, file_type)
        return path

    @classmethod
    def _check_encoding(cls, encoding: str) -> str:
        if normalize_encoding(encoding) not in ENCODINGS:
            raise EncodingError(encoding)
        return normalize_encoding(encoding)


class IFile(File):
    @abstractmethod
    def get(self):
        raise NotImplementedError


class OFile(File):
    @abstractmethod
    def save(self):
        raise NotImplementedError

    @classmethod
    def _check_data(cls, data, data_type, file_type: str):
        if not isinstance(data, data_type):
            raise DataError(file_type)
        return data


class ICsv(IFile):
    """Class ICsv uses for getting data from csv file

    Attributes
    ----------
        path : str
            path to the csv file
        encoding : str
            encoding of the file
        delimiter : str
            delimiter that uses in the file

    Methods
    -------
        get() : np.ndarray
            reads the file and returns data from it in numpy.ndarray

    Raises
    ------
        TypeError
            if path or encoding or delimiter not string
        FileError
            if path does not lead to the csv file
        EncodingError
            if encoding does not exist
    """

    def __init__(self, path: str, encoding: str | None = None, delimiter: str | None = None):
        self._path = File._check_path(File._check_string(path), ".csv")
        self._encoding = File._check_encoding(File._check_string(encoding or "utf-8"))
        self._delimiter = File._check_string(delimiter or ',')

    def get(self) -> np.ndarray:
        """Method for reading csv file and getting data from it

        Returns
        -------
            np.ndarray
                numpy array with data from csv file
        """

        with open(self._path, 'r', encoding=self._encoding) as file:
            return np.array([np.array(list(map(float, line))) for line in csv.reader(file, delimiter=self._delimiter)])


class IJson(IFile):
    """Class IJson uses for getting data from json file

    Attributes
    ----------
        path : str
            path to the csv file
        encoding : str
            encoding of the file

    Methods
    -------
        get() : dict
            reads the file and returns data from it in dict

    Raises
    ------
        TypeError
            if path or encoding not string
        FileError
            if path does not lead to the csv file
        EncodingError
            if encoding does not exist
    """

    def __init__(self, path: str, encoding: str | None = None):
        self._path = File._check_path(File._check_string(path), ".json")
        self._encoding = File._check_encoding(File._check_string(encoding or "utf-8"))

    def get(self) -> dict:
        """Method for reading json file and getting data from it

        Returns
        -------
            dict
                dict with data from json file
        """

        with open(self._path, 'r', encoding=self._encoding) as file:
            return json.load(file)


class OCsv(OFile):
    """Class OCsv uses for writing data in csv file

    Attributes
    ----------
        path : str
            path to the csv file
        encoding : str
            encoding of the file
        delimiter : str
            delimiter that uses in the file

    Methods
    -------
        save() : None
            write data in csv file

    Raises
    ------
        TypeError
            if path or encoding or delimiter not string
        FileError
            if path does not lead to the csv file
        EncodingError
            if encoding does not exist
    """

    def __init__(self, path: str, data: list | np.ndarray, encoding: str | None = None, delimiter: str | None = None):
        self._path = File._check_path(File._check_string(path), ".csv")
        self._data = OFile._check_data(data, (list | np.ndarray), ".csv")
        self._encoding = File._check_encoding(File._check_string(encoding or "utf-8"))
        self._delimiter = File._check_string(delimiter or ',')

    def save(self) -> None:
        """Method for writing data in csv file

        Returns
        -------
            None
        """

        with open(self._path, 'w', encoding=self._encoding) as file:
            file_writer = csv.writer(file, delimiter=self._delimiter, lineterminator="\r")
            [file_writer.writerow(list(map(str, row))) for row in self._data]


class OJson(OFile):
    """Class OJson uses for writing data in json file

    Attributes
    ----------
        path : str
            path to the csv file
        encoding : str
            encoding of the file

    Methods
    -------
        save() : None
            write data in json file

    Raises
    ------
        TypeError
            if path or encoding not string
        FileError
            if path does not lead to the csv file
        EncodingError
            if encoding does not exist
    """

    def __init__(self, path: str, data: dict, encoding: str | None = None):
        self._path = File._check_path(File._check_string(path), ".json")
        self._data = OFile._check_data(data, dict, ".json")
        self._encoding = File._check_encoding(File._check_string(encoding or "utf-8"))

    def save(self) -> None:
        """Method for writing data in json file

        Returns
        -------
            None
        """

        with open(self._path, 'w', encoding=self._encoding) as file:
            json.dump(self._data, file)
