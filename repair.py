import csv # csv library
import re # regular expression library
import pandas as pd

def remove_dollar_sign(input_file: str, output_file: str):
    """
    Function manipulates the data by:
    - removing dollar sign from price column

    @param input_file: file to read from
    @param output_file: file containing the cleaned dataset
    """

    with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", newline="", encoding="utf-8") as output:
        reader = csv.reader(infile)
        wter = csv.writer(output, delimiter=",")
        for row in reader:
            row[7] = re.sub("\$", "", row[7])
            wter.writerow(row)
        
        print("repair.py: Printing done")

def fill_missing_values_rating(df):
    """
    For the rating column, we decided to substitute missing values as 0.0 as we felt that it would
    make more sense rather than using the average of the non-missing values.
    """
    df["Rating"].fillna(0, inplace=True)

def fill_missing_values_type(df):
    """
    For the type column, as there's only 1 row where the type is empty and that
    the price is 0.0, we decided to replace it with the "Free" type
    """
    df["Type"].fillna("Free", inplace=True)

def fill_missing_values_genres(df):
    """
    For the genres column, there is only 1 row where the genres field is empty.
    As the category it is under is LIFESTYLE, we would substitute the missing value as 
    "Lifestyle"
    """
    df["Genres"].fillna("Lifestyle", inplace=True)

def fill_missing_values_currversion(df):
    """
    For the Current Ver column, we decided to fill all missing values as "Varies with device"
    as there is a high probabiliity (according to the frequency table) that the current version
    would be "Varies with device
    """
    df["Current Ver"].fillna("Varies with device", inplace=True)

def fill_missing_values_androidversion(df):
    """
    For the Android Ver column, we decided to fill all missing values as "4.1 and up" as there
    is a high probability that the android version would be 4.1 and up. 
    """
    df["Android Ver"].fillna("4.1 and up", inplace=True)

