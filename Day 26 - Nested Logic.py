date_of_return = str(input())
return_date = str(input())
date_of_return = date_of_return.split(" ")
return_date = return_date.split(" ")
if int(date_of_return[2]) > int(return_date[2]):
    print(10000)
elif int(date_of_return[1]) > int(return_date[1]):
    print (str((int(date_of_return[1]) - int(return_date[1])) * 500))
elif int(date_of_return[0]) > int(return_date[0]):
    print (str((int(date_of_return[0]) - int(return_date[0])) * 15))
else:
    print("error")