# list []
# 여러 데이터를 동시 저장 가능한 자료구조, 대괄호 [] 사용하며 0개 이상 원소 저장
# 인덱스로 특정 요소에 접근 가능 -> (for문을 이용해 데이터 추출 가능)
# 데이터 변경이 가능한 mutable 한 리스트
# 대괄호 안에 : 으로 시작, 끝 인덱스를 설정 가능
# 끝 인덱스는 실제 인덱스보다 1을 크게 더 설정
# list는 딕셔너리의 key값(해쉬)으로 쓸 수 없지만 tuple은 가능 (딕셔너리의 키값은 불변한 값만 올 수 있기 때문)

#리스트 초기화
list1 = [1, 2, 3, 'sdf', ['a', 'b', True]]
list2 = [0, 5]

# [:] -> 전체, [0:] -> 0부터 끝까지, [:4] 4개 count까지
print("리스트 인덱싱 출력", list1[:-1])

# 크기가 n이고, 모든 값이 1인 1차원 리스트 초기화
n = 5
exam_list = [1] * n
print(exam_list)

# list와 tuple의 차이 -> immutable(변), mutable(불변), 속도 : list < tuple

# dic {}
# 중괄호를 사용 {}
# 자바의 map과 유사한 자료형으로 key : value 1:1 대응 형태의 자료구조
# 하나의 키값엔 하나의 value만 대응, key값은 변경이 불가하지만, value는 변경이 가능
dic = {'name': 'lion', 'age': 1}
dic2 = dict(name='lion', age=1)

dic['sex'] = 'male'  # 추가
# print(dic.get('name'))
del dic['name']
dic.clear()
# print(dic2.get('name'))  # 'lion'
# print('name' in dic2)  # True

# tuple
# 여러 데이터를 동시 저장 가능한 자료구조, 소괄호() 사용하며 0개 이상 원소 저장
# 인덱스로 특정 요소에 접근 가능 -> (for문을 이용해 데이터 추출 가능)
# 데이터 변경이 불가능한 immutable 한 리스트 (# TypeError: 'tuple' object does not support item assignment)

tuple1 = (1, "tuple_study")
tuple2 = (3, 4.22)
tuple3 = tuple1 + tuple2
tuple4 = tuple1 * 5

tt = ('a',)+(1231923,) + tuple1[1:]
print(tt)

print(tuple1)
# # tuple1[0] = 2 에러 변경 불가
# print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)


# 리스트 slice, remove(인자와 같은 첫번째 데이터를 찾아서 제거) del, pop(인자로 받은 인덱스 데이터를 제거)
a = [1, 2, 1, 3, 4, 5, 1]
b = [1, 2, 1, 3, 4, 5, 1]

a.remove(1)
# pop : 지워진 인덱스의 데이터값을 변수로 반환하지만, del은 반환하지 않음 -> del이 pop보다 수행속도가 미세하게 빠름
removed = b.pop(1)
print("remove a : ", a)

print("removed : ", removed)
print("pop b : ", b)
