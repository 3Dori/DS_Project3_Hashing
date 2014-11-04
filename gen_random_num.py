def main():
    import sys
    from gen_hash import HashTable
    from random import sample
    rand_list = sample(range(5000), 1000)
    ''' write generated random list into input.txt '''
    try:
        sys.stdout = open('input.txt', 'w')
    except FileNotFoundError:
        print('Cannot open input.txt')
        exit(1)
    print(1000)
    for i in rand_list:
        print(i, end=' ')
    H = HashTable(1000)
    H.hash_seq(rand_list)
    ''' write hashed list into output.txt '''
    try:
        sys.stdout = open('output.txt', 'w')
    except FileNotFoundError:
        print('Cannot open output.txt')
        exit(1)
    for i in H.hash_table:
        if i == None:
            print(-1, end=' ')
        else:
            print(i, end=' ')

if __name__ == '__main__':
    main()
