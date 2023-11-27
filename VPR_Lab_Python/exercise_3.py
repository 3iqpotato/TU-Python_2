# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# my_tuple = (2, 3, 4,5)
# set_1 = {2, 3, 4, 5}
# my_dict = {
#     1: '5',
#     2: '3',
#     3: '8'
# }
#
# print(my_list[2:-5])
# print(my_list[-4:-2])
# print(my_list[-6:-4]) # винаги първия трябва да е по малкъ от 2рия
#
# #увеличаване на стоиностите с 1
# for i in range(len(my_list)):
#     my_list[i] += 1
#
# print(my_list)
# #някакви глупости от дъската които госпожата иска!!!
# my_list.append(5)
# my_list.insert(2, 4)
# my_list.remove(3)
# my_list.pop(2)
#
# print(my_list[2]/ 3)
# print(my_list[-2]// 2)
#
# print(my_list.count(3))
# print(my_list.index(10))
# print(min(my_list))
# print(max(my_list))
# print(sum(my_list))
# print(sum(my_list) / len(my_list))
#
# if my_list[i] == 4:
#     my_list.pop(i)
#
# print(my_list)
import sys


#The task of The Day!!!
# products = ['Laptop', 'Computer', 'Mouse', 'Key Board']
# prices = [3333, 4000, 120, 90]
# sold_products = 0
# options = {
#     1: 'Add product',
#     2: 'Sell product',
#     3: 'Show menu',
#     4: 'Show cheapest product',
#     5: 'Show most expensive product',
#     6: 'Show products in price range',
#     7: 'Show profit'
# }
#
# while True:
#     for n, value in options.items():
#         print(f"Option {n} {value}" )
#     print()
#     option = int(input('Enter option: '))
#
#     if option == 1:
#         product = input('Enter a product: ')
#         price = int(input("Enter price: "))
#
#         products.append(product)
#         prices.append(price)
#
#     elif option == 2:
#         product = input('Enter a product: ')
#         count = int(input("Enter count: "))
#         if product not in products:
#             print('Invalid product')
#
#         else:
#             idx = products.index(product)
#             sold_products+=prices[idx] * count
#
#             print(f'The product price is {prices[idx]}')
#             print(f'Thanks for your purchase!')
#
#
#     elif option == 3:
#         print('Products at the store:')
#         for i in range(len(products)):
#             print(f'{products[i]} --- {prices[i]} lv.')
#
#     elif option == 4:
#         min_price_idx = prices.index(min(prices))
#         product = products[min_price_idx]
#
#         print(f'Тhe cheapest product is {product} with price {prices[min_price_idx]}')
#
#     elif option == 5:
#         max_price_idx = prices.index(max(prices))
#         product = products[max_price_idx]
#
#         print(f'Тhe most expensive product is {product} with price {prices[max_price_idx]}')
#
#     elif option == 6:
#         min_price = int(input('Enter first price: '))
#         max_price = int(input('Enter second price: '))
#
#         indexes_of_prices = [i for i in range(len(prices)) if min_price <= prices[i] <= max_price]
#
#         if indexes_of_prices:
#             for idx in indexes_of_prices:
#                 print(f'{products[idx]} costs {prices[idx]}')
#         else:
#             print('No products to display')
#
#     elif option == 7:
#         print(f'The profit is {sold_products}')

#same task but with my functions
def find_min_price(list_prices):
    curr_min = float('inf')
    for price in list_prices:
        if curr_min > price:
            curr_min = price
    return curr_min


def find_max_price(list_prices):
    curr_max = float('-inf')
    for price in list_prices:
        if curr_max < price:
            curr_max = price
    return curr_max



products = ['Laptop', 'Computer', 'Mouse', 'Key Board']
prices = [3333, 4000, 120, 90]
sold_products = []
options = {
    1: 'Add product',
    2: 'Sell product',
    3: 'Show menu',
    4: 'Show cheapest product',
    5: 'Show most expensive product',
    6: 'Show products in price range',
    7: 'Show profit'
}

while True:
    for n, value in options.items():
        print(f"Option {n} {value}" )
    print()
    option = int(input('Enter option: '))

    if option == 1:
        product = input('Enter a product: ')
        price = float(input("Enter price: "))

        products.append(product)
        prices.append(price)

    elif option == 2:
        product = input('Enter a product: ')
        count = int(input("Enter count: "))
        if product not in products:
            print('Invalid product')

        else:
            idx = products.index(product)
            for _ in range(count):
                sold_products.append(products[idx])

            print(f'The products price is {prices[idx] * count}')
            print(f'Thanks for your purchase!')


    elif option == 3:
        print('Products at the store:')
        for i in range(len(products)):
            print(f'{products[i]} --- {prices[i]} lv.')

    elif option == 4:
        min_price_idx = prices.index(find_min_price(prices))
        product = products[min_price_idx]

        print(f'Тhe cheapest product is {product} with price {prices[min_price_idx]}')

    elif option == 5:
        max_price_idx = prices.index(find_max_price(prices))
        product = products[max_price_idx]

        print(f'Тhe most expensive product is {product} with price {prices[max_price_idx]}')

    elif option == 6:
        min_price = float(input('Enter first price: '))
        max_price = float(input('Enter second price: '))

        indexes_of_prices = [i for i in range(len(prices)) if min_price <= prices[i] <= max_price]

        if indexes_of_prices:
            for idx in indexes_of_prices:
                print(f'{products[idx]} costs {prices[idx]}')
        else:
            print('No products to display')

    elif option == 7:
        price = 0
        for i in sold_products:
            
            price += prices[products.index(i)]

        print(f'The profit is {price:.2f}')







