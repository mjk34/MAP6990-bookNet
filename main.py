import sys, time

from importlib.resources import read_binary
from markov import Markov

def main (argv):
    markov = Markov()

    start = time.time()
    with open(f'./training_txt/{argv[0]}.txt', 'rb') as f:
        holmes_content = f.read()
    markov.create_map(holmes_content)
    
    end = time.time()
    print('\nElapsed Time: %.3fs' % float(end-start))
    
    return

if __name__ == '__main__':
    main(sys.argv[1:])