
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