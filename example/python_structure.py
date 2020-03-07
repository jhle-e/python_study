# tuple
# 여러 데이터를 동시 저장 가능한 자료구조, 소괄호() 사용하며 0개 이상 원소 저장
# 인덱스로 특정 요소에 접근 가능 -> (for문을 이용해 데이터 추출 가능)
# 데이터 변경이 불가능한 immutable 한 리스트 (# TypeError: 'tuple' object does not support item assignment)

tuple1 = (1, "tuple_study")
tuple2 = (3, 4.22)
tuple3 = tuple1 + tuple2
tuple4 = tuple1 * 5

# print(tuple1)
# print(tuple2)
# print(tuple3)
# print(tuple4)

# list
# 여러 데이터를 동시 저장 가능한 자료구조, 대괄호 [] 사용하며 0개 이상 원소 저장
# 인덱스로 특정 요소에 접근 가능 -> (for문을 이용해 데이터 추출 가능)
# 데이터 변경이 가능한 mutable 한 리스트
# list는 딕셔너리의 key값(해쉬)으로 쓸 수 없지만 tuple은 가능 (딕셔너리의 키값은 불변한 값만 올 수 있기 때문)

# list와 tuple의 차이 -> immutable, mutable, 속도 : list < tuple

# dic
# 중괄호를 사용 {}
# 자바의 map과 유사한 자료형으로 key : value 1:1 대응 형태의 자료구조
# 하나의 키값엔 하나의 value만 대응, key값은 변경이 불가하지만, value는 변경이 가능

dic = {1: "my", 2: "name", 3: "is", 4: "python"}

print(dic.keys()) # 1,2,3,4

print(1 in dic.keys()) # true

print(dic.values()) #[my, name, is, python]

print(dic.items()) #[(key, value)]