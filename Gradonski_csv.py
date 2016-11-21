__author__ = "Gradonski Janusz"
__license__ = "GPL"
__version__ = "1.0"

import csv
import sys


def sniff_dialect(sample):
    POSSIBLE_DELIMITERS = [',', '\t', ';', ' ', ':', '|']
    try:
        dialect = csv.Sniffer().sniff(sample, POSSIBLE_DELIMITERS)
    except:
        dialect = None

    return dialect


def readcsv():
    """
    Liest aus CSV-File in den Hauptpseicher gibt es separiert mit einem Beistrich aus
    :return:
    """
    with open("cabc.csv") as csvred:

        dialect=sniff_dialect(csvred)
        csvred.seek(0)

        r= csv.reader(csvred, dialect)
        for row in r:
            print(', '.join(row))

        csvred.close()


def readcsvlist():
    """
    List CSV-File und gibt es in eine Liste
    :return:
    """
    liste=[]
    with open("abc.csv") as csvlist:
        dialect = sniff_dialect(csvlist)
        csvlist.seek(0)

        r=csv.reader(csvlist, dialect)
        for row in r:
            liste.append(row)
        return liste
        csvlist.close()

def csv_dict_writer(path, fieldnames, data):
    """
    Schreibt Daten in ein CSV file mit dem Beistrich als Delimiter
    :param path:
    :param fieldnames:
    :param data:
    :return:
    """
    with open(path, "w") as out_file:
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


if  __name__== '__main__':
    readcsv()
    data = readcsvlist()

    my_list = []
    fieldnames = data[0]
    for values in data[1:]:
        inner_dict = dict(zip(fieldnames, values))
        my_list.append(inner_dict)

    path = "output.csv"
    csv_dict_writer(path, fieldnames, my_list)
