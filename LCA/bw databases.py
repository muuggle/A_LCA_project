from brightway2 import *

projects.set_current('databases demo')

db = Database('example')

example_data = {
    ('example', 'A'): {
        'name': 'A',
        'exchanges': [{
            'amount': 1.0,
            'input': ('example', 'B'),
            'type': 'technosphere'
            }],
        'unit': 'kilogram',
        'location': 'here',
        'categories': ('very', 'interesting')
        },
    ('example', 'B'): {
        'name': 'B',
        'exchanges': [],
        'unit': 'microgram',
        'location': 'there',
        'categories': ('quite', 'boring')
        }
    }

db.write(example_data)

print(db.random())

num_exchanges = [(activity, len(activity.exchanges())) for activity in db]
print(num_exchanges)

print(db.search('*'))

del databases[db.name]
