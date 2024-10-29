import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square",type = int) #here square is positional argument,the first position argument ,we also defined the data-type it can accept
args = parser.parse_args() #parses and finds any value that is given for the positional argument "square" if there is then it stores it in args
print(args.square*args.square) # we get the value for positional argument by the help of args.square, if there was say another argument "root", then we could get it's value by writing args.root

# let's define some optional arguments now
