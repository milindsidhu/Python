from user import User
from post import Post

app_user1 = User("221B@BakerStreet.com", "Sherlock Holmes", "moriarty", "Detective")
app_user1.get_user_info()

# similarly for other users

new_post = Post("'On a secret mission today!'", app_user1.name)
new_post.get_post_info()
