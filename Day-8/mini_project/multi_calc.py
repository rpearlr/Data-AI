import multiprocessing as mp

def calculate(task):
    op, a, b = task

    if op == "add":
        return a + b
    elif op == "sub":
        return a - b
    elif op == "mul":
        return a * b
    elif op == "div":
        return a / b
    elif op == "pow":
        return pow(a, b)
    else:
        return "Invalid operation"


def parallel_calculator(tasks):
    with mp.Pool(mp.cpu_count()) as pool:
        results = pool.map(calculate, tasks)
    return results

if __name__ == "__main__":
    print("Large Number Parallel Calculator")
    print("Operations: add, sub, mul, div, pow")

    tasks = []

    n = int(input("How many calculations? "))

    for _ in range(n):
        op = input("Operation: ")
        a = int(input("First number: "))
        b = int(input("Second number: "))
        tasks.append((op, a, b))

    results = parallel_calculator(tasks)

    print("\nResults:")
    for r in results:
        print(r)
