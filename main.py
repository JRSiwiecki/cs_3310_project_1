from utilities.utils import generate_random_matrices, print_matrix, time_algorithm
from algorithms.classical_matrix_multiplication import classical_matrix_multiplication
from algorithms.divide_and_conquer_matrix_multiplication import divide_and_conquer_matrix_multiplication
from algorithms.strassen_matrix_multiplication import strassen_matrix_multiplication

# matrix_size =  n * n size of a given matrix
# min_value = minimum number for values inside a given matrix
# max_value = maximum number for values inside a given matrix
dataset = [
    {"matrix_size": 2, "min_value": 0, "max_value": 5},
    {"matrix_size": 4, "min_value": 0, "max_value": 5},
    {"matrix_size": 8, "min_value": 0, "max_value": 5},
    {"matrix_size": 16, "min_value": 0, "max_value": 5},
    {"matrix_size": 32, "min_value": 0, "max_value": 5},
    {"matrix_size": 64, "min_value": 0, "max_value": 5},
    {"matrix_size": 128, "min_value": 0, "max_value": 5},
    {"matrix_size": 256, "min_value": 0, "max_value": 5},
    {"matrix_size": 512, "min_value": 0, "max_value": 5},
    {"matrix_size": 1024, "min_value": 0, "max_value": 5},
]

# total number of times to run each test case
iterations = 5
current_iteration_count = 1
display_output = False

dataset_results = []

# run each test case multiple times to get an average time
for set in dataset:
    matrix_size = set["matrix_size"]
    min_value = set["min_value"]
    max_value = set["max_value"]

    a, b = generate_random_matrices(matrix_size, [min_value, max_value])

    if display_output:
        print("MATRIX A: ")
        print_matrix(a)
        print("MATRIX B: ")
        print_matrix(b)
    
    print(f"Test Case #{current_iteration_count}: Matrix Size ~ {matrix_size}, Minimum Value ~ {min_value}, Maximum Value ~ {max_value}\n")

    algorithms = [classical_matrix_multiplication, 
              divide_and_conquer_matrix_multiplication, 
              strassen_matrix_multiplication]

    set_results = {"matrix_size": matrix_size, "min_value": min_value, "max_value": max_value, "results": []}

    # test each algorithm for each test case
    for algorithm in algorithms:
        print(f"----- {algorithm.__name__.upper()} -----")
        execution_times = []

        for _ in range(iterations):
            result, execution_time = time_algorithm(algorithm, a, b)
            execution_times.append(execution_time)
            
            if display_output:
                print("RESULT: ")
                print_matrix(result)
            
        avg_execution_time = sum(execution_times) / iterations
        set_results["results"].append({"algorithm": algorithm.__name__, "avg_execution_time": avg_execution_time})
        print(f"Average Execution Time: {avg_execution_time:.6f} seconds")
        print("-------------------------------------------\n")
    
    dataset_results.append(set_results)
    current_iteration_count += 1