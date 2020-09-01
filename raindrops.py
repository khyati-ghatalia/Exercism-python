def convert(number):
    result_string=""
    num_tuple=(3,5,7)
    str_tuple=("Pling","Plang","Plong")

    for i in range(len(num_tuple)):
        if number%num_tuple[i]==0:
            result_string+=str_tuple[i]

    if result_string=="":
        return str(number)
    else:
        return result_string
    
