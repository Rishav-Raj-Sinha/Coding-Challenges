import argparse
import os
#creating path positional argument
parser = argparse.ArgumentParser()
parser.add_argument("path")

#creating optional arguments

parser.add_argument("-c","--count",action="store_true")
parser.add_argument("-l","--lines",action="store_true")
parser.add_argument("-w","--words",action="store_true")
parser.add_argument("-m","--characters",action="store_true")
args = parser.parse_args()

if args.count:
    f = args.path
    f_size = os.path.getsize(f)
    print(f"{f_size} {args.path}")
elif args.lines:
    count = 0
    with open(args.path, 'r',encoding='utf-8') as f:
        for line in f:
            count+=1
    print(f"{count} {args.path}")
elif args.words:
    word_count = 0
    with open(args.path, 'r', encoding='utf-8') as f:
        for line in f:
            words = line.split()  # Split line into words
            word_count += len(words)
    print(f"{word_count} {args.path}")
elif args.characters:
    char_count = 0
    with open(args.path, 'r', encoding='utf-8') as f:
        for line in f:
            char_count += len(line)
        print(f"{char_count} {args.path}")
