import instaloader
import getpass
from instaloader import Instaloader

f=open("D:\python\Python\Assignment_4again\Followers.txt","r")
old_followers =[]
for line in f:
    old_followers.append(line)
f.close()

L=Instaloader()

user=input("username: ")
passwd=getpass.getpass("password: ")

L.login(user, passwd)
print("successfully logged in.")

profile=instaloader.Profile.from_username(L.context,"y.s.mojtabavi")

new_followers=[]
for follower in profile.get_followers():
    new_followers.append(follower)

for old_follower in old_followers:
    if old_follower not in new_followers:
        print(old_follower)


f=open("D:\python\Python\Assignment_4again\Followers.txty","w")
for follower in new_followers:
    f.write(follower + "\n")
f.close() 