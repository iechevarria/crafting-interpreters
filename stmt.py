from collections import namedtuple

Expression = namedtuple("Expression", ("expression"))
Print = namedtuple("Print", ("expression"))
Var = namedtuple("Var", ("name", "initializer"))
