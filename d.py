d_list = ['a','b','c','b','d','m',
           'n','n'
]

duplicates =[]

for value in d_list:
  if d_list.count(value) > 1:
    if value not in dupllicates:
      duplicates.append(value)

print(duplicates)