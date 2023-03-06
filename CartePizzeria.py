class CartePizzeria:
    def __init__(self):
        self.pizzas = []

    def is_empty(self):
        return len(self.pizzas) == 0

    def nb_pizzas(self):
        return len(self.pizzas)

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def remove_pizza(self, name):
        for i, pizza in enumerate(self.pizzas):
            if pizza.name == name:
                del self.pizzas[i]
                return
            raise CartePizzeriaException(f"La pizza '{name}' n'existe pas dans la carte.")
