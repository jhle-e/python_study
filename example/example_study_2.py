# 리스트
list1 = [1, 2, 3, 'sdf', ['a', 'b', True]]
list2 = [0, 5]

# print(list1[2:3])  # [3, 'sdf']

# 딕셔너리
dic = {'name': 'lion', 'age': 1}
dic2 = dict(name='lion', age=1)

dic['sex'] = 'male'  # 추가
# print(dic.get('name'))
del dic['name']
dic.clear()
# print(dic2.get('name'))  # 'lion'
# print('name' in dic2)  # True


# 리스트 slice, remove(인자와 같은 데이터를 찾아서 제거) del, pop(인자로 받은 인덱스 데이터를 제거)
a = [1, 2, 1, 3, 4, 5, 1]
b = [1, 2, 1, 3, 4, 5, 1]

a.remove(1)
# pop : 지워진 인덱스의 데이터값을 변수로 반환하지만, del은 반환하지 않음 -> del이 pop보다 수행속도가 미세하게 빠름
removed = b.pop(1)
print("remove a : ", a)

print("removed : ", removed)
print("pop b : ", b)