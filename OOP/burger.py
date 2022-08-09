class Burger:
    def __init__(self, meat, sauce , lettuce='', tomato='', size='', cheese=''):
        self.meat=meat
        self.lettuce=lettuce
        self.tomato=tomato
        self.sauce=sauce
        self.size=size
        self.cheese=cheese
    def orderDetails(self):
        print('Your Order:')
        print(f'{self.size} {self.meat} Burger, Sauce: {self.sauce}, Lettuce: {self.lettuce}, Tomato: {self.tomato}, Cheese: {self.cheese}')

class Medium(Burger):
    def __init__(self, meat, sauce, lettuce='', tomato='', size='', cheese=''):
        super(Medium, self).__init__(meat, sauce, lettuce, tomato, size, cheese)
        self.lettuce=6
        self.tomato=6
        self.size='Medium'
        self.cheese=6

class Large(Burger):
    def __init__(self, meat, sauce, lettuce='', tomato='', size='', cheese=''):
        super(Large, self).__init__(meat, sauce, lettuce, tomato, size, cheese)
        self.lettuce=8
        self.tomato=8
        self.size='Large'
        self.cheese=8

meat_order=input('Meat(Pork, Ham, Chicken): ')
sauce_order=input('Sauce(bbq, mayonnaise):')

# medium1=Medium(meat_choice, sauce_choice)
# medium1.orderDetails()

large1=Large(meat_order, sauce_order)
large1.orderDetails()