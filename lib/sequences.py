#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print([0, 1])
    else:
        sequence = [0, 1]
        while len(sequence) < length:
            next_num = sequence[-1] + sequence[-2]
            sequence.append(next_num)
        print(sequence)
    
print(print_fibonacci(10))
# output [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]