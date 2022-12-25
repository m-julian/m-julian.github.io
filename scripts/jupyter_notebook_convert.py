#!/usr/bin/env python3
"""
Convert jupyter notebook into Jekyll blogpost.
Adapted from https://github.com/peterroelants/peterroelants.github.io/tree/main/notebooks

Example useage:
```
python new_convert.py --nbpath <filename>.ipynb
```
"""
import os
from pathlib import Path
import argparse
from nbconvert import HTMLExporter
from nbconvert.preprocessors import CSSHTMLHeaderPreprocessor
from bs4 import BeautifulSoup
import datetime

# Get the base directory of this project relative to this script
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

# Get input arguments

today = datetime.date.today()

parser = argparse.ArgumentParser(
    description='Convert notebook to Jekyll blogpost.')
parser.add_argument(
    '--nbpath', type=str,
    help='File path of notebook file to convert to blogpost')
parser.add_argument(
    '--date', type=str,
    help='Date of original publication of post.')
parser.add_argument(
    '--layout', type=str,
    help='Layout template name to use as Jekyll layout for blogpost.')
parser.add_argument(
    '--description', type=str,
    help='Description of the blogpost.')


def nb2html(nb_filepath):
    """
    Convert notebook to html string.

    Args:
        nb_filepath (str): Path of notbook file

    Returns:
        (str): HMTL of converted notebook.
    """
    exporter = HTMLExporter()
    # https://nbconvert.readthedocs.io/en/latest/usage.html#convert-html
    exporter.template_name = 'basic' # Simplified HTML, useful for embedding in webpages, blogs, etc. This excludes HTML headers.
    output, resources = exporter.from_filename(nb_filepath)
    return output

def remove_output_stderr(soup):
    """
    Remove the `output_stderr` elements from the notebook outputs.

    Args:
        soup (BeautifulSoup): HTML parsed notebook.

    Effect:
        Changes soup object to have divs with class `output_stderr` removed.
    """
    for div in soup.find_all('div', {'class':'output_stderr'}):
        div.decompose()

def add_table_class(soup):
    """
    Add `.table` class to table dataframe.
    Now pandas tables are visualised by html `<table class="dataframe">`. To
     be able to use bootstrap tables they need to have the `.table` class.
     https://getbootstrap.com/docs/4.0/content/tables/
    Args:
        soup (BeautifulSoup): HTML parsed notebook.

    Effect:
        Changes soup object to have divs with class `output_stderr` removed.
    """
    for table in soup.find_all('table', {'class':'dataframe'}):
        if "class" in table.attrs:
            del table.attrs["class"]
        table['class'] = table.get('class', []) + ['table']
        if "border" in table.attrs:
            del table.attrs["border"]
    for thead in soup.find_all("thead"):
        thead["class"] = thead.get("class", []) + ["thead-dark"]
    for table_row in soup.find_all('tr'):
        if "style" in table_row.attrs:
            del table_row.attrs["style"]

def set_anchor_links(soup: BeautifulSoup):
    """
    Set the anchor links to link symbol
    Effect:
        Change anchor-link content to link symbol.
    """
    for a_tag in soup.find_all("a", {"class": "anchor-link"}):
        # Remove previous content
        a_tag.string = ""
        # Insert link symbol as tag
        a_tag.append(soup.new_tag("i", attrs={"class": "fas fa-sm fa-link"}))

def save_conversion(html_str, nbpath, date):
    """
    Save converted notebook file to Jekyll templated html file.

    args:
        html_str (str): Jekyll templated html str.
        nbpath (str): Filepath of original notebook file.
        date (str): Blogpost orginal publishing date (YYYY-MM-DD)

    Effect:
    """
    filename = Path(nbpath).stem
    output_path = os.path.join(
        BASE_DIR, f'{date}-{filename}.html')
    print('output_path: ', output_path)
    with open(output_path, 'w+') as f:
        f.write(html_str)

def main():
    """Run conversion script."""
    args = parser.parse_args()
    print('\nConverting: ', args.nbpath)
    html_str = nb2html(args.nbpath)
    soup = BeautifulSoup(html_str, 'html.parser')
    remove_output_stderr(soup)
    set_anchor_links(soup)
    add_table_class(soup)
    html_str = soup.prettify()
    save_conversion(html_str, args.nbpath, today)

if __name__ == "__main__":
    main()








