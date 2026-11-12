'''TASK2. Create a User class that uses a class-level variable user_count to keep track of the
total number of users created.
Each time a new User object is created, the count should increase.
Include a method to display the current user count.'''

class User:
    user_count=0

    def __init__(self,username):
        self.username=username
        User.user_count+=1

    @classmethod
    def display(cls):
        print(f"the number of users is {cls.user_count}")

obj=User("Guest")
User.display()

user1=User("Alice")
user2=User("John")

User.display()