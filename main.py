class Car :
    def __init__ (self, brand, model):
        self.brand = brand
        self.model = model
        self.__fule =0

    def refuel(self , litres):
        if litres > 0:
            self.__fule += litres
            print (f"Добавить топливо: {litres}")
        else:
            print("Количество топлива должно быть больше 0")
    def drive (self ,km):
        fuel_needed = km * 0.1

        if km <= 0:
            print ("Ростояние должно быть больше 0")
        elif self.__fuel >= fuel_needed:
            self.__fuel -= fuel_needed
            print (f"Машина проехала {km} км")
        else:
            print(f"Недостаточно топливо!")
    def into(self):
        return f"{self.brand} {self.model} {self.__fule} л"
     #два объкта
    car1 = Car("Nexia 3")
    car2 = Car ("Cobalt")
    #проверка первой автомибиль
    car1.refuel(12)
    car1.drive(50)
    print(car.into())

    print ("---------")
    # проверка второй автомобиль
    car2.refuel(20)
    car2.drive(100)
    print(car.into())
    car2.drive(150)