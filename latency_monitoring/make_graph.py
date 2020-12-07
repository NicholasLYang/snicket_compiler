import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
import csv
import pandas as pd

INPUT_FILE = "input_file.csv"


def make_graph(input_file):
    data = []
    valid_data = 0
    total_data = 0
    dividers = np.linspace(0,5,51).tolist()
    for d in range(len(dividers)):
        dividers[d] = round(dividers[d], 1)

    divider_to_index = {}
    for i in range(len(dividers)):
        divider_to_index[dividers[i]] = i

    with open(input_file) as file:
        reader = csv.reader(file)
        for row in reader:
            row = row[-1].split()
            if "seconds" not in row[-1]:
                total_data += 1
                if "...." not in row[-1]: # this is a valid latency
                    valid_data += 1
                    data.append(float(row[-1])) # only add latency in seconds
    data = pd.DataFrame(data) 
    binned_data = pd.cut(data[0], bins=dividers)

    data_to_graph = []
    for divider in dividers:
        data_to_graph.append(0)
    for datapoint in binned_data:
        data_to_graph[divider_to_index[datapoint.left]] += 1


    # convert everything to dataframe so it can be graphed
    data_to_graph = pd.DataFrame(data_to_graph)
    dividers = pd.DataFrame(dividers)
    input_to_graph = pd.concat([data_to_graph, dividers], axis=1)
    input_to_graph.columns = ["latency", "bins"]
    import pdb; pdb.set_trace()




def main(args):
    make_graph(args.input_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Make a graph from data.')
    parser.add_argument("-i", "--input_file", dest="input_file",
                        default=INPUT_FILE,
                        help="File of data to make a graph of. ")

    arguments = parser.parse_args()
    main(arguments)