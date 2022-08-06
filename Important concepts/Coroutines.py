def searcher():
    import time
    names = ["Amaan","Shaurya","Hasnain","Altamash","Irshad"]
    time.sleep(4)

    while True:
        text = (yield)
        if text in names:
            print("Your name exists")
        else:
            print("your name doesn't exists")

search=searcher()
print("Search started")
next(search)
print("Next method run")
search.send("Amaan")
input(" Press any key")
search.send("Shaurya")
input("Press any key")
search.send("Hasnain")
input("Press any key")
search.close()