from typing import Any
from sympy.core import Basic
from sympy.printing.codeprinter import CodePrinter

known_functions = ...
class GLSLPrinter(CodePrinter):
    _not_supported: set[Basic] = ...
    printmethod = ...
    language = ...
    _default_settings = ...
    def __init__(self, settings=...) -> None:
        ...
    
    def indent_code(self, code) -> str | list[Any]:
        ...
    
    _print_tuple = ...
    _print_Tuple = ...


def glsl_code(expr, assign_to=..., **settings) -> str | tuple[set[tuple[Any, str]], set[Any], str]:
    ...

def print_glsl(expr, **settings) -> None:
    ...

