from brightway2 import *

projects.set_current('cats and dogs')

db = Database('a&e')

a_and_e_data = {
    ("a&e", "cat"): {
        'name': 'cat',
        'unit': 'kilogram',
        'color': 'black',  # Custom field - you can add whatever fields you need
        'exchanges': [{
            'input': ('a&e', 'cat food'),
            'amount': 10,
            'type': 'technosphere'
        }, {
            'input': ('a&e', 'kitty litter'),
            'amount': 10,
            'type': 'technosphere'
        }, {
            'input': ('a&e', 'smell'),
            'amount': 1,
            'type': 'biosphere'
        }]
    },
    ("a&e", "kitty litter"): {'name': 'yuck'},
    ("a&e", "cat food"): {'name': 'yum'},
    ("a&e", "smell"): {'name': 'stinky', 'type': 'biosphere'},
}

db.write(a_and_e_data)

act = db.get('cat')
print(act)
print('----------------------')
act['location'] = 'indside'
act['categories'] = ['felis', 'catus']

print(act)
print('----------------------')
act.save()

for key in act:
    print(key, ':', act[key])

print(act.key)
print('----------------------')
for exc in act.exchanges():
    print(exc)
print('----------------------')
print('technosphere:')
for exc in act.technosphere():
    print(exc)
print('biosphere:')
for exc in act.biosphere():
    print(exc)
print('production:')
for exc in act.production():
    print(exc)
print('----------------------')
print(len(act.exchanges()))
print('----------------------')

na = db.new_activity('dog')
na['name'] = 'fido'
new_exc = na.new_exchange(input = act, amount = 1, type = 'technosphere')
new_exc.save()


