from sqlite3 import Date

class Student : 
    def __init__(self , firstname , lastname , classID, registerDate , status , dob , email):
        """To initialize attributes to describe a car"""
        self.firstname = firstname
        self.lastname = lastname 
        self.classID = classID
        self.registerDate = registerDate 
        self.status = status 
        self.email = email
        
    #This function is to return student information
    def get_student_info(self): 
        information  = f"Full Name : {self.firstname}  {self.lastname}\n Class ID :  {self.classID}\n Registration Date : {self.registerDate}\n Status :  {self.status}\n Email :  {self.email}"
        return information
    
    @classmethod
    def set_student_info(self):
        while 1 : 
            try :
                firstname = input('First Name : ')
                lastname = input('Last Name : ')
                classID = int(input ('Class  : '))
                registerDate = Date.today
                status = 1
                email = input ('Email : ')
                
            except:
                continue
  
    
#TO TEST THE CLASS
student1 = Student('Nurul Nadzirah' , 'Zaid' , 1 , Date.today() , 1 , Date.today , 'nadzirahzaid144@gmail.com')
print(student1.get_student_info())
             