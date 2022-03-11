
"""Create a to-do list using Disctionary"""
people = {
    'Nurul ' : {'I need to poop'  , 'Study math'},
    'Abdullah' : {'My first activity' , 'Prepare lunch'},
    'Ayesha' : {'Maybe watch my cartoon' , 'Disturb my parents' , 'ipad?'},
    'Omar' : {'Cry' , 'eat' , 'poo poo' , 'disturb mummy'}
}

for name , todolists in people.items():
    print(f"\n{name.title()}'s  to do list are : ")
    for todolist in todolists:
        print(f"\t{todolist.title()}") 
        
#Add value to Dictionary
class DictionarySample:
    def __init__(self) :
        self = dict()
        
    #Function to add item to DictionarySample 
    def add(self , key , value):
        self[key] = value
        
dictionary1 = DictionarySample()

dictionary1.key = input('Enter the key : ')
dictionary1.value = input ('Enter the value : ')

dictionary1.add(dictionary1.key, dictionary1.value)
dictionary1.add(2 , 'Student 2')

print(dictionary1)
        