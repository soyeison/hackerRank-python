from cmath import phase

if __name__ == '__main__':
    N = complex(input())
    
    # Calculate module
    angle = abs(N)
    
    # Calculate phase
    r = phase(N)

    print(angle)
    print(r)