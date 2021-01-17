date_of_return = str(input())
return_date = str(input())
date_of_return = date_of_return.split(" ")
return_date = return_date.split(" ")

delay = False
if int(date_of_return[2]) < int(return_date[2]):
    print(0)
    
elif int(date_of_return[2]) == int(return_date[2]):

    if int(date_of_return[1]) < int(return_date[1]):
        print(0)
    elif int(date_of_return[1]) == int(return_date[1]):

        if int(date_of_return[0]) <= int(return_date[0]):
            print(0)
        else:
            print ((int(date_of_return[0]) - int(return_date[0])) * 15)
        
    else:
        print ((int(date_of_return[1]) - int(return_date[1])) * 500)

else:
    print(10000)
