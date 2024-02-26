import math
if __name__ == '__main__':

    AB = int(input())
    BC = int(input())

    h = math.sqrt(AB**2 + BC**2)

    theta = math.acos(BC/h)
    print(round(math.degrees(theta)), chr(176), sep="")