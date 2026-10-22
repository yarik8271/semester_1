from func_builtin_1 import run_math
from func_builtin_2 import run_datetime
from func_builtin_3 import run_random
from func_builtin_4 import run_json
from func_builtin_5 import run_os

from func_ext_1 import run_requests
from func_ext_2 import run_numpy
from func_ext_3 import run_pandas
from func_ext_4 import run_pillow
from func_ext_5 import run_matplotlib
from func_ext_6 import run_scipy
from func_ext_7 import run_sympy
from func_ext_8 import run_colorama
from func_ext_9 import run_tqdm
from func_ext_10 import run_art

def main():
    print("=== Built-in Libraries ===")
    print(run_math())
    print(run_datetime())
    print(run_random())
    print(run_json())
    print(run_os())

    print("\n=== External Libraries ===")
    print(run_requests())
    print(run_numpy())
    print(run_pandas())
    print(run_pillow())
    print(run_matplotlib())
    print(run_scipy())
    print(run_sympy())
    print(run_colorama())
    print(run_tqdm())
    print(run_art())

if __name__ == "__main__":
    main()
