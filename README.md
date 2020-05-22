# Plotting GDP Data on World Map
## Overwiew
**Plotting GDP Data on World Map** is the final project of the [Python Data Visualization](https://www.coursera.org/learn/python-visualization/home/welcome)course on Coursera platform. 

The main task of this project is to process the World Bank GDP data and build a dictionary whose values represented the GDP data for a given year that can be plotted with [Pygal](http://www.pygal.org/en/stable/index.html). 
## Features
The project consists of two parts.
* [Part 1](#part1). To link Pygal's map dictionary (mapping 2-letter country codes to country names) to a dictionary that stored World Bank GDP country data keyed by the "Country Name" field and to plot GDP data on world map. 
* [Part 2](#part2). To improve the quality of the world map plots created in Part 1 by creating a better mapping from pygal country codes to World Bank country names.
### Part 1 <a name="part1"></a>
In Part 1 the following problems are solved.
1. Create a dictionary that maps Pygal country codes to World Bank country names (**reconcile_countries_by_name** function).
2. Transform GDP data for given year into a form suitable for a world map plot (**build_map_dict_by_name** function). 

The dictionary should map the country codes from ```plot_countries``` to the log (base 10) of the GDP for the associated country in the given year. (The logarithmic scaling is chosen to yield a better distribution of color shades in the final plot.) 

3. Create an SVG image of the GDP data plotted on the world map (**render_world_map_in_file** function).
5. Render the GDP data plotted on the world map in browser (**render_world_map_in_browser** function).

### Part 2 <a name="part2"></a>
In Part 2 the following problems are solved.

1. Generate a dictionary that maps different country codes to each other (**build_country_code_converter** function).
2. Create a dictionary that maps *Pygal* country codes to *World Bank* country codes (**reconcile_countries_by_code** function).
3. Transform GDP data for given year into a form suitable for a world map plot (**build_map_dict_by_code** function). 
4. Create an SVG image of the GDP data plotted on the world map (**render_world_map_in_file** function).
5. Render the GDP data plotted on the world map in browser (**render_world_map_in_browser** function).

In both parts of the project, for **build_map_dict_by_code** function the logarithmic scaling is chosen to yield a better distribution of color shades in the final plot.

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
### ```gdpinfo``` dictionary <a name="gdpinfo"></a>
The ```gdpinfo``` is a GDP information dictionary. It specifies information about GDP data file. The current GDP data file ```isp_gdp.csv``` is downloaded from [course materials](https://storage.googleapis.com/codeskulptor-isp/course4/isp_gdp.csv) and contains the raw economic data collected from the World Bank. The first two columns of CSV file correspond to the *"Country Name"* and *"Country Code"* for each country in the file. Subsequent fields include GDP data (in current US dollars) for the years from 1960-2015 inclusive.

 **Important!** The current ```isp_gdp.csv``` file is slightly modified to handle missing GDP data in a more consistent manner.
 
As the format of the CSV file that stores the GDP data could change (or you could acquire data from somewhere else), the functions that operate directly on the data will all take a "gdpinfo" dictionary that provides information about the file. 

The ```gdpinfo``` dictionary contains the following items.

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
### ```codeinfo``` dictionary <a name="codeinfo"></a>
The ```codeinfo``` is a country code information dictionary that is used to access the country codes from the Open Knowledge Network's [collection](http://data.okfn.org/data/core/country-codes). The current version of country codes data is organised in ```isp_country_codes.csv``` file downloaded from [course materials](https://storage.googleapis.com/codeskulptor-isp/course4/isp_country_codes.csv).

 **Important!** The current ```isp_country_codes.csv``` file is slightly modified to handle missing GDP data in a more consistent manner.
 
The ```codeinfo``` dictionary contains the following items.
 
```sh
codeinfo = {
        "codefile": "isp_country_codes.csv", # Name of the country code CSV file
        "separator": ",",                    # Separator character in CSV file
        "quote": '"',                        # Quote character in CSV file
        "plot_codes": "ISO3166-1-Alpha-2",   # Plot code field name
        "data_codes": "ISO3166-1-Alpha-3"    # GDP data code field name
    }
```
### ```gdp_countries```, a dictionary whose keys are the country names used within the GDP data. 
## Dev Dependencies
Cool tech stuff used in this project.
* **Pygal** Python data visualization library
  * http://www.pygal.org/en/stable/documentation/index.html
* Pyhton **csv** library
  * https://docs.python.org/3/library/csv.html
* Python **math** library
  * https://docs.python.org/3/library/math.html
http://www.pygal.org/en/stable/index.html
## Getting Started
### Prerequisites
To run the project, **Pygal** Python module is required. It is available in [PyPI](https://pypi.org/), and can be installed by typing the following command as *superuser*.
```sh
pip install pygal
```
The application can be used explicitely with ```isp_gdp.csv``` and ```isp_country_codes.csv``` files. To use data from another files, change the [```gdpinfo```](#gdpinfo) or [```codeinfo```](#codeinfo) dictionary structure accordingly.

To render GDP plot in file, invoke **render_world_map_in_file** function.
To render GDP plot in browser, invoke **render_world_map_in_browser** function.
By default,  **render_world_map_in_browser** function is invoked.

### Running
To get GDP by country unified by common name, run the following command.
```sh
$ python unify_via_name.py
```
To get GDP by country unified by common code, run the following command.
```sh
$ python unify_via_code.py
```
Example of plotting GDP data on world map is shown below.
![image](https://user-images.githubusercontent.com/53233637/82405590-373fa800-9a19-11ea-9358-8283348ebebf.png)

## Authors
Alexandra Baturina
