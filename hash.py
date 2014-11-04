def linear_probing(collision_num):
    return 1

class HashTable(object):
    def __init__(self, table_size, hash_func, probe=linear_probing):
        self.table_size = table_size
        self.hash_table = [None for i in range(self.table_size)]
        self.hash_func = hash_func
        self.probe = probe

    def insert(self, elem):
        collision_num = 0
        hash_value = self.hash_func(elem)
        current_index = hash_value
        while self.hash_table[current_index] != None:
            if self.hash_table[current_index] == elem: # already exist
                pass
            else:
                collision_num += 1
            current_index += self.probe(collision_num)
            while current_index >= self.table_size:
                current_index -= self.table_size
            if current_index == hash_value: # there's a infinite loop
                print('Infinite loop while inserting {}'.format(elem))
                exit(1)
        else:
            self.hash_table[current_index] = elem # successfully inserted

def main():
    import sys
    try:
        sys.stdin = open('input.txt', 'r')
    except FileNotFoundError:
        print('Cannot open input.txt')
        exit(1)
    N = int(input())
    inputs = map(int, input().split())
    H = HashTable(N, lambda x: x % N)
    for i in inputs:
        H.insert(i)
    for i in range(N):
        print('{} '.format(H.hash_table[i]), end='')
    print()

if __name__ == '__main__':
    main()
