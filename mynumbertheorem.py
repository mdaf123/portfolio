import math 

def factorial_float(s):
  return math.gamma(s + 1)

def choose(n, k):
  return factorial_float(n) / (factorial_float(k) * factorial_float(n - k))

def summation_part_of_formula(b, c, w, seq):
  R=c-b+1
  q=0
  while R>0:
    q+=((-1)**(b+1))*choose(c, b)*float(seq[w+1-b])
    b+=1
    R= R-1
  return q

sequence = input("Enter a sequence of numbers separated by commas:\nex:1, 2, 3\n")
e = float(input("What is the degree of the polynomial?:\n"))
v = float(input("What is the leading coefficient of the polynomial?:\n"))
values = sequence.split(',')
f=len(values)-1
next_value = v*factorial_float(e) + summation_part_of_formula(1, e, f, values)
print("The next value in the sequence is " + str(next_value))
