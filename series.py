def is_prime(n):
  if n <= 1:
      return False
  for i in range(2, int(n ** 0.5) + 1):
      if n % i == 0:
          return False
  return True

def get_first_x_primes(x):
  primes = []
  num = 2
  while len(primes) < x:
      if is_prime(num):
          primes.append(num)
      num += 1
  return primes 

def get_primes_lower_than_x(x):
  primes = []
  num = 2
  while num < x:
      if is_prime(num):
          primes.append(num)
      num += 1
  return primes 


