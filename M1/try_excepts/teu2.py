def sichere_division(a, b):
    try:
        return a / b 


    except ZeroDivisionError:
        print("Teilen durch 0 ist leider nicht möglich")


div = sichere_division(10, 2)
div2 = sichere_division(10, 0)

print(div, div2)
