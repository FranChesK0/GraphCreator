class FileError(TypeError):
    """Class FileError that is used as Exception

    Note: child of TypeError

    Attributes
    ----------
        file : object
            not appropriate file
        file_type : str
            type that file must match
    """

    def __init__(self, file, file_type):
        super().__init__(f"{file} is not {file_type} file")


class DataError(TypeError):
    """Class DataError that is used as Exception

    Note: child of TypeError

    Attributes
    ----------
        file_type : str
            type of file that data must match
    """

    def __init__(self, file_type):
        super().__init__(f"Not appropriate data for {file_type}")


class EncodingError(TypeError):
    """Class EncodingError that is used as Exception

    Note: child of TypeError

    Attributes
    ----------
        encoding : str
            wrong or unknown encoding
    """

    def __init__(self, encoding):
        super().__init__(f"Unknown encoding: {encoding}")


class NoIndexError(ValueError):
    """Class NoIndexError that is used as Exception

    Note: child of ValueError
    """

    def __init__(self):
        super().__init__(f"The Graph properties must have an index")


class DpiError(ValueError):
    """Class DpiError that is used as Exception

    Note: child of ValueError

    Attributes
    ----------
        msg : str
            message that will be shown
    """

    def __init__(self, msg):
        super().__init__(msg)
