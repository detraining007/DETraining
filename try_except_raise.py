<<<<<<< HEAD
try:
  x = int(input())
  if x > 5:
    raise ValueError("x cannot be greater than 5")
  elif x==5:
      raise ValueError("X cannot be 5")
except ValueError as e:
=======
try:
  x = int(input())
  if x > 5:
    raise ValueError("x cannot be greater than 5")
  elif x==5:
      raise ValueError("X cannot be 5")
except ValueError as e:
>>>>>>> 95904fb3354e403a37a876779019fbdd2e0d26f6
    print(f"Error: {e}")