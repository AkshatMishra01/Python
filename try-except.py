try:
    open("D:\file4.txt","r")
except IOError:
    print("IOerror present")
except:
    print("An another error occured")
finally:
    print("File opened")

