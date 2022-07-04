import argparse
import logging
import multiprocessing
import time
from typing import List

logging.basicConfig(level = logging.INFO)

def parse_args():
    # Parse command line arguments
    parser = argparse.ArgumentParser()

    parser.add_argument("--input", type=str, default="./pro2_in2.txt", help="Input Unsorted File.")
    parser.add_argument("--output", type=str, default="./pro2_out2.txt", help="Output Sorted File.")
    parser.add_argument("--benchmark", dest="benchmark", action="store_true", help="Run multiple times to benchmark the time.")
    parser.add_argument("--addvertices", type=int, default=0, help="How many vertices to add (multiplicatively / additive).")

    args = parser.parse_args()
    return args

def read_matrix(file):
    matrices = []
    for line in file:
        line = line.strip()
        if not line: continue
        matrices.append([row.strip().split(" ") for row in line.split(',')])
    return matrices

def write_matrix(file, matrices):
    file.write('\n'.join([' ,'.join([' '.join(map(str, row)) for row in matrix]) for matrix in matrices]))

def process_matrix(matrix: List[List[str]]) -> List[List[int]]:
    num_rows, num_cols = len(matrix), len(matrix[0])
    dist = [[0] * num_cols for _ in range(num_rows)]
    queue = [(i, j) for i in range(num_rows) for j in range(num_cols) if matrix[i][j] == "o"]
    seen = set(queue)

    # 广度优先搜索
    while queue:
        i, j = queue.pop(0)
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= x < num_rows and 0 <= y < num_cols and (x, y) not in seen:
                dist[x][y] = dist[i][j] + 1
                queue.append((x, y))
                seen.add((x, y))
    return dist

def main(args):
    with open(args.input, 'r') as file:
        matrices = read_matrix(file)

    cpus = multiprocessing.cpu_count() - 1
    logging.info(f"Processing on {cpus} CPU Cores")

    if args.benchmark:
        # Scale by V *= 10 & E *= (10 + 10-1)
        matrices = [matrix * (1 + args.addvertices) for matrix in matrices]

        # Scale by V += X & E += (X + X-1)
        #for matrix in matrices:
            # Take the last row as often as needed to get += X Vertices
        #    for _ in range(1+(args.addvertices//len(matrix[-1]))):
        #        matrix.append(matrix[-1])

    x = time.time()

    # 第一次尝试 （需要下面的bfs函数）
    #for matrix in matrices:
    #    for i in range(len(matrix)):
    #        for j in range(len(matrix[0])):
    #            bfs(matrix, i, j)

    # 第二次尝试
    #new_matrices = []
    #for matrix in matrices:
    #    new_matrices.append(process_matrix(matrix))
    #matrices = new_matrices

    # 第三次尝试
    with multiprocessing.Pool(cpus) as p:
       matrices = p.map(process_matrix, matrices)

    logging.info(f"Took {time.time() - x} to process {len(matrices)} examples.")

    with open(args.output, 'w') as file:
        write_matrix(file, matrices)

if __name__ == '__main__':
    args = parse_args()
    main(args)

 
# 第一次尝试 - But too slow, as we recompute values for each row & col!
"""
def bfs(matrix, i, j):
    queue = [(i,j,0,False)]
    while queue:
        # Take vertex with least steps [DJKISTRA]
        cur_vertex = min(queue, key=lambda vertex: (vertex[-2]))
        queue.remove(cur_vertex)

        i, j, step, is_known = cur_vertex

        # Check objective
        if (matrix[i][j] in ("o", 0,)) or is_known:
            return step

        # Add all valid neighbors [BFS]
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
                # If we already know the distance of a field, do not recompute & mark it as a final endpoint
                if isinstance(matrix[x][y], int):
                    queue.append((x,y,step+matrix[x][y]+1,True))
                else:
                    queue.append((x,y,step+1,False))

    # This should not be reached
    raise ValueError("Input must contain at least one 'o'.")
"""