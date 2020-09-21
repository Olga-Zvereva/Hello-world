class Robot1:
	pass
if __name__=='__main__':
    x=Robot1()
    y=Robot1()
    x1=x
    print(x1==x)
    print(x1==y)
    x.name='Федор'
    x.year=2019
    y.name='Marwin'
    y.year=1993
    Robot1.brand="UrFu"
    print(x.brand, y.brand, sep=' И ')
    print(x.__dict__)
    print(Robot1.__dict__)
    getattr(x, 'energy', 100)
    
