print("PY4E exercise 5.2")

num = 0
total = 0.0
while True :
  sval = input('Enter a number: ')
  if sval == 'done' :
    break
  try:
    fval = float(sval)
  except:
    print('Invalid input. Please enter a number or the text "done" when you are finished.')
    continue
  print(fval)
  num = num + 1
  total = total + fval

print('ALL DONE')
print(total, num, total/num)