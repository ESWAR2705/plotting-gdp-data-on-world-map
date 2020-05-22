"""
Project for Week 4 of "Python Data Visualization".
Unify data via common country codes.
"""

import csv
import math
import pygal
import os

gdpinfo = {
    "gdpfile": "isp_gdp.csv",
    "separator": ",",
    "quote": '"',
    "min_year": 1960,
    "max_year": 2015,
    "country_name": "Country Name",
    "country_code": "Country Code"
}

codeinfo = {
    "codefile": "isp_country_codes.csv",
    "separator": ",",
    "quote": '"',
    "plot_codes": "ISO3166-1-Alpha-2",
    "data_codes": "ISO3166-1-Alpha-3"
}

plot_countries = pygal.maps.world.COUNTRIES

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


def build_country_code_converter(codeinfo):
    """
    Inputs:
      codeinfo      - A country code information dictionary

    Output:
      A dictionary whose keys are plot country codes and values
      are world bank country codes, where the code fields in the
      code file are specified in codeinfo.
    """
    codes_dict = {}

    codefile = codeinfo["codefile"]
    keyfield = codeinfo["plot_codes"]
    separator = codeinfo["separator"]
    quote = codeinfo["quote"]
    codeinfo_data = read_csv_as_nested_dict(codefile, keyfield, separator, quote)

    for code in codeinfo_data:
        data_code = codeinfo["data_codes"]
        codes_dict[code] = codeinfo_data[code][data_code]

    return codes_dict


def reconcile_countries_by_code(codeinfo, plot_countries, gdp_countries):
    """
    Inputs:
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      gdp_countries  - Dictionary whose keys are country codes used in GDP data

    Output:
      A tuple containing a dictionary and a set.  The dictionary maps
      country codes from plot_countries to country codes from
      gdp_countries.  The set contains the country codes from
      plot_countries that did not have a country with a corresponding
      code in gdp_countries.

      Note that all codes should be compared in a case-insensitive
      way.  However, the returned dictionary and set should include
      the codes with the exact same case as they have in
      plot_countries and gdp_countries.
    """
    codes_mapping = {}
    not_found = set()
    converted_codes = build_country_code_converter(codeinfo)

    converted_codes_uppercase = {}
    for item in converted_codes:
        converted_codes_uppercase[item.upper()] = converted_codes[item]

    gdp_uppercase_keys = []
    for key in gdp_countries:
        gdp_uppercase_keys.append(key.upper())

    for pygal_code in plot_countries:
        uppercase_code = pygal_code.upper()
        if uppercase_code in converted_codes_uppercase:
            if converted_codes_uppercase[uppercase_code].upper() in gdp_uppercase_keys:
                codes_mapping[pygal_code] = converted_codes_uppercase[uppercase_code]

    for pygal_code in plot_countries:
        if pygal_code not in codes_mapping:
            not_found.add(pygal_code)

    return codes_mapping, not_found


def build_map_dict_by_code(gdpinfo, codeinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary mapping plot library country codes to country names
      year           - String year for which to create GDP mapping

    Output:
      A tuple containing a dictionary and two sets.  The dictionary
      maps country codes from plot_countries to the log (base 10) of
      the GDP value for that country in the specified year.  The first
      set contains the country codes from plot_countries that were not
      found in the GDP data file.  The second set contains the country
      codes from plot_countries that were found in the GDP data file, but
      have no GDP data for the specified year.
    """
    plot_dict = {}
    not_found = set()
    no_data = set()

    filename = gdpinfo["gdpfile"]
    keyfield = gdpinfo['country_code']
    separator = gdpinfo["separator"]
    quote = gdpinfo["quote"]
    gdp_countries = read_csv_as_nested_dict(filename, keyfield, separator, quote)

    codes_mapping, not_found = reconcile_countries_by_code(codeinfo, plot_countries, gdp_countries)

    for code in codes_mapping:
        for gdp_code in gdp_countries:
            if codes_mapping[code].upper() == gdp_code.upper():
                if year in gdp_countries[gdp_code]:
                    if gdp_countries[gdp_code][year] != "":
                        plot_dict[code] = math.log10(float(gdp_countries[gdp_code][year]))
                    else:
                        no_data.add(code)

    return plot_dict, not_found, no_data


def render_world_map_in_file(gdpinfo, codeinfo, plot_countries, year, map_file):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary mapping plot library country codes to country names
      year           - String year of data
      map_file       - String that is the output map file name

    Output:
      Returns None.

    Action:
      Creates a world map plot of the GDP data in gdp_mapping and outputs
      it to a file named by svg_filename.
    """
    country_codes, not_found, no_data = build_map_dict_by_code(gdpinfo, codeinfo, plot_countries, year)

    gdp_worldmap_chart = pygal.maps.world.World()
    title = "GDP by country for {} (log scale), unified by common country code".format(year)
    gdp_worldmap_chart.title = title
    gdp_worldmap_chart.add('GDP for {}'.format(year), country_codes)
    gdp_worldmap_chart.add('Missing from World Bank Data', not_found)
    gdp_worldmap_chart.add('No GDP data', no_data)
    gdp_worldmap_chart.render_to_file(map_file)

    return


def render_world_map_in_browser(gdpinfo, codeinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary mapping plot library country codes to country names
      year           - String year of data

    Output:
      Returns None.

    Action:
      Creates a world map plot of the GDP data in gdp_mapping and outputs
      it to a browser.
    """
    country_codes, not_found, no_data = build_map_dict_by_code(gdpinfo, codeinfo, plot_countries, year)

    gdp_worldmap_chart = pygal.maps.world.World()
    title = "GDP by country for {} (log scale), unified by common country code".format(year)
    gdp_worldmap_chart.title = title
    gdp_worldmap_chart.add('GDP for {}'.format(year), country_codes)
    gdp_worldmap_chart.add('Missing from World Bank Data', not_found)
    gdp_worldmap_chart.add('No GDP data', no_data)
    gdp_worldmap_chart.render_in_browser()

    return


# Get user input
year = input("Enter year to build map: ")
if int(gdpinfo["min_year"]) <= int(year) <= int(gdpinfo["max_year"]):
    mode = input("Enter 1 to render map in browser or 2 to render map in file :")
    if mode == "1":
        render_world_map_in_browser(gdpinfo, codeinfo, plot_countries, year)
    elif mode == "2":
        map_file = input("Enter file name to save GDP data with svg extension: ")
        result = os.path.splitext(map_file)
        if result[1] == ".svg":
            render_world_map_in_file(gdpinfo, codeinfo, plot_countries, year, map_file)
        else:
            print("Enter a file name with valid extension.")
    else:
        print("Choose a valid option to render map.")
else:
    print("There is no data in your .csv file for this year.")
