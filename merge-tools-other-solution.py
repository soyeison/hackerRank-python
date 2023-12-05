def eliminateEquals(substring):
    arr = []
    for l in substring:
        if l not in arr:
            arr.append(l)
    return "".join(arr)

def merge_the_tools(string, k):
    lengthOfSubstrings = len(string) // k
    counter = 0
    inicio = 0
    while counter < lengthOfSubstrings:
        # Logica
        fin = inicio +  k
        print(eliminateEquals(string[inicio:fin]))
        inicio = fin
        counter += 1

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)