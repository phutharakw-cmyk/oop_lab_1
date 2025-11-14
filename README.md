# 🧮 Data Processing of Country CSV File

This is a basic Python data processing project that calculates or filters data from a CSV file.  
It works similarly to Google Sheets — like what I learned from a previous lab.

---

## File Structure

- `data_processing.py`: The main Python program that contains all the classes and functions.  
- `Cities.csv`: The dataset used by the program for processing.
- `Countries.csv`: The anoter dataset used by the program for processing.

---

## Classes Overview

Located in `data_processing.py`, the **`Table`** and **`DataLoader`** classes include:

### Attributes
- `loader` (object): The object created from the `DataLoader` class.  
- `cities` (list): The list of data loaded from the CSV file.  
- `my_table1` (object): The object created from the `Table` class.

### Methods
- `filter(condition)`: Filters the data using a custom condition.  
- `aggregate(aggregate_function, aggregate_key)`: Calculates or summarizes data (e.g., average, max, count).  
- `table()`: Returns the filtered list of dictionaries.

---

## How the Code Works

1. The program creates a `DataLoader` object to load data from `Cities.csv`.  
2. It initializes a `Table` object (`my_table1`) containing the CSV data.  
3. Various filters and aggregate functions are applied to answer specific questions
   for example:
   - Find all cities in Germany  
   - Calculate the average temperature of all cities  
   - Find the max temperature in Italy  

---

## Running the Program

To run the program, open a terminal in this folder and execute:

```bash
python data_processing.py

