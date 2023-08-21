from instagrapi import Client

# Your username and password
user = ""
password = ""

# Start from this post
post_url = ""

cl = Client()
cl.delay_range = [4, 7]
cl.login(user, password)

pk = cl.media_pk_from_url(post_url)
id = cl.media_id(pk)

count = 0

with open("liked.txt", "w") as f:
    for user in cl.media_likers(id):
        if count > 500:
            print("500 accounts observed")
            break
        print("Onto user: " + user.username)
        count += 1
        if user.is_private:
            print("User: " + user.username + " is private. Continuing...")
            continue
        user_id = cl.user_id_from_username(user.username)
        posts = cl.user_medias(user_id, 2)
        for i in range(len(posts)):
            cl.media_like(posts[i].id)
            f.write(str(user.username) + " " + str(posts[i].id) + "\n")
            print("Successfully liked " + user.username + "'s post!")
        