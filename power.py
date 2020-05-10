import time
import math

def calc_power_rec(x, y):
    
    if y == 0:
        return 1
    if (y % 2 == 0):
        z = calc_power_rec(x, y/2)
        return z * z
    else:
        return x * calc_power_rec(x,y-1)
    
def calc_power_sys(x, y):
    return math.pow(x,y)
    

def power_calculation(x, y):
    start_time = time.time()
    print(calc_power_rec(x,y))
    elapsed_time = time.time() - start_time
    print("Time taken for execution using recursion with radix: "+str(x)+" and power :"+str(y)+" is: "+str(elapsed_time))
    print("\n")
    start_time = time.time()
    print(calc_power_sys(x,y))
    elapsed_time = time.time() - start_time
    print("Time taken for execution using system with radix: "+str(x)+" and power :"+str(y)+" is: "+str(elapsed_time))

if __name__ == "__main__":
    power_calculation(2,10000)
