from argparse import ArgumentParser

parser = ArgumentParser(description='This is going to be used to specify which specific sequence type tests to run')

parser.add_argument('--seq_type', default='array', choices=['array', 'deque'])
args = parser.parse_args()
seq_type = args.seq_type



if __name__=='__main__':
    pass
