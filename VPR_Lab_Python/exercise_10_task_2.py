class Car:
    def __init__(self, brand, model, price, color, manufacturer_year):
        self.car_brand = brand
        self.car_model = model
        self.car_price = price
        self.car_color = color
        self.manufacturer_year = manufacturer_year

    def display_info(self):
        return f'{self.car_brand} {self.car_model} {self.car_price} {self.car_color} {self.manufacturer_year}'




brands = ['Lada', 'Bmw', 'Dacia', 'Ford', 'Nissan', 'Lada', 'Volvo']
models = ['2107', 'Model M', 'Duster', 'Focus', 'Patrol', '2105', 'XC60']
prices = [33000, 13000, 10000, 1000, 5000, 9000, 9001]
colors = ['Green', 'Yellow', 'Blue', 'Black', 'Yellow', 'Red', 'White']
years = [1989, 2009, 2022, 2011, 1999, 2000, 2001]
cars_list = []
for idx in range(7):
    cars_list.append(Car(brands[idx], models[idx], prices[idx], colors[idx], years[idx]))


def sort_price():
    cars_prices = [c.car_price for c in cars_list]
    cars_prices.sort(key=lambda x: -x)
    return cars_prices

print(sort_price())

def list_by_brand(brand):
    cars = [car for car in cars_list if car.car_brand == brand]
    for car in cars:
        print(car.display_info())


list_by_brand('Lada')

def search_color(color):
    car = list(map(lambda x: x if x.car_color == color and x.car_price == max(x.car_price for x in cars_list if x.car_color == color) else None, cars_list))
    print(car)
    cars_with_the_color = [car for car in cars_list if car.car_color == color]
    max_price = max(car.car_price for car in cars_with_the_color)
    my_car = [car for car in cars_with_the_color if car.car_price == max_price][0]
    print(my_car.display_info())

search_color('Yellow')

def newest_car():
    year = 2022
    cars = [car for car in cars_list if car.manufacturer_year == year]
    return cars

print(newest_car())

