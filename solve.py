import sys
from itertools import permutations 
import enchant


if __name__ == "__main__":
    input_string = None
    if len(sys.argv) <= 1:
        print("Need to supply a string.")
        sys.exit(1)
    input_string = sys.argv[1]

    
    d = enchant.Dict("en_US")
    all_permutations = []
    for x in range(3, len(input_string)+1):
        all_permutations += [''.join(p) for p in permutations(input_string, x)]
    print("All permutations")
    for x in sorted(set(all_permutations)):
        # print(x)
        if d.check(x): print(x) 
