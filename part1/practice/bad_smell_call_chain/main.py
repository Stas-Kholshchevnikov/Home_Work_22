# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Person:
    def __init__(self, person_room, city_population):
        self.__person_room = person_room
        self.__city_population = city_population

    def get_person_room(self):
        return self.__person_room

    def get_city_population(self):
        return self.__city_population


# TODO после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.