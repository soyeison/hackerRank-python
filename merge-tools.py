def merge_the_tools(string, k):
    lengthOfSubstrings = len(string) // k
    inicio = 0
    for i in range(0, lengthOfSubstrings):
        fin = inicio + k
        substring = set(string[inicio:fin])
        print(''.join(substring))
        inicio = fin

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)