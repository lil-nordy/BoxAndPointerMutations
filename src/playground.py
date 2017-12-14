import rosegraphics as rg

def main():
    # point = rg.Point(300, 300)
    # point = point
    # point2 = point2
    # for k in range(10):
    #     point2 = point2
    #     print(point2)

    string1 = 'hello'
    string2 = 'hello'
    print("for strings: \n", string1 is string2, string1 == string2)

    int1 = 5
    int2 = 5
    print('for integers: \n', int1 is int2, int1 == int2)
main()