"""

I will simply implement the 'follow function' of Instagram with OOP. 

The follow function requires two main actions.
'Following' means the people who follow me are in the following list.
'Follower' means the people who follow me are int the foller list.

In addition to the follow method, the 'num_following' method, which shows the number of users who follow the user,
and the 'num_followers' method, which shows the number of users who follow the user.

When I add all of these methods to the User class and then run the code, the following execution results should be coming up:

Jenny 2 2
Rose 1 3
Jisu 2 0
Lisa 1 1

"""

class User:
    # Set the init
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
        self.following_list = []    # The people who follow me are in the following list.
        self.followers_list = []    # The people who I follow are in the follower list.
        
    # Follow method
    def follow(self, another_user):
        self.following_list.append(another_user)
        another_user.followers_list.append(self)
        
    # Return the number of people I follow
    def num_following(self):
        return len(self.following_list)

    # Return the number of people who follow me
    def num_followers(self):
        return len(self.followers_list)  
      
user1 = User("Jenny", "jenny@blackpink.kr", "123456")
user2 = User("Rose", "rose@blackpink.kr", "abcdef")
user3 = User("Jisu", "jisu@blackpink.kr", "123abc")
user4 = User("Lisa", "lisa@blackpink.kr", "abc123")

# Each user follow each other who they want.
user1.follow(user2)
user1.follow(user3)
user2.follow(user1)
user2.follow(user3)
user2.follow(user4)
user4.follow(user1)

# Print user name, the number of followers and the number of followings.
print(user1.name, user1.num_followers(), user1.num_following())
print(user2.name, user2.num_followers(), user2.num_following())
print(user3.name, user3.num_followers(), user3.num_following())
print(user4.name, user4.num_followers(), user4.num_following())
        
        
        
        
        
        
