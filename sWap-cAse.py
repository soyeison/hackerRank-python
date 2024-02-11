def swap_case(s):
    for i, e in enumerate(s):
        if e.isalpha():
            if e.isupper():
                s = s[:i] + e.lower() + s[i + 1:]
            else:
                s = s[:i] + e.upper() + s[i + 1:]
    return s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)