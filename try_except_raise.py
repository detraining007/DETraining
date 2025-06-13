try:
  x = int(input())
  if x > 5:
    raise ValueError("x cannot be greater than 5")
  elif x==5:
      raise ValueError("X cannot be 5")
except ValueError as e:
    print(f"Error: {e}")
