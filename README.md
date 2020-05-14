# Plotting GDP Data on World Map
**Plotting GDP Data on World Map** is the final project of the [Python Data Visualization](https://www.coursera.org/learn/python-visualization/home/welcome)course on Coursera platform. 

The main task of this project is to process the World Bank GDP data and build a dictionary whose values represented the GDP data for a given year that can be plotted with [Pygal](http://www.pygal.org/en/stable/index.html). 

The project consists of two parts.
* [Part 1](#part1). To link Pygal's map dictionary (mapping 2-letter country codes to country names) to a dictionary that stored World Bank GDP country data keyed by the "Country Name" field and to plot GDP data on world map. 
* [Part 2](#part2). To improve the quality of the world map plots created in Part 1 by creating a better mapping from pygal country codes to World Bank country names.
## Part 1 <a name="part1"></a>
In Part 1 the following problems are solved.
1. Creating a dictionary that maps Pygal country codes to World Bank country names

The **reconcile_countries_by_name** function takes ```plot_countries```, a dictionary mapping country codes used by a plot library (such as *Pygal*) to the corresponding country name, and ```gdp_countries```, a dictionary whose keys are the country names used within the GDP data. 

The **reconcile_countries_by_name** function should return a dictionary and a set. The dictionary should map the country codes from ```plot_countries``` to country names that match between ```plot_countries``` and ```gdp_countries```. It should not contain key-value pairs for the countries within ```plot_countries``` that do not appear in ```gdp_countries```. The set should contain all of the country codes within ```plot_countries``` that did not match any countries in ```gdp_countries```, so is effectively the set of countries that the plot library knows about, but cannot be found within the GDP data.

2. Transforming GDP data for given year into a form suitable for a world map plot

The **build_map_dict_by_name** function takes ```gdpinfo```, a GDP information dictionary, ```plot_countries```, a dictionary mapping country codes used by a plot library (such as *Pygal*) to the corresponding country name, and ```year```, the year for which to create a GDP map dictionary, expressed as a string.

The **build_map_dict_by_name** function should return a dictionary and two sets. The dictionary should map the country codes from ```plot_countries``` to the log (base 10) of the GDP for the associated country in the given year. (The logarithmic scaling is chosen to yield a better distribution of color shades in the final plot.) The first set should contain the country codes from ```plot_countries``` that were not found in the GDP data file. The second set contains the country codes from ```plot_countries``` that were found in the GDP data file, but have no GDP information for the specified year.

3. Creating an SVG image of the GDP data plotted on the world map

The **render_world_map** function takes ```gdpinfo```, a GDP information dictionary, ```plot_countries```, a dictionary mapping country codes used by *Pygal* to the corresponding country name, and ```year```, the string year for which to create a GDP map dictionary, and ```map_file```, the string name of the file to write the output plot to.

## Part 2 <a name="part2"></a>
In Part 2 the following problems are solved.

1. Generate a dictionary that maps different country codes to each other

The **build_country_code_converter** function takes ```codeinfo```, a country code info dictionary, and returns a dictionary that maps plot country codes to data country codes.

2. Create a dictionary that maps *Pygal* country codes to *World Bank* country codes

The **reconcile_countries_by_code** function takes ```codeinfo```, a country code information dictionary, ```plot_countries```, a dictionary mapping country codes used by a plot library (such as *Pygal)* to the corresponding country name, and ```gdp_countries```, a dictionary whose keys are the country codes used within the GDP data.

3. Transform GDP data for given year into a form suitable for a world map plot

The **build_map_dict_by_code** function takes ```gdpinfo```, a GDP information dictionary, ```codeinfo```, a country code information dictionary, ```plot_countries```, a dictionary mapping country codes used by a plot library (such as *Pygal*) to the corresponding country name, and ```year```, the year for which to create a GDP map dictionary, expressed as a string. 

The **build_map_dict_by_code** function should return a dictionary and two sets. The dictionary should map the country codes from ```plot_countries``` to the log (base 10) of the GDP for the associated country in the given year. (The logarithmic scaling is chosen to yield a better distribution of color shades in the final plot.) The first set should contain the country codes from ```plot_countries``` that were not found in the GDP data file. The second set contains the country codes from ```plot_countries``` that were found in the GDP data file, but have no GDP information for the specified year.

4. Create an SVG image of the GDP data plotted on the world map

The **render_world_map** function takes ```gdpinfo```, a GDP information dictionary, ```codeinfo```, a country code information dictionary, ```plot_countries```, a dictionary mapping country codes used by *Pygal* to the corresponding country name, and ```year```, the string year for which to create a GDP map dictionary, and ```map_file```, the string name of the file to write the output plot to.
## Data Used
### ```plot_countries``` dictionary
The ```plot_countries``` is a dictionary mapping country codes used by *Pygal* to the corresponding country name. It has the following format.
```sh
ad Andorra
ae United Arab Emirates
af Afghanistan
al Albania
am Armenia
...
```
### GDP information dictionary ```gdpinfo```

The ```gdpinfo``` dictionary contains the raw economic data collected by the World Bank. The ```isp_gdp.csv``` file with data on GDP in current US dollars is downloaded from [course materials](https://storage.googleapis.com/codeskulptor-isp/course4/isp_gdp.csv). The first two columns correspond to the *"Country Name"* and *"Country Code"* for each country in the file. Subsequent fields include GDP data (in current US dollars) for the years from 1960-2015 inclusive.

 **Important!** This file is slightly modified to handle missing GDP data in a more consistent manner.
 
As the format of the CSV file that stores the GDP data could change (or you could acquire data from somewhere else), the functions that operate directly on the data will all take a "gdpinfo" dictionary that provides information about the file. 

```sh
    gdpinfo = {
        "gdpfile": "isp_gdp.csv",        # Name of the GDP CSV file
        "separator": ",",                # Separator character in CSV file
        "quote": '"',                    # Quote character in CSV file
        "min_year": 1960,                # Oldest year of GDP data in CSV file
        "max_year": 2015,                # Latest year of GDP data in CSV file
        "country_name": "Country Name",  # Country name field name
        "country_code": "Country Code"   # Country code field name
    }
```

## Prerequisites
To run the project, **Pygal** Python module is required. It is available in [PyPI](https://pypi.org/), and can be installed by typing the following command as *superuser*.
```sh
pip install pygal
```
The application can be used explicitely with ```isp_gdp.csv file```. The current version of isp_gdp.csv file is downloaded from [course materials](https://storage.googleapis.com/codeskulptor-isp/course4/isp_gdp.csv). It contains GDP data up until the end of 2015, and this file is slightly updated to handle missing GDP data in a more consistent manner.

To use data from another file (including files with other separators), change the ```gdpinfo``` dictionary structure accordingly.
```sh
    gdpinfo = {
        "gdpfile": "isp_gdp.csv",        # Name of the GDP CSV file
        "separator": ",",                # Separator character in CSV file
        "quote": '"',                    # Quote character in CSV file
        "min_year": 1960,                # Oldest year of GDP data in CSV file
        "max_year": 2015,                # Latest year of GDP data in CSV file
        "country_name": "Country Name",  # Country name field name
        "country_code": "Country Code"   # Country code field name
    }
```
The application also can be used explicitely with ```isp_country_codes.csv``` file.
```sh
codeinfo = {
        "codefile": "isp_country_codes.csv", # Name of the country code CSV file
        "separator": ",",                    # Separator character in CSV file
        "quote": '"',                        # Quote character in CSV file
        "plot_codes": "ISO3166-1-Alpha-2",   # Plot code field name
        "data_codes": "ISO3166-1-Alpha-3"    # GDP data code field name
    }
```
## Running
To get GDP by country unified by common name, run the following command.
```sh
$ python unify_via_name.py
```
To get GDP by country unified by common code, run the following command.
```sh
$ python unify_via_code.py
```
## Authors
Alexandra Baturina
