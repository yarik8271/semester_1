from tqdm import tqdm
import time

def run_tqdm():
    for _ in tqdm(range(5), desc='Processing'):
        time.sleep(0.01)
    return 'tqdm loop finished'
