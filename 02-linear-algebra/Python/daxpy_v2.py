import numpy as np
from time import time
def daxpy(a:float, x:list[float], y:list[float],fnumpy:bool =True):
    N = len(x)
    assert N == len(y), f"x and y must have the same dimension ({N}!={len(y)})"
    print(f"Initiating computation...")
    stime = time()
    if fnumpy:
        x = np.array(x)
        y = np.array(y)
        d = a*x+y
    else:
        d = [a*x[it]+y[it] for it in range(N)]
    print(f"Computation concluded in {time()-stime} seconds!")
    return d

if __name__ == "__main__":
    dims = [10,int(1e6),int(1e8)]
    a = 3
    x_val = 0.1
    y_val = 7.1
    print("Benchmarking without numpy:\n")
    for N in dims:
        print(f"N = {N}")
        x = [x_val for it in range(N)]
        y = [y_val for it in range(N)]
        res = daxpy(a,x,y,fnumpy=False)
        assert all(abs(component - 7.4)<1e-6 for component in res), f"{res[0]} != 7.4"
        print('\n')
    print("Benchmarking with numpy:\n")
    for N in dims:
        print(f"N = {N}")
        x = [x_val for it in range(N)]
        y = [y_val for it in range(N)]
        res = daxpy(a,x,y)
        assert all(abs(component - 7.4)<1e-6 for component in res), f"{res[0]} != 7.4"
        print('\n')
    