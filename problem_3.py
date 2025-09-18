num = input("Enter Cell Number: ")

if len(num) != 11:
    print("Invalid cell number")

elif not num.startswith != "09":
    print("Not Philippines Number. ")

else:
    prefix = num[:4]
    if prefix in ["0913", "0914", "0920", "0921", "0928", "0929", "0930"]:
        print("Your network is Smart")
    elif prefix in ["0909", "0910", "0911","0912","0918","0919"]:
        print("Your network is TNT")
    elif prefix in ["0922","0923","0932","0933"]:
        print("Your network is Sun")
    elif prefix in ["0915","0916","0917","0925","0926","0927"]:
        print("Your network is Globe")
    elif prefix in ["0903","0904","0905","0906","0907"]:
        print("Your network is TM")
    elif prefix in ["0901","0902","0924"]:
        print("Your network is Red")
    elif prefix in ["0991","0992","0993","0994","0995","0996","0997","0998"]:
        print("Your network is Dito")