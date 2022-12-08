fruites = {
    'apple': 'red',
    'pineapple': 'yellow',
    'banana': 'yellow',
    'grape': 'green',
    'kg': 10,
    'chery': ['yellow', 'red']
     }

all_green = []
all_green.append(fruites)

for x in range(10):
    all_green.append(fruites)
for z in all_green:
    print(z)


