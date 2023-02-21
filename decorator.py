def decor_result(result_function):
    def distinction(marks):
        for m in marks:
            if m>=75:
                print("congraulation||you have got it")
        else:
            result_function(marks)
    return distinction
@decor_result
def  result(marks):
    for i in marks:
        if i>=33:
            pass
        else:
            print("fail")
            break
    else:
        print("pass")
result([38,46,89,70,45,78,60])
    