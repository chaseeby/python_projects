guest_list = ['Chase', 'Madison', 'Lila']
print(guest_list)

guest_list.remove('Chase')
guest_list.append('Alex')

print(guest_list)

guest_list.insert(1, 'Joan')
print(guest_list)

for name in guest_list:
    print(f"{name}, you are welcome to the party")
