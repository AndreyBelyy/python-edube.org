# A car's fuel consumption may be expressed in many different ways.
# For example, in Europe, it is shown as the amount of fuel consumed per 100 kilometers.
#
# In the USA, it is shown as the number of miles traveled by a car using one gallon of fuel.
#
# Your task is to write a pair of functions converting l/100km into mpg, and vice versa
m_km = 1.609344
l_g = 3.785411784

def liters_100km_to_miles_gallon(liters):
    mpg = (100 / m_km) / (liters / l_g)
    return mpg
def miles_gallon_to_liters_100km(miles):
    kml = 100 / ((miles * m_km) / l_g)
    return kml



print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))