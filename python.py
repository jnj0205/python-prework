### 1 Write a function to print "Hello_USERNAME!"USERNAME###

def hello_name(user_name):
    print("Hello " + user_name.title() + "!" + user_name.title())
hello_name(user_name='Ana')

### 2 Write a python fuction, first-odds that prints the odd numbers###
###from 1-100 and returns nothing. def first-odds():###

def first_odds():
 
 for n in list(range(1,100,2)):
   if n % 2 == 1:
     print(n)
first_odds()

### 3 Write a function, max_num_in_list to return the max number of a given list.###
### The first line of the code has been defined as below. def max_num_in_list(a_list):###


def max_num_in_list(max_num):
    max_num = max(a_list)
    return max_num

test = max_num_in_list([1,2,3,4])

print(max_num_in_list([1,2,3,4])) 


### 4 Write a function to return if the given year is a leap year.### 
###A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400.###
###  The return should be boolean Type (true/false). def is_leap_year(a_year):  ###
  
  
def is_leap_year(n):

    put = False

    if n % 4 == 0 :
         put = True
    if     n % 100 == 0 :
         put = False
    if     n % 400 == 0:
         put = True
    return put

n = 2024
if(is_leap_year(n)):
    print("This year is a leap")
    
else: 
      print("Is not a leap Year")
    
### 5 Write a function to check to see if all numbers in the list are consecutive numbers.
### For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.###
### The return should be boolean Type. def is_consecutive(a_list):###

def is_consecutive(a_list):
   i = 0
   status = True
   while i < len(a_list) - 1:
        if a_list[i] + 1 == a_list[i + 1]:
            i += 1
        else:
            status = False
            break
a_list = [1,2,3,4,5,7,8]
print(status)
    
