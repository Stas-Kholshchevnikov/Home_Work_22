# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def move(self, direction):
        speed = self._get_speed()
        if direction == "up":
            self.field.set_unit(x=self.x, y=self.y + speed, unit=self)
        if direction == "down":
            self.field.set_unit(x=self.x, y=self.y - speed, unit=self)
        if direction == "left":
            self.field.set_unit(x=self.x - speed, y=self.y, unit=self)
        if direction == "right":
            self.field.set_unit(x=self.x + speed, y=self.y, unit=self)

    def _get_speed(self):
        if self.status == "fly":
            return self.speed * 1.2
        elif self.status == "crawl":
            return self.speed * 0.5
        else:
            raise Exception

#     ...
