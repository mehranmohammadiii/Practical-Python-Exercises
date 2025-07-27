class My_Exception_Handling(Exception) :
    def __init__(self,message):
        super().__init__(message)
        self.__message=message
    def __str__(self):
        return 'EROR is : '+ self.__message+'...'
# -------------------------------------------------------------------------------
class Player() :
    def __init__(self,playercode,age,height,wight):
        self.__Playerode=playercode
        self.__Age=age
        self.__Height=height
        self.__Wight=wight
    
    def __WeightValidation(self) :
        if  Player.__CheckFloat(self.__Wight) :
            if Player.__CheckInteger(self.__Age) :
                self.__Age=int(self.__Age)
                self.__Wight=float(self.__Wight)
                if self.__Age>=15 and self.__Age<=25 :
                    if self.__Wight >=60 and self.__Wight <=80 :
                        return True
                    else : raise My_Exception_Handling('Weight out of range This person is not allowed to register')
                elif self.__Age>25 and self.__Age<=35 :
                    if self.__Wight >=50 and self.__Wight <=75 :
                        return True
                    else : raise My_Exception_Handling('Weight out of range This person is not allowed to register')
                else : raise My_Exception_Handling('Age out of range This person is not allowed to register')
            else : raise My_Exception_Handling('Age is not valid')
        else : raise My_Exception_Handling('Weight is not valid')

    def __HeightValidation(self) :
        if Player.__CheckInteger(self.__Height) :
            self.__Height=int(self.__Height)
            if self.__Height>=170 and self.__Height<=190 :
                return True
            raise My_Exception_Handling('Height out of range This person is not allowed to register')
        else : raise My_Exception_Handling('Height is not valid')

    @staticmethod
    def __CheckFloat(Weight) :
        try :
            float(Weight)
            return True
        except :
            return False

    @staticmethod
    def __CheckInteger(Height_Age) :
        try :
            int(Height_Age)
            return True
        except :
            return False

    def RegisterPlayer(self) :
        try :
            self.__WeightValidation()
            self.__HeightValidation()
            return True
        except My_Exception_Handling as e:
            print(e)
    def __str__(self):
        return f'{self.__Playerode}\t{self.__Age}\t{self.__Height}\t{self.__Wight}'
# -------------------------------------------------------------------------------
Playerlist=[]
x=1
while x!=0 :
    playercode=input('Player Code is : ')
    weight=input('Weight is : ')
    age=input('Age is : ')
    height=input('Height is : ')
    Players=Player(playercode,age,height,weight)
    if Players.RegisterPlayer() :
        Playerlist.append(Players)
    x=int(input('0 or 1 :'))

for item in Playerlist:
    print(item)