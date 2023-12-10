"""typing from operations values"""
from collections.abc import Callable
from typing_variables import VectorReal


def median(series: VectorReal) -> float:

    """
    Calculate median in a list of values

    Args:
        series(List[float, int]): list with values

    Returns:
        Float: value from median
    """
    total = len(series)
    return sum(series) / total


def deviation(series: VectorReal, value_median: float) -> VectorReal:

    """
    Calculate difference between value in median to values
    in list.

    Args:
        series(list): list with values float or integer
        Value_media: value median from list

    Returns:
        list: list with values of difference entre number in original list
        and the value from median
    """
    return [abs(value_median - number) for number in series]


def variance(series: VectorReal, subtract: bool = True) -> float:

    """
    Calculate variance in a list of values integer or float

    Args:
        Series(list): list of values integer or float
        Subtract: if subtract total in variance per -1 or
        not

    Returns:
        float: value of variance to series
    """

    def is_subtract_total(indicator: bool) -> int:
        """
        if subtract is true return 1 or else return 0

        Args:
            indicator (bool): value passed per user

        Returns:
            int: Value 1 or 0
        """
        return 1 if indicator else 0

    value_subtract = is_subtract_total(subtract)
    total = len(series)
    elevation = map(lambda value: value**2, series)
    return sum(elevation) / (total - value_subtract)


def standard_deviation(
    series: VectorReal, func_median: Callable[[VectorReal], float] = median
) -> float:

    """
    calculate standard deviation to list values integer or  float.

    Args:
        series(list): list with values integer or float.
        func_median(function, optional): function to calculate median.
        for series, defaults to median.

    Returns:
        float: return value of standard deviation.
    """

    value_median = func_median(series)
    difference = deviation(series, value_median)
    value_variance = variance(difference)
    return value_variance**(1/2)


def calculator_standardization(
    unknown: float,
    value_median: float,
    value_deviation: float
) -> float:
    """
    calculate value to standardization

    Args:
        unknown (float): value original to calculates standardization,
        unknown.
        median (float): value of median to set from unknown.
        deviation (float): value of deviation to set from unknown.

    Returns:
        float: Value of standardization.
    """
    return (unknown - value_median) / value_deviation


def standardization(
    series: VectorReal, func_median: Callable[[VectorReal], float] = median
) -> VectorReal:

    """
    Return a list with values standardized to arguments from series

    Args:
        series(list): list with values integer or float
        func_median(function, optional): function that calculate median

    Returns:
        list: list with values standardized
    """
    deviation_values = standard_deviation(series)
    value_median = func_median(series)
    return [calculator_standardization(
        value, value_median, deviation_values)
        for value in series]


def calculate_normalize(
    unknown: float,
    value_maximum: float,
    value_minimum: float
) -> float:
    """
    Calculate normalization by value in argument unknown.

    Args:
        unknown (float): value to be normalize.
        value_maximum (float): value maximum in set from unknown.
        value_minimum (float): value minimum in set from unknown.

    Returns:
        float: Value normalized.
    """
    return (unknown - value_minimum) / (value_maximum - value_minimum)


def normalization(series: VectorReal) -> VectorReal:

    """
    Calculate values to normalization from series

    Args:
        series(list): list with values integer or float

    Returns:
        list: list with values normalized
    """

    max_value = max(series)
    min_value = min(series)

    return [calculate_normalize(
        value, max_value, min_value) for value in series]


if __name__ == "__main__":
    print(standardization([4, 5, 6, 7, 8]))
    print(normalization([4, 5, 6, 7, 8]))
