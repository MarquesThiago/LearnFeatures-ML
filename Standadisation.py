def median(series: list) -> float:

    """
    Calcute median in a list of values

    Args:
        series(list): list with values

    Returns:
        float: value from median
    """
    total = len(series)
    return sum(series) / total


def deviation(series: list, value_median: float) -> list:

    """
    Calcuate diveference between value in median to values
    in list.

    Args:
        series(list): list with values float or integer
        Value_media: value median from list

    Returns:
        list: list with values of dirence entre number in original list
        and the value from median
    """
    return [abs(value_median - number) for number in series]


def variancy(series: list, subtract: bool = True) -> float:

    """
    Calculate variancy in a list of values integer or float

    Args:
        Series(list): list of values integer or float
        Substract: if substract total in variancy per -1 or
        not

    Returns:
        float: value of variancy to series
    """

    def is_substract_total(indicator: bool) -> int:
        """
        if substract is true return 1 or else return 0

        Args:
            indicator (bool): value passed per user

        Returns:
            int: Value 1 or 0
        """
        return 1 if indicator else 0

    value_substract = is_substract_total(subtract)
    total = len(series)
    elevation = map(lambda value: value**2, series)
    return sum(elevation) / (total - value_substract)


def standard_deviation(series: list, func_median=median) -> float:

    """
    calculate stardard deviation to list values integer or  float.

    Args:
        series(list): list with values integer or float.
        func_median(function, optional): function to calculete median.
        for series, defaults to median.

    Returns:
        flaot: return value of standard deviation.
    """

    value_median = func_median(series)
    diference = deviation(series, value_median)
    variance = variancy(diference)
    return variance**(1/2)


def calculator_stardardisation(
    incognite: float,
    median: float,
    deviation: float
) -> float:
    """
    calculate value to stardardization

    Args:
        incognite (float): value orignal to calculates stardardisation,
        incognite.
        median (float): value of median to set from incognite.
        deviation (float): value of deviantion to set from incognite.

    Returns:
        float: Value of standardisation.
    """
    return (incognite - median) / deviation


def standardisation(series, func_median=median) -> list:

    deviation_values = standard_deviation(series)
    value_median = func_median(series)
    return [calculator_stardardisation(
        value, value_median, deviation_values)
        for value in series]


def calculate_normalize(
    incognite: float,
    value_maximium: float,
    value_minimum: float
) -> float:
    return (incognite - value_minimum) / (value_maximium - value_minimum)


def normalization(series: list) -> list:
    max_value = max(series)
    min_value = min(series)

    return [calculate_normalize(
        value, max_value, min_value) for value in series]


print(standardisation([-4, 5, 6, 7, 8]))
print(normalization([-4, 5, 6, 7, 8]))
