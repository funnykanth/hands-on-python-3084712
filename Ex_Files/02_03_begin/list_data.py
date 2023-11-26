names = ['durga','phani', 'kanth', 'pilli','Veda', 'Vasuki', 'Leena', 'Lee']
nums = [10, 20, 30, 40]
# print (name)
# print (name[1].upper())
# print (name[:2])
# print(name[::-3])
# print(min(nums) )
# print(max(nums) )
# print (sum (nums))
for name in names:
  print(name.upper())
print ('reversed: --> ')
for name in reversed(names):
  print(name.lower())

i =0
while i < len(nums):
  print(nums[i])
  i += 1

for name, age in zip(names[3:], nums):
  print (f"{name} is of age {age}")

  print( "Range")
  for num in range(10):
    print (num)

  print( "Range Reverse")
  for num in reversed(range(10)):
    print (num)