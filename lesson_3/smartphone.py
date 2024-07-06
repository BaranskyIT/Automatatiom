# class Smartphone:
#         def __init__(self, mark, model, number):
#             self.mark = mark
#             self.model = model
#             self.number = number
    
#             self.print_mark()
#             self.print_model()
#             self.print_number()

#         def print_mark(self):
#             print(self.mark)

#         def print_model(self):
#             print(self.model)

#         def print_number(self):
#             print(self.number)

class Smartphone:
    def __init__(self, brand, model, phone_number):
        self.brand = brand
        self.model = model
        self.phone_number = '+7' + str(phone_number)

    def __str__(self):
        return f"{self.brand} - {self.model}. {self.phone_number}"
