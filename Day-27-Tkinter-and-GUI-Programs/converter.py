from constants import CONVERSIONS


def convert(value, from_unit, to_unit):

    if from_unit == to_unit:
        return value

    key = (from_unit, to_unit)

    if key not in CONVERSIONS:
        raise ValueError("Conversion not supported")

    return CONVERSIONS[key](value)