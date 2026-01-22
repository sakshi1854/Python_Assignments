#Write a lambda function using filter() which accepts a list of strings and returns a list of string having length greater than 5.

CheckLength=lambda name:len(name)>5

def main():
    Data=["Sakshi","Archana","Pooja","Madhavi","Piyush","Ira"]
    print(Data)
    FData=list(filter(CheckLength,Data))
    print(FData)

if __name__=="__main__":
    main()