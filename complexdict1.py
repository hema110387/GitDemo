person = {
    'name':'kalai',
    'age':34
}

print(person['name'])
print(person['age'])

person ['age'] =36
print(person)

person['profession']='Developer'
print(person)

person['location']=(14.34578,45.8907)

person['address']= {
    'street':'paavai street',
    'city':'chennai',
    'pincode':'600043'
}
person['languages']=['c','c#','dba','java']
print(person)

for key in person.keys():
    print(key)

for value in person.values():
    print(value)

for key,value in person.items():
    print (f'{key.title()}={value}')

print('looping through complex dictionary')

for key,value in person.items():
    if isinstance(value,tuple) or isinstance(value,list):
        print(key.title())
        for items in value:
            print(f'\t {items}')

    elif isinstance(value,dict):
        print(key.title())

        for key2,value2 in value.items():
            print(f'\t {key2.title()}={value2}')

    else:
                print(f'{key.title()}={value}')

