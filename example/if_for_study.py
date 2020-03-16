a = 23
b = 45

if a >= b:
    print("더 큰 수는 ", a)
elif a <= b:
    print("더 큰 수는 ", b)

# and, or
c = 33
if a < b and c > b:
    print("and 조건 성립")

i = 1
# while i < 10:
#     i = i + 1
#     if (i % 2 == 0):
#         print("짝수 -> ", i)


cars = {'porsche':'911', 'benz':'e class', 'ford':'mustang', 'ferrari':'f8'}


for key, value in cars.items():
    print('{} 브랜드의 모델명은 : {}'.format(key, value))


for i in range(2,10):
    print("{gugudan}단 ".format(gugudan=i))
    for j in range(1,10):
        print("{} * {} = {}".format(i,j,i*j))


