print("PY4E exercise 5.1")

num = 0
total = 0.0
while True :
  sval = input('Enter a number: ')
  if sval == 'done' :
    break
  try:
    fval = float(sval)
  except:
    print('Invalid input.')
    continue
  print(fval)
  num = num + 1
  total = total + fval

print('ALL DONE')
print(total, num, total/num)