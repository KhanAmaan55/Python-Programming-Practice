def printing(*arr,**karry):
    """
    practicing *args and **kwargs
    """
    for items in arr:
        print(items)
    for key,value in karry.items():
        print(f"{key} is a {value}")


arr=["music","Dance","reading","singing","party"]
krt={"shaurya":"business","hasnain":"sleep","altamash":"Programmer","irshad":"Architect","sangam":"P.Engineer"}
printing(*arr,**krt)