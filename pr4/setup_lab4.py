import os

files_content = {
    # 5 вбудованих
    "func_builtin_1.py": "import math\n\ndef run_math():\n    return f'Square root of 144 is {math.sqrt(144)}'\n",
    "func_builtin_2.py": "from datetime import datetime\n\ndef run_datetime():\n    return f'Current time: {datetime.now().strftime(\"%Y-%m-%d %H:%M:%S\")}'\n",
    "func_builtin_3.py": "import random\n\ndef run_random():\n    return f'Random dice roll: {random.randint(1, 6)}'\n",
    "func_builtin_4.py": "import json\n\ndef run_json():\n    data = {'lab': 4, 'status': 'completed'}\n    return json.dumps(data)\n",
    "func_builtin_5.py": "import os\n\ndef run_os():\n    return f'Current directory: {os.getcwd()}'\n",
    # 10 невбудованих
    "func_ext_1.py": "import requests\n\ndef run_requests():\n    response = requests.get('https://httpbin.org/get')\n    return f'HTTP Status Code: {response.status_code}'\n",
    "func_ext_2.py": "import numpy as np\n\ndef run_numpy():\n    arr = np.array([1, 2, 3, 4, 5])\n    return f'NumPy Array Mean: {np.mean(arr)}'\n",
    "func_ext_3.py": "import pandas as pd\n\ndef run_pandas():\n    df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})\n    return f'Pandas Shape: {df.shape}'\n",
    "func_ext_4.py": "from PIL import Image\n\ndef run_pillow():\n    img = Image.new('RGB', (100, 100), color='red')\n    return f'Image Mode: {img.mode}, Size: {img.size}'\n",
    "func_ext_5.py": "import matplotlib\n\ndef run_matplotlib():\n    return f'Matplotlib Version: {matplotlib.__version__}'\n",
    "func_ext_6.py": "from scipy import stats\n\ndef run_scipy():\n    res = stats.describe([1, 2, 3, 4, 5])\n    return f'SciPy Describe Mean: {res.mean}'\n",
    "func_ext_7.py": "import sympy as sp\n\ndef run_sympy():\n    x = sp.Symbol('x')\n    expr = sp.diff(x**2 + 3*x, x)\n    return f'SymPy Derivative of x^2 + 3x: {expr}'\n",
    "func_ext_8.py": "from colorama import Fore, Style\n\ndef run_colorama():\n    return f'{Fore.GREEN}Colorama Output: Success!{Style.RESET_ALL}'\n",
    "func_ext_9.py": "from tqdm import tqdm\nimport time\n\ndef run_tqdm():\n    for _ in tqdm(range(5), desc='Processing'):\n        time.sleep(0.01)\n    return 'tqdm loop finished'\n",
    "func_ext_10.py": "from art import text2art\n\ndef run_art():\n    return text2art('Lab 4')\n",
    # Точка входу
    "main.py": """from func_builtin_1 import run_math
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

    print("\\n=== External Libraries ===")
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
"""
}

for filename, code in files_content.items():
    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)

print("Усі 16 файлів успішно створено!")