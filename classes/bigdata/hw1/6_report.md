## Project 报告 - 孟念


### Project 1


#### 第一部分


I benchmarked three sorting functions according to the seconds they take for pro2_in1.txt:
- My quicksort implementation - 1.1919701099395752
- My quicksort implementation with squaring done after the sorting - 1.3256316184997559
- Python's built-in sorted function - 0.2832770347595215

Pythons built-in sorted function, which uses the Timsort algorithm written in C is 4x faster than my python quicksort function.
Squaring after the sorting did not improve the speed. My hypothesis was that maybe its faster sorting smaller strictly positive numbers.


#### 第二部分


I created a simple GUI consisting of three parts:
- Input Box
- Button
- Output Box

When the user inputs a valid array into the input box and hits the button, the same quicksort function from 第一部分 is used.
If the array is invalid, an error message appears, showing the user a valid example.


### Project 2

**思路**

我从实现BFS开始，然后只是将其应用于数组中的每个元素。这就构成了 "第一次尝试"。
然后我发现我在几次计算同样的距离，所以我重新实现了这个函数，只对所有非零元素执行BFS。这就是 "第二次尝试"。
然后，我增加了多处理功能，以并行计算多个解决方案 - "第三次尝试"。

**结果和复杂度**

|                                      | 第一次尝试                            | 第二次尝试                    | 第三次尝试 |
| -----------                          | ------------------------------------ |-------------------------------| ---------|
| 说明                                 | 使用一个loop对每个元素进行宽度优先搜索。 | 同时对整个矩阵进行宽度优先搜索。| 加多重处理 |
| 复杂度*                               | O(V * (V + E)) (loop * BFS)          | O(V + E)                     | O(V + E) / num_cpus |
|||||
| 速度 - Sample（V; E)                | 0.0019965171813964844                 | 0.0009996891021728516        | 0.2869374752044678 | 
| 速度 - Sample（V*2; ~E*2)           | 1.7716591358184814                     | 0.000957489013671875         | 0.2909998893737793 | 
| 速度 - Sample（V*5; ~E*5)           | 306.440710067749                      | 0.001986265182495117         | 0.30095577239990234 | 
| 速度 - Sample（V*10; ~E*10)         | N/A                                   | 0.003041982650756836         | 0.2840578556060791 | 
| 速度 - Sample（V*100; ~E*100)       | N/A                                   | 0.05306434631347656       | 0.30097341537475586 | 
| 速度 - Sample（V*1000; ~E*1000)     | N/A                                   | 3.505746841430664         | 2.302999258041382 | 
| 速度 - Sample（V*10000; ~E*10000)   | N/A                                   | N/A                       | 173.58572268486023 | 
|||||
| 速度 - pro2_in2.txt （V; E)           | N/A                                   | 11.085063695907593           | 3.3065407276153564 |
| 速度 - pro2_in2.txt（V*2; ~E*2)     | N/A                                   | 41.546650648117065           | 10.69340991973877 |


*假设V是每个元组(Vertex), Edge是每个边缘(Edge)


The first try scales with V**2 in respect to each new Vertex V. This is extremely bad and hence it is not good enough for long arrays.

The second try is much better and scales a bit more than linearly with the input size. For pro2_in2.txt it takes about 3.5x as long when 2x the amount of vertices, which is close to O(V+E). The edges actually scale with a bit more than 2x and the exact amount it needs to search may vary.

The third try scales similarly to the second, but roughly divided by the number of CPUs. For small inputs, such as the Sample, there is too much overhead involved in spinning up multiple processes, so it is slower than the other approaches. As the number of vertices increases though, it gets more useful and is ~4 times faster than the 2nd approach on the last task. (I used 7 CPUs, so it should increase up to almost 7x faster if we further scale up).


The experiments can be rerun by using e.g.
```
# Run 第三次尝试 pro2_in2.txt（V; ~E)
python run3.py --benchmark --addvertices 0
# Run 第三次尝试 pro2_in2.txt（V*2; ~E*2)
python run3.py --benchmark --addvertices 1
```

For the other ones, some part of the code needs to be uncommented.