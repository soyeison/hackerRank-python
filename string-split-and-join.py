def split_and_join(line):
    arrResps = line.split(" ")
    return "-".join(arrResps)
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)