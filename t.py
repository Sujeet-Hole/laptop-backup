z =[{'category': 'chai', 'description': 'c', 'date': 'c', 'Amount':600.00},
     {'category': 'fuel_charges ', 'description': 'rt', 'date': 'grf', 'Amount': 1000.0},
     {'category': 'chai', 'description': 'c', 'date': 'c', 'Amount':600.00}
     ]
categories = {}


for item in z :
    
    key = item["category"]
    value = item["Amount"]

    if key not in categories :
        categories[key] = 0

    categories[key] += int(value)


print(categories)




