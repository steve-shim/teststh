from functools import reduce

# reduce(집계 함수, 순회 가능한 데이터[, 초기값])
users = [{'mail': 'gregorythomas@gmail.com', 'name': 'Brett Holland', 'sex': 'M', 'age': 73},
        {'mail': 'hintoncynthia@hotmail.com', 'name': 'Madison Martinez', 'sex': 'F', 'age': 29},
        {'mail': 'wwagner@gmail.com', 'name': 'Michael Jenkins', 'sex': 'M', 'age': 51},
        {'mail': 'daniel79@gmail.com', 'name': 'Karen Rodriguez', 'sex': 'F', 'age': 32},
        {'mail': 'ujackson@gmail.com', 'name': 'Amber Rhodes', 'sex': 'F', 'age': 42}]

# 나이 총합
print(reduce(lambda acc, cur: acc + cur["age"], users, 0))
# 이메일 리스트
print(reduce(lambda acc, cur: acc + [cur["mail"]], users, []))

def names_by_sex(acc, cur):
    sex = cur["sex"]
    if sex not in acc:
        acc[sex] = []
    acc[sex].append(cur["name"])
    # test = {**acc, 'haha':(acc[cur["sex"]] if cur["sex"] in acc else []) + [cur["name"]]}
    # print("test",test)
    return acc

print(reduce(names_by_sex, users, {}))

print(reduce(lambda acc, cur: {**acc, cur["sex"]: (acc[cur["sex"]] if cur["sex"] in acc else []) + [cur["name"]]}, users, {}))