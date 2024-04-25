def main():
    print("ET0735 (DevOps FOR AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    float_list = get_user_input()
    int_list = get_user_input2(float_list)
    print(float_list)
    
    Average = calc_average_temp(float_list)
    print("Average is" +str(Average))
    Minimum, Maximum = calc_min_and_max_temp(int_list)
    result_list = max_min_result(Maximum, Minimum)
    print("Maximum and Minimum are" +str(result_list))

    
def display_main_menu():
    print("enter commands separately by a comma eg. 5,67,32")
    

def get_user_input():
    user_input = input("Enter numbers:")
    num_list = user_input.split(",")
    float_list = [float(item) for item in num_list]
    return float_list
    

def get_user_input2(float_list):
    int_list = list(map(int, float_list))
    return int_list

def calc_average_temp(float_list):
    list_length = len(float_list)
    total_sum = sum(float_list)
    average = total_sum/ list_length
    return average

def calc_min_and_max_temp(int_list):
    Minimum = min(int_list)
    Maximum = max(int_list)
    return Minimum, Maximum

def max_min_result(Maximum, Minimum):
    result_list = [Maximum, Minimum]
    return result_list
    
    
    


if __name__=="__main__":
    main()
