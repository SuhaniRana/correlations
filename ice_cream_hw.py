import csv
import numpy as np


def getDataSource(data_path):
    ice_cream = []
    temp = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            ice_cream.append(float(row["Ice-cream Sales"]))
            temp.append(float(row["\tTemperature"]))

    return {"x" : ice_cream, "y": temp}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between emperature and ice cream sales :-  \n--->",correlation[0,1])

def setup():
    data_path  = "./data/Ice-Cream vs Cold-Drink vs Temperature"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()
