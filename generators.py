#Generators - How to use them and the benefits you receive
#Generators dont hold the entire result in memory, it yeilds each one!
#Generators are more readable when it comes to lists
#before we use a generator, lets use a regular function that sqares a list of numbers
#def sqare_numbers(nums):
#    result = []
#    for i in nums:
#        result.append(i*i)
#    return result

#my_nums = sqare_numbers([1,2,3,4,5])

#print(my_nums)

#lets use a generator to do the same thing
#wont need result variable, return statement, or result.append
#we have to add a yield keyword, which makes it a generator
#Generators dont hold the entire result in memory, it yields each result!
def sqare_numbers(nums):
    for i in nums:
        yield (i*i)

#my_nums = sqare_numbers([1,2,3,4,5])

#print(next(my_nums)) #prints 1
#use a for loop instead for generators to print all results
#for num in my_nums:
#    print(num)

#list comprehesion using regular function from first example
my_nums = [x*x for x in [1,2,3,4,5]]    #list comprehesion for functions use sqare bracets
print(my_nums) #prints list
for num in my_nums:
    print(num)

#list comprehesion genereator example better for performance of long lists
my_nums = (x*x for x in [1,2,3,4,5])#list comprehesion for genereators use parenthsis
print(my_nums) #generator list comprhension object
for num in my_nums:
    print(num)
