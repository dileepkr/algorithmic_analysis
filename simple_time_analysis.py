import time

def sumOfN(N):
    start_time = time.time()
    sum = 0
    for num in range(1, N+1):
        sum += num
    end_time = time.time()
    run_time = start_time - end_time
    return (sum, run_time)

if __name__ == "__main__":
    res = sumOfN(10)
    print(f" Sum: {res[0]}, run_time: {res[1]}")