# python3


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

    m = len(data)

    for i in range (m// 2, -1,-1):
       
            l=j
            if 2 * j + 1 < m and data [2 * j + 1 ] < data[l]:
                l= 2 * j + 1
            if 2*j + 2 < m and data[2*j+2] < data[l]:
                l= 2 * j + 2
            if l==j:
                break
            if l != j:
                swaps.append((j,l))
                data[j], data [l] = data[l], data[j]
                s=l
                p=s

                while 2 * s + 2< m:
                    if data[2*s +2] < data[p]:
                        p = 2 * s + 2
                    if data[2*s 1] < data[p]:
                        p = 2 * s + 1
                    if p != s:
                        swaps.append((s, p))
                        data[s], data [p] = data[p], data[s]
                        s=p
                    else:
                        break
                if 2 * s+1<m and data [2* s + 1] < data[p]:
                    l = 2*s+1
                    swaps.append((s,p))
                    data[s], data [p] = data[p], data[s]

    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    inputs = input()
    if "I" in inputs:

    # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))

        # checks if lenght of data is the same as the said lenght
        assert len(data) == n

    if  "F" in inputs:
        inputs = "tests/"+ input()
        with open(inputs, 'r') as file:
            n=int(file.readline().strip())
            data = list(map(int, file.readline().strip().split()))

    # checks if lenght of data is the same as the said lenght
            assert len(data) == n
    

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    swaps =build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
