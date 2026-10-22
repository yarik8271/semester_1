from scipy import stats

def run_scipy():
    res = stats.describe([1, 2, 3, 4, 5])
    return f'SciPy Describe Mean: {res.mean}'
