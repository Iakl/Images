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

def get_fibonacci_lower_than_x(x):
    fibonacci = []
    a, b = 0, 1
    while a < x:
        fibonacci.append(a)
        a, b = b, a + b
    return fibonacci

def get_numbers_lower_than_x(serie, x):
  if serie == "primes":
      return get_primes_lower_than_x(x)
  elif serie == "fibonacci":
      return get_fibonacci_lower_than_x(x)
  elif serie == "pi":
      return get_pi_digits_lower_than_x(x)
  else:
      return []


# def get_pi_digits_lower_than_x(x):
#   pi_digits = []
#   num = 1
#   pi_num = 0
#   while pi_num < x:
#       pi_num = pi(num) -
#       num += 1
#   return pi_digits

def arccot(x, unity):
    sum = xpower = unity // x
    n = 3
    sign = -1
    while 1:
        xpower = xpower // (x * x)
        term = xpower // n
        if not term:
            break
        sum += sign * term
        sign = -sign
        n += 2
    return sum

def pi(digits):
    unity = 10 ** (digits + 10)
    pi = 4 * (4 * arccot(5, unity) - arccot(239, unity))
    return pi // 10 ** 10

def get_primes_lower_than_x(x):
  primes = []
  num = 2
  while num < x:
      if is_prime(num):
          primes.append(num)
      num += 1
  return primes 


print(pi(1000))