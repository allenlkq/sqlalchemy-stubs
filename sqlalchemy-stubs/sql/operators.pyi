from typing import Any, Optional, Text, List, Union
from .selectable import Select as Select
from .elements import BindParameter as BindParameter, UnaryExpression

class Operators(object):
    def __and__(self, other): ...
    def __or__(self, other): ...
    def __invert__(self): ...
    def op(self, opstring, precedence: int = ..., is_comparison: bool = ...): ...
    def operate(self, op, *other, **kwargs): ...
    def reverse_operate(self, op, other, **kwargs): ...

class custom_op(object):
    __name__: str = ...
    opstring: str = ...
    precedence: Any = ...
    is_comparison: Any = ...
    natural_self_precedent: Any = ...
    eager_grouping: Any = ...
    def __init__(self, opstring, precedence: int = ..., is_comparison: bool = ...,
                 natural_self_precedent: bool = ..., eager_grouping: bool = ...) -> None: ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    def __call__(self, left, right, **kw): ...

class ColumnOperators(Operators):
    timetuple: Any = ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    __hash__: Any = ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def is_distinct_from(self, other): ...
    def isnot_distinct_from(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __neg__(self): ...
    def __contains__(self, other): ...
    def __getitem__(self, index): ...
    def __lshift__(self, other): ...
    def __rshift__(self, other): ...
    def concat(self, other): ...
    def like(self, other: Text, escape: Optional[Any] = ...): ...
    def ilike(self, other: Text, escape: Optional[Any] = ...): ...
    def in_(self, other: Union[List[Any], BindParameter, Select]): ...
    def notin_(self, other: Union[List[Any], BindParameter, Select]): ...
    def notlike(self, other, escape: Optional[Any] = ...): ...
    def notilike(self, other, escape: Optional[Any] = ...): ...
    def is_(self, other): ...
    def isnot(self, other): ...
    def startswith(self, other: str, **kwargs): ...
    def endswith(self, other, **kwargs): ...
    def contains(self, other, **kwargs): ...
    def match(self, other, **kwargs): ...
    def desc(self) -> UnaryExpression: ...
    def asc(self) -> UnaryExpression: ...
    def nullsfirst(self): ...
    def nullslast(self): ...
    def collate(self, collation): ...
    def __radd__(self, other): ...
    def __rsub__(self, other): ...
    def __rmul__(self, other): ...
    def __rdiv__(self, other): ...
    def __rmod__(self, other): ...
    def between(self, cleft, cright, symmetric: bool = ...): ...
    def distinct(self): ...
    def any_(self): ...
    def all_(self): ...
    def __add__(self, other): ...
    def __sub__(self, other): ...
    def __mul__(self, other): ...
    def __div__(self, other): ...
    def __mod__(self, other): ...
    def __truediv__(self, other): ...
    def __rtruediv__(self, other): ...

def from_(): ...
def as_(): ...
def exists(): ...
def istrue(a): ...
def isfalse(a): ...
def is_distinct_from(a, b): ...
def isnot_distinct_from(a, b): ...
def is_(a, b): ...
def isnot(a, b): ...
def collate(a, b): ...
def op(a, opstring, b): ...
def like_op(a, b, escape: Optional[Any] = ...): ...
def notlike_op(a, b, escape: Optional[Any] = ...): ...
def ilike_op(a, b, escape: Optional[Any] = ...): ...
def notilike_op(a, b, escape: Optional[Any] = ...): ...
def between_op(a, b, c, symmetric: bool = ...): ...
def notbetween_op(a, b, c, symmetric: bool = ...): ...
def in_op(a, b): ...
def notin_op(a, b): ...
def distinct_op(a): ...
def any_op(a): ...
def all_op(a): ...
def startswith_op(a, b, escape: Optional[Any] = ...): ...
def notstartswith_op(a, b, escape: Optional[Any] = ...): ...
def endswith_op(a, b, escape: Optional[Any] = ...): ...
def notendswith_op(a, b, escape: Optional[Any] = ...): ...
def contains_op(a, b, escape: Optional[Any] = ...): ...
def notcontains_op(a, b, escape: Optional[Any] = ...): ...
def match_op(a, b, **kw): ...
def notmatch_op(a, b, **kw): ...
def comma_op(a, b): ...
def concat_op(a, b): ...
def desc_op(a): ...
def asc_op(a): ...
def nullsfirst_op(a): ...
def nullslast_op(a): ...
def json_getitem_op(a, b): ...
def json_path_getitem_op(a, b): ...
def is_comparison(op): ...
def is_commutative(op): ...
def is_ordering_modifier(op): ...
def is_natural_self_precedent(op): ...
def mirror(op): ...
def is_precedent(operator, against): ...
