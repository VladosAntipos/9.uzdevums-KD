brother = int(
  input("brother:")
)

sister = int(
  input("sister:")
)

if sister > brother:
  print("sister is older")
elif brother > sister:
  print("brother is older")
else:
  print("equal age")