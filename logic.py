import random
from exceptions import *


symbols = [i for i in range(10)]
difficult = 4
unique_elements = True




def make_code(symbols, difficult):
    rnd = random.Random()
    # rnd.seed(0)
    s = symbols.copy()
    res = []
    for i in range(1, int(difficult) + 1):
        sym =rnd.choice(s)
        res.append(sym)
        s.remove(sym)
    
    # return rnd.choices(symbols, k=difficult)
    return res


def check(code, try_code):
    tc = [int(i) for i in try_code]
    black = 0
    white = 0    
    for i,j in zip(code, tc):
        if i == j:
            black += 1
        elif j in code:
            white += 1
    
    return black, white


def check_rules(try_code, difficult):
    if len(try_code) != difficult:
        raise LengthError
    if len(try_code) != len(set(try_code)):
        raise UniqueError

    

def main():
    code = make_code(symbols, difficult)
    print('Try to guess secret code for the minimum attempts')
    attempts = 0
    while True:
        print(f'Input {difficult} numbers:')
        inp = input()
        try:
            try_code = [int(i) for i in inp]
        except ValueError as e:
            print('some symbols not numbers')
            continue
        
        if check_rules(try_code):
            continue

        b,w = check(code, try_code)
        
        print(f'bulls: {b}, cows: {w}')
        attempts += 1
        
        if code == try_code:
            print('Attempts: ', attempts)
            break
        

if __name__=='__main__':
    main()

    
    
    

