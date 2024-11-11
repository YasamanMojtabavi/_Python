import Actor
class Media:
    def __init__(self,n,di,I,u,du,c):
        self.name=n
        self.director=di
        self.IMDB_score=I
        self.url=u
        self.duration=du
        self.casts=c



    @staticmethod
    def add():
      name=input("name: ")
      di=input("director: ")
      Imdb=input("IMDB score: ")
      url=input("url: ")
      du=input("duration: ")
      t=input("time: ")
      number=input("enter number actor: ")
      list=[]
      for i in range(number):
          n=input("enter name of actor",i,": ")
          actor=Actor(n)
          list.append(actor)

      media=Media(name,di,Imdb,url,du,list,t)
      return media
    

    def showInfo(self):
       print("name: ",self.name)
       print("director: ",self.director)
       print("IMDB score: ",self.IMDB_score)
       print("url: ",self.url)
       print("duration: ",self.duration)
       for self.cast in self.casts:
          print(self.cast.show_name())

    def download(self):
       ...


    
        