from collections import Counter

if __name__ == '__main__':
    K = int(input())
    groups = input().split()

    groups = Counter(groups)
    captain = [k for k, v in groups.items() if v == 1][0]
    print(captain)