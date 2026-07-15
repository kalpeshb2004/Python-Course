# Ye threading module ka hi ek advanced/easy version hai. Manual Thread(), start(), join() baar-baar likhne ki jagah, ThreadPoolExecutor khud thread manage karta hai — tumhe bas batana hai kitne threads chahiye aur konsa function chalana hai.

from concurrent.futures import ThreadPoolExecutor
import time

def task(name):
    print(f"{name} start")
    time.sleep(2)
    print(f"{name} done")
    return f"{name} finished"

with ThreadPoolExecutor(max_workers=3) as executer:
    result = executer.map(task, ["thread-1","thread-2","thread-3"])

print("all done")

