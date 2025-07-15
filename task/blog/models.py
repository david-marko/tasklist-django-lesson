from django.db import models

# new_post = {
#     "title": title, # Character, String
#     "body": body,
#     "excerpt": excerpt,
#     "author": author,
#     "date": date,
#     "image": image,
#     "status": status,
#     "link": link
# }

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255) # a blog should have a title as a string not longer than 255 characters
    body = models.TextField() # A body should be a text with any amount of characters
    excerpt = models.TextField()
    author = models.CharField(max_length=15, default='Admin') 
    date = models.DateField(auto_now_add=True) # I want a column for dates. But, if someone does not provide it, then automatically add the date now.
    image = models.TextField() # image link
    status = models.CharField(default="draft", max_length=15) # either draft or published
    link = models.TextField()
