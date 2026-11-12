'''TASK2: Implement a PasswordManager class in Python where the password is
stored privately and can be set or changed only after validation'''

class Password:
    def __init__(self,password):
        self.__password=password

    def validation(self,old_pw,new_pw):
        if old_pw == self.__password and len(new_pw)>6:
            self.__password = new_pw
            print("password updated")
        else:
            print("cant be verified")
c1=Password("123456")
c1.validation("123456","1234578")

