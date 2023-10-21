class NumberLists:
    def __init__(self, list_1: list[int | float], list_2: list[int | float]):
        self.list_1 = list_1
        self.list_2 = list_2

    def get_average_values(self) -> tuple[float, float]:
        average_1 = 0
        if self.list_1:
            average_1 = sum(self.list_1) / len(self.list_1)

        average_2 = 0
        if self.list_2:
            average_2 = sum(self.list_2) / len(self.list_2)

        return average_1, average_2

    def compare_averages(self) -> None:
        average_1, average_2 = self.get_average_values()
        if average_1 > average_2:
            print('Первый список имеет большее среднее значение')
        elif average_1 < average_2:
            print('Второй список имеет большее среднее значение')
        else:
            print('Средние значения равны')
