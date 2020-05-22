"""
Project for Week 3 of "Python Data Visualization".
Unify data via common country name.
"""

import csv
import math
import pygal

pygal_countries = pygal.maps.world.COUNTRIES

gdpinfo = {
    "gdpfile": "isp_gdp.csv",
    "separator": ",",
    "quote": '"',
    "min_year": 1960,
    "max_year": 2015,
    "country_name": "Country Name",
    "country_code": "Country Code"
}


def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - Name of CSV file
      keyfield  - Field to use as key for rows
      separator - Character that separates fields
      quote     - Character used to optionally quote fields

    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    nested_dict = {}
    with open(filename, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        for row in csvreader:
            rowid = row[keyfield]
            nested_dict[rowid] = row
    return nested_dict


def reconcile_countries_by_name(plot_countries, gdp_countries):
    """
    Inputs:
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      gdp_countries  - Dictionary whose keys are country names used in GDP data

    Output:
      A tuple containing a dictionary and a set.  The dictionary maps
      country codes from plot_countries to country names from
      gdp_countries The set contains the country codes from
      plot_countries that were not found in gdp_countries.
    """
    country_codes = {}
    missing_counts = set()
    for code, country in plot_countries.items():
        if country in gdp_countries:
            country_codes[code] = country
        else:
            missing_counts.add(code)
    return country_codes, missing_counts


def build_map_dict_by_name(gdpinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for

    Output:
      A tuple containing a dictionary and two sets.  The dictionary
      maps country codes from plot_countries to the log (base 10) of
      the GDP value for that country in the specified year.  The first
      set contains the country codes from plot_countries that were not
      found in the GDP data file.  The second set contains the country
      codes from plot_countries that were found in the GDP data file, but
      have no GDP data for the specified year.
    """
    country_codes = {}
    not_found = set()
    no_data = set()

    filename = gdpinfo["gdpfile"]
    keyfield = gdpinfo['country_name']
    separator = gdpinfo["separator"]
    quote = gdpinfo["quote"]
    gdpdata = read_csv_as_nested_dict(filename, keyfield, separator, quote)

    codes, not_found = reconcile_countries_by_name(plot_countries, gdpdata)

    for code in codes:
        for country in gdpdata:
            if codes[code] == country:
                if year in gdpdata[country]:
                    if gdpdata[country][year] != "":
                        country_codes[code] = math.log10(float(gdpdata[country][year]))
                    else:
                        no_data.add(code)
                else:
                    not_found.add(code)
    return country_codes, not_found, no_data


def render_world_map_in_file(gdpinfo, plot_countries, year, map_file):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for
      map_file       - Name of output file to create

    Output:
      Returns None.

    Action:
      Creates a world map plot of the GDP data for the given year and
      writes it to a file named by map_file.
    """
    country_codes, not_found, no_data = build_map_dict_by_name(gdpinfo, plot_countries, year)

    gdp_worldmap_chart = pygal.maps.world.World()
    title = "GDP by country for {} (log scale), unified by common country name".format(year)
    gdp_worldmap_chart.title = title
    gdp_worldmap_chart.add('GDP for {}'.format(year), country_codes)
    gdp_worldmap_chart.add('Missing from World Bank Data', not_found)
    gdp_worldmap_chart.add('No GDP data', no_data)
    gdp_worldmap_chart.render_to_file(map_file)

    return


def render_world_map_in_browser(gdpinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for

    Output:
      Returns None.

    Action:
      Creates a world map plot of the GDP data for the given year and
      writes it to a file named by map_file.
    """
    country_codes, not_found, no_data = build_map_dict_by_name(gdpinfo, plot_countries, year)

    gdp_worldmap_chart = pygal.maps.world.World()
    title = "GDP by country for {} (log scale), unified by common country name".format(year)
    gdp_worldmap_chart.title = title
    gdp_worldmap_chart.add('GDP for {}'.format(year), country_codes)
    gdp_worldmap_chart.add('Missing from World Bank Data', not_found)
    gdp_worldmap_chart.add('No GDP data', no_data)
    gdp_worldmap_chart.render_in_browser()

    return
