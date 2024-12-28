def read_input():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    first_line = data[0].strip().split()
    t = int(first_line[0])
    p = int(first_line[1])

    results = []
    for i in range(1, t + 1):
        results.append(data[i].strip().split())

    return t, p, results


def analyze_results(t, p, results):
    matrix = [[1 if results[i][j] == '+' else 0 for j in range(p)] for i in range(t)]

    print("Результаты в бинарном виде:")
    for row in matrix:
        print(row)

    solved_counts = [sum(row) for row in matrix]

    print("\nКоличество решенных задач для каждой команды:")
    for i in range(t):
        print(f"Команда {i + 1}: {solved_counts[i]} задач(и) решено.")


def main():
    t, p, results = read_input()
    analyze_results(t, p, results)


# Запуск программы при старте
if __name__ == "__main__":
    main()
