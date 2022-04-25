import time

# Creates a string of n fibonacci numbers in sequence, starting with the number, f0 and f1
# Returns the string created and the last 2 fibonacci numbers that composes it
def fib_chunk(n, f0, f1): 
    fib = [(f1 + f0) , (f1 + f0 + f1)]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    # Convert each integer to a string
    fibint = [str(int) for int in fib] 
    # Combine each string into a sequence
    sfib = "".join(fibint) 
    vf0 = fib[-2]
    vf1 = fib[-1]
    return sfib, vf0, vf1 

def is_prime(n) : 
    if (n <= 1) :
        return False
    if (n <= 3) :
        return True
    if (n % 2 == 0 or n % 3 == 0) :
        return False
    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6
    return True

# Decoder from 10digit number to letter
def num2alph(n):
    salp = 'abcdefghijklmnopqrstuvwxyz'
    alp = list(salp)
    v = ''
    a = []
    s = str(n)
    s1 = list(s)
    for x in range(0,10,2):
        a.append(s1[x] + s1[x + 1])
    ai = [(int) for int in a]
    ai = list(map(int,ai))
    for x in ai:    
        v = v + (alp[x % 26])
    return v

t0 = time.time()
x = 0
pfib = []
# First 3 fibonacci numbers
fib = '112'
# Last 2 fibonacci numbers of the sequence
f0 = 1
f1 = 2

fib1, f0, f1 = fib_chunk(5, f0, f1) 
# Position of wanted prime numbers
P1 = 44722
P2 = 53215

# Adds fib numbers to the sequence, until at least P2 prime numebers are detected
while len(pfib) < P2: 
    fib = fib + fib1 
    # Runs trough the entire string checking for 10 digit prime numbers
    while x < (len(fib)-10): 
        # Gets s10, a 10 digit integer from the sequence
        s10 = int(fib[x:(x + 10)])
        # If s10 is prime, stores it in a pfib array
        if is_prime(s10): 
            pfib.append(s10)
        x += 1
    # Get the next chunck of number to be added to the sequence
    fib1, f0, f1 = fib_chunk(1, f0, f1) 

print('1 st: ', pfib[1 - 1])
print(P1, 'nd: ', pfib[P1 - 1], ' = ', num2alph(pfib[P1 - 1]))
print(P2, 'th: ', pfib[P2 - 1], ' = ', num2alph(pfib[P2 - 1]))
t1 = time.time()
print("Time required :", t1 - t0)
