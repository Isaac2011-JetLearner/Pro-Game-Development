class Recipe:
    def __init__(self,food,flour,bakingpowder,chocolate,butter,milk,oil,):
        self.food = food
        self.flour = flour
        self.bakingpowder = bakingpowder
        self.chocolate = chocolate
        self.butter = butter
        self.milk = milk
        self.oil = oil

    def Baking(self):
        print("Baking...")
        print(f"food: {self.food}")
        print(f"flour: {self.flour}")
        print(f"bakingpowder: {self.bakingpowder}")
        print(f"chocolate: {self.chocolate}")
        print(f"butter: {self.butter}")
        print(f"milk: {self.milk}")
        print(f"oil: {self.oil}")

    # def Frying(self):
    #     print(f"food: {self.food}")
    #     print(f"flour: {self.flour}")
    #     print(f"bakingpowder: {self.bakingpowder}")
    #     print(f"chocolate: {self.chocolate}")
    #     print(f"butter: {self.butter}")
    #     print(f"milk: {self.milk}")
    #     print(f"oil: {self.oil}")

cookies = Recipe("Cookies","100g","20g","20g","10g","200g","0g")

cookies.Baking()