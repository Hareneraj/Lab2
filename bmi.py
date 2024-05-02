def calculate_bmi(height,weight):  
    print("Height=" +str(height))
    print("Weight=" +str(weight))
    bmi = weight/(height*height)
    print("bmi=" +str(bmi))

    if bmi<18.5:
        print("bmi_range= under weight")
        return -1
    elif bmi >18.5 and bmi <=25.0:
        print("bmi_range= normal weight")
        return 0
    elif bmi>25.0:
        print("bmi_range= over weight")
        return 1
       
calculate_bmi(weight=57,height=1.73)