def first_1():
    numb1 = 2
    numb2 = 2

    if numb1 == numb2:
        print ("Hurra")
    else:
        print ("nicht huure")

    f = open("guru99.txt", "w+")
    f.write("second line")
    f.close()

def main():
    first_1()

if __name__=="__main__":
    main()

