import time

# 1이 될때까지 반복
# 어떤 수 N이 1이 될떄까지 아래와 같이 2개중 하나를 반복적으로 선택해 수행하려 한다.
# 1. N - 1,
# 2. N / K (조건 - N이 K로 나누어 0이 될때만 연산하기)
# ex) N = 17 / K = 4일때 2번 조건이 되지 않으므로 1번 먼저 하고 16 % 4 = 0이기에 나누기 연산
# 위처럼 연산을 반복하여 N이 결국 1로 되어지는 최소한의 횟수를 구하기
# 입력조건  1 <= N <= 100,000 / 2 <= K <= 100,000

start_time = time.time()

n = 100000
k = 144
count = 0
while True:
    if n == 1:
        break
    elif n % k == 0:
        n //= k
        count = count + 1
    else:
        n = n - 1
        count = count + 1


end_time = time.time()

print(count) #6분
print("%f초 걸렸습니다." % (end_time - start_time))