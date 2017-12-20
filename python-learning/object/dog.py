class Dog:
    def __init__(self,name,month,day,year,sparkText):
        self.name = name
        self.month = month
        self.day = day
        self.year = year
        self.sparkText = sparkText
    
    def speak(self):
        return self.sparkText

    def getName(self):
        return self.name

    def getBirthday(self):
        return self.day + '/' + self.month + '/' + self.year

    def __add__(self,otherDog):
        return Dog("Puppy of " + self.name + " and " + otherDog.name,self.day,self.month,self.year + 1,self.sparkText)

def main():
    boyDog = Dog('Mesa',5,1,2018,'Barbar')
    girlDog = Dog('LiLi',1,12,2017,'Wangwang')

    print(boyDog.getName())
    bg = boyDog + girlDog
    print(bg.getName())


if __name__ == '__main__':
    main()



