#A mock list of toppings and prices to help organize items at "Len's Slice"
#A list of toppings
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

#A list of corresponding prices
prices = [2, 6, 1, 3, 2, 7, 2]

#Length of list 'toppings'
num_pizzas = len(toppings)

#Testing the code
print('We sell '+ str(num_pizzas) + ' different kinds of pizza!')

#Combining the toppings with the prices
pizzas = list(zip(prices, toppings))

#Testing the code
print(pizzas)

#Sorting the list 'pizzas'
pizzas.sort()

#Creating cheapest pizza var
cheapest_pizza = pizzas[0]

#Creating priciest pizza var
priciest_pizza = pizzas[-1]
 
#Creating 3 cheapest pizza var
three_cheapest = pizzas[0:3]

#Testing the code
print(three_cheapest)

#Counting number of $2 slices
num_two_dollar_slices = prices.count(2)

#Testing the code
print(num_two_dollar_slices)