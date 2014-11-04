#!/usr/local/bin/python3

'''
Generate 1000 random numbers ranging from 0 to 9999
and sort them, store them in input.txt
Then hash them into the hash table in gen_hash.py
store the hash result in output.txt
'''
def main():
    import sys
    from gen_hash import HashTable
    from random import sample
    rand_list = sorted(sample(range(10000), 1000))
    ''' write generated random list '''
    '''
    try:
        sys.stdout = open('input.txt', 'w')
    except FileNotFoundError:
        print('Cannot open input.txt')
        exit(1)
    '''
    print(1000)
    for i in rand_list:
        print(i, end=' ')
    H = HashTable(1000)
    H.hash_seq(rand_list)
    ''' write hashed list'''
    '''
    try:
        sys.stdout = open('output.txt', 'w')
    except FileNotFoundError:
        print('Cannot open output.txt')
        exit(1)
    '''
    for i in H.hash_table:
        if i == None:
            print(-1, end=' ')
        else:
            print(i, end=' ')

if __name__ == '__main__':
    main()
