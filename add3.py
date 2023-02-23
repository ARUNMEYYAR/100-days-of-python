Str1 = input('Enter a string:')
count = 0
for i in Str1:
  if ord(i) >= 48 and ord(i) <= 57:
   count= count + int(i)
print('Sum is: ' + str(count))