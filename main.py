import sys, time

#from importlib.resources import read_binary
from markov import Markov
from undirectedWeightedNetwork import uwn

def main (argv):
    markov = Markov()

    start = time.time()
    with open(f'./training_txt/{argv[0]}.txt', 'rb') as f:
        holmes_content = f.read()
    my_network = uwn(markov.create_mat(holmes_content), markov.get_word_list())

    end = time.time()
    print('\nElapsed Time: %.3fs' % float(end-start))

    print(f'\nMean degree: {my_network.mean_degree()}')

    second_end = time.time()
    print('\nElapsed Time: %.3fs' % float(second_end - end))

    #my_network.mat_to_csv()
    #my_network.mat_to_gml()

    third_end = time.time()
    print('\nElapsed Time: %.3fs' % float(third_end - end))

    #matrix_from_markov = my_network.matrix
    #my_network.csv_to_mat("Network_09032022_192153")
    #matrix_from_csv = my_network.matrix
    #match_check = True
    #for z in range(len(matrix_from_markov[0])):
    #    for zz in range(len(matrix_from_markov[0])):
    #        if matrix_from_markov[z][zz] != matrix_from_csv[z][zz]:
    #            match_check = False
    #if match_check is True:
    #    print("\nMatrices match!")
    #else:
    #    print("\nMatrices don't match :(")

    #fourth_end = time.time()
    #print('\nElapsed Time: %.3fs' % float(fourth_end - end))

    #my_network.mat_to_gml()

    my_network.graph_network("Network_09032022_201028")

    return

if __name__ == '__main__':
    main(sys.argv[1:])