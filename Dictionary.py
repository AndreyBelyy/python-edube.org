fruites = {
    'apple': 'red',
    'pineapple': 'yellow',
    'banana': 'yellow',
    'grape': 'green',
    'kg': 10
     }
print(fruites['apple'])

fruites['peach'] = 'yellow'
print(fruites)

del fruites['grape']
print(fruites)

fruites['kg'] = fruites['kg'] + 2
while fruites['kg'] < 20:
    fruites['kg'] = fruites['kg'] + 1
    print(fruites)

print(fruites.values())
print(fruites.keys())
print(fruites)