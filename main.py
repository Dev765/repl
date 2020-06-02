import d

pictue = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

#1:Iterate over picture
 #if 0 print empty-space 
 #if 1 print *

for row in pictue:
  for pixel in row:
    if pixel == 1:
      print("*", end="")
    else:
      print("", end="")
  print("")