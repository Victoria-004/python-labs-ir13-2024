class Stadium:
    total_viewership = 0

    def __init__(self, viewership = 32100, name = "Стадіон", lightning = "1200 ЛЮКСІВ", event = "футбол", area = 150):
        """
        Задання значень полів
        """
        self.__viewership = viewership
        self.__name = name
        self.__lightning = lightning
        self.event = event
        self.area = area

        Stadium.total_viewership += viewership

    def __str__(self):
        """
        Метод представлення рядків, повертає зручне представлення для користувача
        """
        return f"Stadium(viewership:{self.viewership}, name:{self.name}, lightning:{self.lightning}, event:{self.event}, area:{self.area})"

    def __repr__(self):
        """
         Метод, який повертає предсталвення рядка, зручне для розробників
        """
        return f"Stadium('{self.viewership}', '{self.name}', '{self.lightning}', '{self.event}', '{self.area}')"

    def set_data(self, viewership, name, lightning):
        """
        Встановлення значень
        """
        Stadium.total_viewership -= self.__viewership
        self.name = name
        self.lightning = lightning
        self.viewership = viewership
        Stadium.total_viewership += viewership

    def get_data(self):
        """
        Виведення значень
        """
        print("viewership:", self.__viewership, "name:", self.__name, "lightning:", self.__lightning, "event:", self.event, "area:", self.area)

    def get_viewership(stad):
        """
        Функція для отримання кількості глядачів на стадіоні
        """
        return stad.__viewership


    def most_popular_stadium(stadiums):
        """
        Функція для знаходження найбільш відвідуваного стадіону
        """
        most_popular = max(stadiums, key=Stadium.get_viewership)
        print(f"Most popular stadium is {most_popular.__name} with {most_popular.__viewership} viewership")

    def __del__(self):
        """
        Деструктор класу
        """
        Stadium.total_viewership -= self.__viewership
        print('Object is deleted')


def main():
        stad1 = Stadium()
        stad2 = Stadium(40000, 'Metalist', '2400 lux', 'Футблол', 100)
        stad3 = Stadium(21000, 'Karpaty', '2400 lux', 'Football', 100)

        stad1.get_data()
        stad2.get_data()
        stad3.get_data()

        print(f"\nTotal viewership: {Stadium.total_viewership}")
        Stadium.most_popular_stadium([stad1, stad2, stad3])

if __name__ == "__main__":
    main()