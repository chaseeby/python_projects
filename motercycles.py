motercycles = ['honda', 'yamaha', 'suzuki']
print(motercycles)

motercycles.append('ducati')
print(motercycles)

motercycles = []
motercycles.append('honda')
motercycles.append('yamaha')
motercycles.append('suzuki')

print(motercycles)

motercycles.insert(0, 'ducati')
print(motercycles)

motercycles = ['honda', 'yamaha', 'suzuki']
del motercycles[1]
print(motercycles)

motercycles = ['honda', 'yamaha', 'suzuki']
print(motercycles)

last_owned = motercycles.pop()

print(f'The last motercycle I owned was a {last_owned.title()}')

motercycles = ['honda', 'yamaha', 'suzuki']
print(motercycles)

first_owned = motercycles.pop(0)

print(f'The first motercycle I owned was a {first_owned.title()}')

motercycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motercycles)

too_expensive = 'ducati'
motercycles.remove(too_expensive)
print(motercycles)
print(f"\nA {too_expensive.title()} is a little to expensive for me.")



