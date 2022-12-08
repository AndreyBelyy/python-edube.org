def create_record(name, telephone, address):
    """Address book"""
    record = {
        'name': name,
        'phone': telephone,
        'address': address
    }
    return record
user1 = create_record("Petr", "903", "Cyprus")
user2 = create_record("Petrarka", "923", "Greece")

print(user1)
print(user2)

def awards(category, *persons):
    """Give awards"""
    for person in persons:
        print("Senor " + person.title() + " nagrajdaetsia award "+ category)
awards("Hours working", "Ilia", "Petr")
awards("For Love & Care", "galina", "Aleksandr")