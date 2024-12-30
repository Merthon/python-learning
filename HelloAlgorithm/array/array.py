import random

def random_access(arr):
    """
    Random access to an array.
    """
    n = len(arr)
    for i in range(n):
        j = random.randint(0, n-1)
        arr[j] = i
    return arr

if __name__ == '__main__':
    arr = [0] * 10
    print(random_access(arr))   

