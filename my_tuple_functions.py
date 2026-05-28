T1 = (1,3,2,4)

def length (T1):
    return len(T1)

def concat (T1, T2):
    return T1 + T2

def index (idx):
    return T1.index(idx)

def count (cnt):
    return T1.count(cnt)

if __name__ == '__main__':

    print(length(T1))

    T2 = (5,6)

    print(concat(T1,T2))

    print(count(2))

    print(index(3))
