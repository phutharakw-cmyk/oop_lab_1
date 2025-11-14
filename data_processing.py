import csv, os
from pathlib import Path
import sqlite3

class DataLoader:
    """Handles loading CSV data files."""
    
    def __init__(self, base_path=None):
        """Initialize the DataLoader with a base path for data files.
        """
        if base_path is None:
            self.base_path = Path(__file__).parent.resolve()
        else:
            self.base_path = Path(base_path)
    
    def load_csv(self, filename):
        """Load a CSV file and return its contents as a list of dictionaries.
        """
        filepath = self.base_path / filename
        data = []
        
        with filepath.open() as f:
            rows = csv.DictReader(f)
            for row in rows:
                data.append(dict(row))
        
        return data

class DB:
    def __init__(self):
        self.alldatabase = {}

    def insert(self,object_input):
        self.alldatabase.update({object_input.name:object_input.dict_list})

    def search(self,finder):
        return self.alldatabase[finder]
    
class Table:
    def __init__(self,name,dict_list):
        self.name = name
        self.dict_list = dict_list
        self.filtered_data = dict_list

    def filter(self,condition):
        filter_list = []
        for i in self.filtered_data:
            if condition(i) :
                filter_list.append(i)
        self.filtered_data = filter_list
        return self

    def aggregate(self,aggregate_function,aggregate_key):
        want_list = []
        for i in self.filtered_data:
            try:
                want_list.append(float(i[aggregate_key]))
            except:
                want_list.append(i[aggregate_key])
        return aggregate_function(want_list)
    
    def table(self):
        to_return = self.filtered_data
        self.filtered_data = self.dict_list
        return to_return
    
    def join(self, other_table, key):
        new = []
        for i in self.dict_list:
            new_dict = i
            for j in other_table.dict_list:
                if i[key] == j[key]:
                    for k in j:
                        new_dict.update({k:j[k]})
            new.append(new_dict)
        self.filtered_data = new
        self.dict_list = new
        return self
                        
    def __str__(self):
        return self.name + ':' + str(self.table)

loader = DataLoader()
cities = loader.load_csv('Cities.csv')
table1 = Table('cities', cities)
countries = loader.load_csv('Countries.csv')
table2 = Table('countries', countries)

my_DB = DB()
my_DB.insert(table1)
my_DB.insert(table2)

my_table1 = Table("my_table1",my_DB.search('cities'))
print("List all cities in Italy:") 
my_table1_filtered = my_table1.filter(lambda x: x['country'] == 'Italy')
print(my_table1_filtered.table())
print()

print("Average temperature for all cities in Italy:")
print(my_table1_filtered.aggregate(lambda x: sum(x)/len(x), 'temperature'))
print()

my_table2 = Table("my_table2",my_DB.search('countries'))
print("List all non-EU countries:") 
my_table2_filtered = my_table2.filter(lambda x: x['EU'] == 'no')
print(my_table2_filtered.table())
print()

print("Number of countries that have coastline:")
print(my_table2.filter(lambda x: x['coastline'] == 'yes').aggregate(lambda x: len(x), 'coastline'))
print()

my_table3 = my_table1.join(my_table2, 'country')
print("First 5 entries of the joined table (cities and countries):")
for item in my_table3.table()[:5]:
    print(item)
print()

print("Cities whose temperatures are below 5.0 in non-EU countries:")
my_table3_filtered = my_table3.filter(lambda x: x['EU'] == 'no').filter(lambda x: float(x['temperature']) < 5.0)
print(my_table3_filtered.table())
print()

print("The min and max temperatures for cities in EU countries that do not have coastlines")
my_table3_filtered = my_table3.filter(lambda x: x['EU'] == 'yes').filter(lambda x: x['coastline'] == 'no')
print("Min temp:", my_table3_filtered.aggregate(lambda x: min(x), 'temperature'))
print("Max temp:", my_table3_filtered.aggregate(lambda x: max(x), 'temperature'))
print()