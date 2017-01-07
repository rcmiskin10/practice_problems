#returns true ifnumber = to 2

def is_prime(n): 
  if n == 2: 
    return True
  #if even then no prime
  if n%2 == 0: 
    return False 
  if n<2: 
    return False 
  #for item in list of numbers 3 through squareroot of number, and only look at odd numbers
  for item in range(3,int(n**0.5),2): 
    #if no remainder then it is not prime
    if n%item == 0: 
      return False
  # if gets to this point then it is prime
  return True 
  
def prime_list(num): 
  list = range(0,num+1)#list of the numbers 0-the number given
  prim_list = [] 
  for item in list: 
    if is_prime(item):# if function returned True then append to list 
      prim_list.append(item) 
  return prim_list#  return list
  
prime_list(100)
# prints all prime numbers 1-100
