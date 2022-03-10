from datetime import datetime
import numpy as np
import networkx as nx
from pyvis.network import Network

class uwn:
    def __init__(self, matrix, word_list):
        self.matrix = matrix
        self.word_list = word_list
        word_list.sort()

    def mean_degree(self):
        somme = 0
        for i in range(len(self.matrix[0])):
            for j in range(len(self.matrix[0])):
                somme += self.matrix[i][j]
        return somme / len(self.matrix[0])

    def mat_to_csv(self):
        f = open(f'./network_mapping/Network_{datetime.now().strftime("%d%m%Y_%H%M%S")}.csv', 'a')
        f.write(str(len(self.matrix[0])) + ",,\n")
        f.write("node i, node j, weight\n")
        for i in range(len(self.matrix[0]) - 1):
            for j in range(i + 1, len(self.matrix[0])):
                f.write(str(self.word_list[i]) + "," + str(self.word_list[j]) + "," + str(int(self.matrix[i][j])) + "\n")
        f.close()

    def csv_to_mat(self, file):
        f = open(f'./network_mapping/{file}.csv', 'r')
        # grab the size of the array
        array_size = int(f.readline().split(",")[0])
        f.readline()
        # write into matrix
        csv_matrix = np.zeros((array_size, array_size))
        i_counter = -1
        i_tracker = ""
        for line in f:
            split_line = line.split(",")
            if i_tracker != split_line[0]:
                i_tracker = split_line[0]
                i_counter += 1
                j_counter = i_counter + 1
                if i_counter == array_size:
                    continue
            csv_matrix[i_counter][j_counter] = split_line[2]
            csv_matrix[j_counter][i_counter] = split_line[2]
            j_counter += 1
        self.matrix = csv_matrix

    def mat_to_gml(self):
        f = open(f'./network_mapping/Network_{datetime.now().strftime("%d%m%Y_%H%M%S")}.gml', 'a')
        f.write("graph\n[\n")
        for i in range(len(self.word_list)):
            if '-' in self.word_list[i]:
                f.write(f'  node\n  [\n    id {i + 1}\n    label "{self.word_list[i]}"\n  ]\n')
            else:
                f.write(f'  node\n  [\n    id {i + 1}\n    label {self.word_list[i]}\n  ]\n')
        for i in range(len(self.matrix[0]) - 1):
            for j in range(i + 1, len(self.matrix[0])):
                if int(self.matrix[i][j]) != 0:
                    f.write(f'  edge\n  [\n    source {str(i + 1)}\n    target {str(j + 1)}\n    label {str(int(self.matrix[i][j]))}\n  ]\n')
        f.write(']')
        f.close()

    def graph_network(self, file):
        mygraph = nx.read_gml(f'./network_mapping/{file}.gml')
        net = Network(notebook=True)
        net.from_nx(mygraph)
        net.show(f'./network_graphs/Network_{datetime.now().strftime("%d%m%Y_%H%M%S")}.html')
