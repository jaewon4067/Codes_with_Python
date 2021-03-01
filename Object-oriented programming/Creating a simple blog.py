"""

As I'm learning OOP, I'm going to make a mini blog where people can post with me. 
I'm going to create a 'Post' class and a BlogUser' class to print out the full contents of the blog.

"""

class Post:
    def __init__(self, date, content):
        # The post class has date and content as attributes.
        self.date = date
        self.content = content

    def __str__(self):
        # a method that returns the infomation of the post.
        return "Date: {}\n Content: {}".format(self.date, self.content)
    
    
class BlogUser:
    def __init__(self, name):
        # Users from a blog have name and posts as attributes.
        self.name = name
        self.posts = []

    def add_post(self, date, content):
        # Append a new post.
        new_post = Post(date, content)
        self.posts.append(new_post)

    def show_all_posts(self):
        # Print all the posts
        for post in self.posts:
            print(post)
        

    def __str__(self):
        # Return a simple sentence with the name.
        return("Hello, I am {}.\n".format(self.name))
    

# Create a blog user instance.
blog_user_1 = BlogUser("Jaewon")

# Print a blog user instance(hello, name)
print(blog_user_1)

# Write two posts 
blog_user_1.add_post("1th March 2021", """
It's already march, time flies.
Let's be a better person!
""")

blog_user_1.add_post("28th Feb 2021", """
I love coding, I don't have to think about anything else.
I like problem solving, I want to live my life happy like this with Python!
""")

# Print all the post
blog_user_1.show_all_posts()
