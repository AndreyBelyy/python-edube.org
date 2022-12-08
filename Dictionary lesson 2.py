fruites = {
    'apple': 'red',
    'pineapple': 'yellow',
    'banana': 'yellow',
    'grape': 'green',
    'kg': 10,
    'chery': ['yellow', 'red']
     }

all_green = []
#all_green.append(fruites.copy()) # diffrent copies of dictionary

for x in range(10):
    all_green.append(fruites.copy()) # diffrent copies of dictionary

print("_____________________________________")
all_green[1]['kg'] = 24
all_green[3]['grape'] = 'red'
for z in all_green:
    print(z)
