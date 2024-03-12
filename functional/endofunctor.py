from typing import Any, Callable

#Functor -> returns a different functor
class StringFunctor:
    def __init__(self, value: Any):
        self.value = value

    def map(self, func: Callable[[Any], Any]):
        return ListFunctor([func(self.value)])

#Endofunctor -> returns the same functor
class ListFunctor:
    def __init__(self, values: list[Any]):
        self.values = values

    def map(self, func: Callable[[Any], Any]):
        return ListFunctor([func(value) for value in self.values])


# Example usage:
sf = StringFunctor("Hello")
lf = sf.map(len)  # Now it's a ListFunctor, not a StringFunctor

# Further mapping will use ListFunctor's map method
lf2 = lf.map(lambda x: x * 2)