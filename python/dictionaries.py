'''
Python dictionaries
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
'''
<class 'dict'>
'''


for x in thisdict:
  print(x)
'''
brand
model
year
'''
for x in thisdict.keys():
  print(x)
'''
brand
model
year
'''

for x in thisdict.values():
  print(x)
'''
Ford
Mustang
1964
'''

for x, y in thisdict.items():
  print(x, y)

'''
brand Ford
model Mustang
year 1964
'''

