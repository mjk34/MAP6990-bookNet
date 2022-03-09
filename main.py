import sys, time

from importlib.resources import read_binary
from markov import Markov

def mean_degree(matrix):
    somme = 0
    for i in range(len(matrix[0])):
        for j in range(len(matrix[0])):
            somme += matrix[i][j]
    return somme/len(matrix[0])

def main (argv):
    markov = Markov()

    start = time.time()
    with open(f'./training_txt/{argv[0]}.txt', 'rb') as f:
        holmes_content = f.read()
    matrix = markov.create_mat(holmes_content)
    
    end = time.time()
    print('\nElapsed Time: %.3fs' % float(end-start))

    print(f'\nMean degree: {mean_degree(matrix)}')

    print('\nElapsed Time: %.3fs' % float(time.time() - end))

    return




if __name__ == '__main__':
    main(sys.argv[1:])