import instaloader

bot1 = instaloader.Instaloader()

username="profile_username"

print(bot1.download_profile(username,profile_pic_only=True))
