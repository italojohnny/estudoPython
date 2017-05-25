import pint

ureg = pint.UnitRegistry()

distance = 24.0 * ureg.kph
print(distance)

print("")
print(type(distance.magnitude))
print(type(distance.units))

print("")
if 'magnitude' in dir(distance):
    print(distance.magnitude)
print(distance.units)


