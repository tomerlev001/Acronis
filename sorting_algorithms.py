from collections.abc import Iterable, Generator, Iterator
from heapq import heapify
from logger import Logger, DebugLevel


LOGGER = Logger(__name__).get_logger(DebugLevel.DEBUG)


def merge(*iterables: Iterable[int | float, ...]) -> Generator[int, None, None]:
    """
    Merge sorted iterables[int | float,...] into one sorted generator.

    INPUT: Iterables[int | float, ...], the iterables must be sorted from the smallest to the largest number.
    RETURN: Sorted merge of all the iterables as generator.
    """
    if not iterables:
        return

    iterators = __convert_iterables_to_iterators(iterables)
    ordered_iterators = __order_iterators(iterators)

    LOGGER.info("Beginning to yield sorted numbers.")
    while len(ordered_iterators) > 0:
        try:
            iterator_data = ordered_iterators[0]
            number, order, iterator_object = iterator_data
            yield number
            iterator_data[0] = next(iterator_object)
            heapify(ordered_iterators)
        except StopIteration:
            ordered_iterators.pop(0)
            heapify(ordered_iterators)
            continue


def __order_iterators(iterators_list: list[Iterator, ...]) -> list[list[int, int, Iterator], ...]:
    LOGGER.info("Ordering iterators.")
    iterators = []
    for i in range(len(iterators_list)):
        try:
            iterator = iterators_list[i]
            value = next(iterator)
            if type(value) not in [int, float]:
                LOGGER.error(f"The value '{value}' isn't int or float type, Iterables must contain int only.")
                raise ValueError(f"The value '{value}' isn't int or float type, Iterables must contain int only.")
            iterators.append([value, i, iterator])
        except StopIteration:
            continue
    heapify(iterators)

    return iterators


def __convert_iterables_to_iterators(iterables: tuple[Iterable[int], ...]) -> list[Iterator, ...]:
    LOGGER.info("Converting iterables to iterators.")
    iterators = []
    for iterable in iterables:
        if not isinstance(iterable, Iterable):
            LOGGER.error(f"The parameter '{iterable}' isn't iterable.")
            raise TypeError(f"The parameter '{iterable}' isn't iterable, the input must contain only iterables.")
        iterators.append(iter(iterable))

    return iterators
