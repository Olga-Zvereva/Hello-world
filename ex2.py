class Robot2:
    
    def __init__(self, name=None, build_year=None):
        self.__name = name
        self.__build_year=build_year	
	        
    def say_hi(self):
        if self.__name:
            print("Здравствуйте, Я - " + self.__name)
        else:
            print("Здравствуйте, Я - просто робот")
        if self.__build_year:
            print("Меня создали в " + str(self.__build_year))
        else:
            print("Я не знаю, когда меня создали!")

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name     
   
    @property
    def build_year(self):
        return self.__build_year    
    
    @build_year.setter 
    def build_year(self, by):
        self.__build_year = by       
  
x=Robot2('Marvin', 1979)
x.say_hi()
print(x.name)
print("Второй робот:")
y=Robot2()
y.name="Федор"
print(y.name)


