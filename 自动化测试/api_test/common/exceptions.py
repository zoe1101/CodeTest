# -*- coding: utf-8 -*-
"""
异常类
"""
from requests.exceptions import RequestException

class ParserError(Exception):
    pass


class ExtractExpressionError(Exception):
    pass

class YamlException(Exception):
    """Custom exception for error reporting."""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "\n".join(
            [
                "usecase execution failed",
                "   spec failed: {}".format(self.value),
                "   For more details, see this the document.",
            ]
        )
