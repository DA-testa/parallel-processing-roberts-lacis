# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    threads = []
    for a in range(n):
        threads.append([0,0])
    i = 0
    while i < len(data):
        for a in range(n):
            if threads[a][0] == 0:
                threads[a][0] = data[i]
                threads[a][1] += data[i]
                output.append([a,threads[a][1]])
                i += 1
        for a in range(n):
            if threads[a][0] != 0:
                threads[a][0] -= 1

        

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    a = list(map(int, input().split()))
    n = a[0]
    m = a[1]

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int,input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for i,j in result:
        print(i,j)



if __name__ == "__main__":
    main()
