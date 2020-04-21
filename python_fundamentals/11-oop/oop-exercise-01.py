class Vehicles:

    def __init__(self, name, price, types='ford', color='white'):
        self.name = name
        self.types = types
        self.color = color
        self.price = price

    def describe(self):
        return f"The name of the Vehicle is {self.name}, type is {self.types} of {self.color} and price {self.price}"

    def __str__(self):
        return f"Vehicles {self.name} and type {self.types}"


list_of_vehicles = []
for i in range(3):
    name = input("Enter name: ")
    price = int(input("Enter price"))
    yes_no = input("do you want to add type and color : y or n :")
    if yes_no == 'y':
        types = input("Enter type: ")
        color = input("Enter color: ")
        vehicle = Vehicles(name, price, types, color)
    else:
        vehicle = Vehicles(name, price)

    list_of_vehicles.append(vehicle)

for i in list_of_vehicles:
    print(i.describe())
print(list_of_vehicles[0])
