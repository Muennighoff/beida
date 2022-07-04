import argparse
import random
import time

def parse_args():
    # Parse command line arguments
    parser = argparse.ArgumentParser()

    parser.add_argument("--input", type=str, default="./pro2_in1.txt", help="Input Unsorted File.")
    parser.add_argument("--output", type=str, default="./pro2_out1.txt", help="Output Sorted File.")

    args = parser.parse_args()
    return args

def read_input(filename):
    """
    读入数据
    """
    data = []
    with open(filename, 'r') as f:
        for line in f:
            data.append(list(map(int, line.strip()[1:-1].split(','))))
    return data

def write_output(filename, data):
    """
    输出数据
    """
    with open(filename, 'w') as f:
        for line in data:
            f.write(f"[{','.join(map(str, line))}]\n")

def quicksort(A):
    if len(A) <= 1:
        return A
    L, R = [], []
    pivot_idx = random.choice(range(len(A))) 
    pivot_val = A[pivot_idx]
    for i in range(len(A)):
        if i == pivot_idx:
            continue
        if A[i] < pivot_val:
            L.append(A[i])
        else:
            R.append(A[i])
    return quicksort(L) + [pivot_val] + quicksort(R)

def square_sort_A(data): # 1.1919701099395752
    """
    对数组每个数字求平方，然后排序
    """
    return quicksort(list(map(lambda x: x ** 2, data)))

def square_sort_B(data): # 1.3256316184997559
    """
    对数组每个数字求平方，然后排序
    """
    return list(map(lambda x: x**2, quicksort(list(map(lambda x: abs(x), data)))))

def square_sort_C(data): # 0.2832770347595215
    """
    对数组每个数字求平方，然后排序
    """
    return sorted(list(map(lambda x: x ** 2, data)))

if __name__ == '__main__':
    x = time.time()
    args = parse_args()
    data = read_input(args.input)
    result = list(map(square_sort_A, data))
    write_output(args.output, result)
    print("Took: ", time.time() - x)