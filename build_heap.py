# python3


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

    m = len(data)

    for i in range (m// 2, -1,-1):
        j=i
        while True:
            l=j
            if 2 * j + 1 < m and data [2 * j + 1 ] < data[l]:
                l= 2 * j + 1
            if 2*j + 2 < m and data[2*j+2] < data[l]:
                l= 2 * j + 2
            if l==j:
                break
            if l != j:
                data[j], data [l] = data[l], data[j]
                swaps.append((j,l))
                j = l

    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    inputs = input()
    if inputs == "I":

    # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))

        # checks if lenght of data is the same as the said lenght
        assert len(data) == n
        assert len(set(data)) == n

    elif inputs == "F":
        filename = input()
        with open("tests.txt") as file:
            n=int(file.readline())
            data = list(map(int, file.readline().split()))

    # checks if lenght of data is the same as the said lenght
            assert len(data) == n
            assert len(set(data)) == n
    else:
        return

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j, end = " ")


if __name__ == "__main__":
    main()
