import sys
args = sys.argv[1:]
args.reverse()
print(''.join(reversed(sys.argv[1:])))
