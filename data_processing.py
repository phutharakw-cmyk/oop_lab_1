import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany
print("all cities in Germany:")
german_city = []
for i in cities:
    if i["country"] == "Germany":
        german_city.append(i["city"])
print(",".join(german_city))
print()

# Print all cities in Spain with a temperature above 12°C
print("all cities in Spain with a temperature above 12°C:")
spain_city = []
for i in cities:
    if i["country"] == "Spain" and float(i["temperature"]) > 12:
        spain_city.append(i["city"])
print(",".join(spain_city))
print()

# Count the number of unique countries
print("the number of unique countries:")
uniqe = []
for i in cities:
    if i["country"] not in uniqe:
        uniqe.append(i["country"])
print(len(uniqe))
print()

# Print the average temperature for all the cities in Germany
print("the average temperature for all the cities in Germany:")
german_city = []
combind = 0
count = 0
for i in cities:
    if i["country"] == "Germany":
        combind += float(i["temperature"])
        count += 1
print(combind/count)
print()

# Print the max temperature for all the cities in Italy
print("the max temperature for all the cities in Italy:")
max_temp = 0
for i in cities:
    if i["country"] == "Italy":
        if float(i["temperature"]) > max_temp:
            max_temp = float(i["temperature"])
print(max_temp)
print()
