S1 = {2, 3, 1}
S2 = {'a', 'b', 'c'}
S3 = list(zip(S1, S2))
print(S3, "\n")

lst1 = [10, 20, 30, 40]
lst2 = [100, 200, 300, 400]
for x, y in zip(lst1, lst2[::-1]):
    print(x, y)

stocks = ['Reliace', 'Infosys', 'TCS']
prices = [2175, 1127, 2750]

new_dict = {stocks : prices for stocks, 
            prices in zip(stocks, prices)}
print("\n{}".format(new_dict))