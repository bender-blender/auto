from director import Director



def client_code(name:str):
    director = Director()
    car = director.add_car("5,2-литровый 10-цилиндровый бензиновый атмосферный двигатель","Оранжевый","преселективная 7-ступ","Нитро")
    car.name = name
    print(f"Название:{name}")
    print(car)
    
client_code("Lamborgini Uracan")
