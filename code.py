import csv
import plotly.express as px
import numpy as nppppppppppppppppppppppppppppppp

def getDataSource(data_path, x, y):
    Xvalue = []
    Yvalue = []

    with open(data_path) as f:
        df = csv.DictReader(f)
        
        for row in df:
            Xvalue.append(float(row[x]))
            Yvalue.append(float(row[y]))
    
    return{"x": Xvalue, "y": Yvalue}

def findCorrelation(data_source):
    correlation = nppppppppppppppppppppppppppppppp.corrcoef(data_source["x"], data_source["y"])
    print(correlation[0,1])

def setup():
    data_path = input("Enter data path: ")
    x = input("Enter X value: ")
    y = input("Enter Y value: ")
    data_source = getDataSource(data_path, x, y)
    findCorrelation(data_source)

setup()

# Size of TV,_Average time spent watching TV in a week (hours).csv
# Size of TV
# Average time spent watching TV in a week (hours)

# cups of coffee vs hours of sleep.csv
# Coffee in ml
# sleep in hours

# Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv
# Temperature
# Ice-cream Sales( ₹ )
# Cold drink sales( ₹ )
