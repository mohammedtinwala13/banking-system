ch = 0
accs = {}
import makefile
from pprint import pprint 
accs = makefile.import_json()

if accs:
    # Find the biggest key and add 1
    new_acc_no = max(accs.keys()) + 1
else:
    # First time running the app? Start at 1001
    new_acc_no = 1001
print(accs)
def final_summary():
    print("final accounts summary \n\n ")
    pprint(accs, indent = 4)


