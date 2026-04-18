test_dict = {"I'm" : 3, 'going' : 2, 'to' : 2, 'grab' : 2, 'a ' : 1, 'coffee' : 3}

print("The original dictionary : " +  str(test_dict))
  
In = int(input("Enter a value (1, 2, 3): "))

res = 0
for key in test_dict:
    if test_dict[key] == In:
        res = res + 1
      
print("Frequency of ", In ,"is : " + str(res))