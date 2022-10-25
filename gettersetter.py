class Car:
    """
    Car Class
    """

    __count = 0

    def __init__(self, name, age):
        self.__name = name  # 클래스 인스턴스 내부에서만 접근이 가능한 변수
        self.__age = age
        Car.__count += 1

    @property
    def get_name(self):
        return f"Hyundai {self.__name}"

    @property
    def get_age(self):
        return self.__age

    @get_age.setter
    def set_age(self, new_age):
        if new_age < 0:
            raise ValueError("Invalid age")
        else:
            self.__age = new_age


my_car = Car("Nyyang", 10)
# 클래스로부터 인스턴스를 생성한 이후, 클래스 인스턴스 내부에서 데이터를 안전하게 접근하기 위해서는 
# Getter, Setter을 사용하는게 OOP에서 관례이다.

#print(my_car.age)   # AttributeError: 'Car' object has no attribute 'age'

print(my_car.get_name)
print(my_car.get_age)
# my_car.set_age = -20  # ValueError: Invalid age
my_car.set_age = 20
print(my_car.get_age)