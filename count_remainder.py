#!/usr/loacl/bin/python3

'''
Count the number of collisions (if the hash function is x % N)
And print 10 most common collisions.
'''
def main():
    import sys, collections
    '''
    try:
        sys.stdin = open('input.txt', 'r')
    except FileNotFoundError:
        print("Cannot open input.txt")
        exit(1)
    '''
    N = int(input())
    remainders = map(lambda x: int(x) % N, input().split())
    remainder_stat = collections.Counter(remainders)
    print(remainder_stat.most_common(10))

if __name__ == '__main__':
    main()
