CAPTALS = {
    'USA': 'Washington', 
    'Canada': 'Ottawa', 
    'UK': 'London', 
    'Russia': 'Moscow', 
    'China': 'Beijing', 
    'INDIA': 'Delhi'
}

CAPTALS.update({'Germany': 'Berlin'})
CAPTALS.update({'USA': 'Las Vegas'})
CAPTALS.pop('China')
CAPTALS.clear()

print('{')
for key, value in CAPTALS.items():
    print(f'\t\"{key}\": \"{value}\",')
    
print('}')
