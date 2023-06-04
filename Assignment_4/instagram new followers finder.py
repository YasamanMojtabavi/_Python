import instaloader
import getpass

L=instaloader.Instaloader()

username=input("please enter username: ")
password=getpass.getpass("please enter password: ")
L.login(username,password)
print("hooora!successfuly logged in! ")

profile=instaloader.Profile.from_username(L.context,username)

f=open("followers.txt","r")
old_followers=[]
for line in f:
    old_followers.append(line)
f.close()

new_followers=[]
for follower in profile.get_followers():
    new_followers.append(follower)

for new_follower in new_followers:
    if new_follower not in old_followers:
        print(new_follower)


f=open("followers.txt","w")
for follower in new_followers:
    f.write(follower + "\n")
f.close


