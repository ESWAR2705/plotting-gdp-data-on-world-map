# Plotting GDP Data on World Map
**Plotting GDP Data on World Map** is the final project of the [Python Data Visualization](https://www.coursera.org/learn/python-visualization/home/welcome)course on Coursera platform. It consists of two parts.
* [Part 1](#part1): To link Pygal's map dictionary (mapping 2-letter country codes to country names) to a dictionary that stored World Bank GDP country data keyed by the "Country Name" field and to plot GDP data on world map. 
* [Part 2](#part2): To improve the quality of the world map plots created in Part 1 by creating a better mapping from pygal country codes to World Bank country names.
## Part 1 <a name="part1"></a>
In **Part 1** of the project the following problems are solved.
1. Creating a dictionary that maps Pygal country codes to World Bank country names (**reconcile_countries_by_name** function).
2. Transforming GDP data for given year into a form suitable for a world map plot (**build_map_dict_by_name** function).
3. Creating an SVG image of the GDP data plotted on the world map (**render_world_map** function).
## Part 2 <a name="part2"></a>
In **Part 2** or the project the following problems are solved.

1. Generate a dictionary that maps different country codes to each other

The **build_country_code_converter** function takes ```codeinfo```, a country code info dictionary, and returns a dictionary that maps plot country codes to data country codes.

2. Create a dictionary that maps *Pygal* country codes to *World Bank* country codes

The **reconcile_countries_by_code** function takes ```codeinfo```, a country code information dictionary, ```plot_countries```, a dictionary mapping country codes used by a plot library (such as *Pygal)* to the corresponding country name, and ```gdp_countries```, a dictionary whose keys are the country codes used within the GDP data.

3. Transform GDP data for given year into a form suitable for a world map plot

The **build_map_dict_by_code** function takes ```gdpinfo```, a GDP information dictionary, ```codeinfo```, a country code information dictionary, ```plot_countries```, a dictionary mapping country codes used by a plot library (such as *Pygal*) to the corresponding country name, and ```year```, the year for which to create a GDP map dictionary, expressed as a string. 

The **build_map_dict_by_code** function should return a dictionary and two sets. The dictionary should map the country codes from ```plot_countries``` to the log (base 10) of the GDP for the associated country in the given year. (The logarithmic scaling is chosen to yield a better distribution of color shades in the final plot.) The first set should contain the country codes from ```plot_countries``` that were not found in the GDP data file. The second set contains the country codes from ```plot_countries``` that were found in the GDP data file, but have no GDP information for the specified year.

4. Create an SVG image of the GDP data plotted on the world map

The **render_world_map** function takes ```gdpinfo```, a GDP information dictionary, ```codeinfo```, a country code information dictionary, ```plot_countries```, a dictionary mapping country codes used by *Pygal* to the corresponding country name, and ```year```, the string year for which to create a GDP map dictionary, and ```map_file```, the string name of the file to write the output plot to.
