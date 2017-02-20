import pint

ureg = pint.UnitRegistry()

distance = 24.0 * ureg.kph
print(distance)
print(distance)
print(type(distance.magnitude))
print(distance.units)
print(type(distance.print))


