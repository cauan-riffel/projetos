class test:
  def __init__(self) -> None:
    pass

a:dict[int,test]={}

a[1]=test()
a[13]=test()
print(a)
