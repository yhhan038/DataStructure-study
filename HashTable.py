
# hash : 임의 값을 고정 길이로 변환하는 것


def hash_func(key):  # hashing function : key에 대한 산술 연산을 이용해 데이터 위치를 찾을 수 있는 함수
    return key % 5

def storage_data(data, value):
    key = ord(data[0])  #
    hash_address = hash_func(key)  # key를 해싱 함수로 연산해서 해쉬 값을 알아내고, 이를 기반으로
    # 해쉬테이블에서 해당 key에 대한 데이터 위치를 일관성 있게 찾을 수 있음
    hash_table[hash_address] = value


def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]


hash_table = list([0 for i in range(10)])  # hash table : 키 값의 연산에 의해 직접 접근이 가능한 데이터구조


data1 = 'Andy'
data2 = 'Dave'
data3 = 'Trump'

# ord() : 문자의 ASCII 코드를 리턴
print(ord(data1[0]), ord(data2[0]), ord(data3[0]))
print(hash_func(ord(data1[0])), hash_func(ord(data2[0])), hash_func(ord(data3[0])))
