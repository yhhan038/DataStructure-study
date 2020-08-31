# Linear Probing 기법
hash_table = list([0 for i in range(10)])


def get_key(data):
    return hash(data)


def hash_func(key):
    return key % 8


def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_func(index_key)

    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                hash_table[index] = [index_key, value]
                return
            elif hash_table[index][0] == index_key:  # 데이터를 업데이트
                hash_table[index][1] = value
                return
    else:
        hash_table[hash_address] = [index_key, value]


def read_data(data):
    index_key = get_key(data)
    hash_address = hash_func(index_key)

    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                return None
            elif hash_table[index] == index_key:
                return hash_table[index][1]
    else:
        return None