from itertools import combinations_with_replacement

if __name__ == '__main__':
    params = input().split()
    combinations = list(combinations_with_replacement(sorted(params[0]), int(params[1])))
    combinationsSorted = sorted(combinations)

    for i in combinationsSorted:
        print(''.join(i))