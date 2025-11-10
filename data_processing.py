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


def filtering(condition,dict_list):
    temps = []
    for item in dict_list:
        if condition(item,temps):
            temps.append(item)
    return temps


def aggregate(aggregate_key,aggregate_function,dict_list):
        num = 0
        want_list = []
        for i in dict_list:
            want_list.append(float(i[aggregate_key]))
        num = aggregate_function(num,want_list)
        return num
    
            
# Print all cities in Germany
flitered = filtering(lambda x , y:x["country"] == "Germany",cities)
print(flitered)
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
flitered = filtering(lambda x , y:x != "",cities)
print(aggregate("temperature",lambda a, y: (a + sum(float(x) for x in y))/len(y),flitered))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Spain with a temperature above 12°C
print("all cities in Spain with a temperature above 12°C:")
flitered = filtering(lambda x , y:x["country"] == "Spain" and float(x["temperature"]) > 12,cities)
print(flitered)
print()

# Count the number of unique countries
print("the number of unique countries:")
flitered = filtering(lambda x,y:x["country"] not in [i["country"] for i in y],cities)
print(len(flitered))
print()

# Print the average temperature for all the cities in Germany
print("the average temperature for all the cities in Germany:")
flitered = filtering(lambda x , y:x["country"] == "Germany",cities)
print(aggregate("temperature",lambda a, y: (a + sum(float(x) for x in y))/len(y),flitered))
print()

# Print the max temperature for all the cities in Italy
print("the max temperature for all the cities in Italy:")
flitered = filtering(lambda x , y:x["country"] == "Italy",cities)
print(aggregate("temperature",lambda a, y: max(float(x) for x in y),flitered))
print()

# Print the max temperature for all the country
countryname = []
max = 0
print("the max temperature for all the cities in Italy:")
for i in cities:
    if i["country"] not in countryname:
        flitered = filtering(lambda x , y:x["country"] == i["country"] ,cities)
        tem = aggregate("temperature",lambda a, y: (a + sum(float(x) for x in y))/len(y),flitered)
        if tem > max:
            max = tem
            country = i["country"]
        countryname.append(i["country"])
    else:
        continue
print(max,country)
print()