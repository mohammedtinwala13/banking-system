
import os 
import acc_creation
import balance
import deposit
import withdrawal
import transfer
import deactivate
import makefile
import global_var


Enter_to_exit = input("Press Enter to continue")
ch = 0
while ch!=7:
    os.system('cls')
    print("\n\n Bank Account Management Software: \n" \
    "1: create account \n" \
    "2: Check Account Balance\n" \
    "3: Deposit Money \n" \
    "4: Withdrawal \n" \
    "5: Transfer to other account \n"\
    "6: Deactivate account \n" \
    "7: EXIT \n" \
    "--enter choice-- \n")

    try: 
        ch = int(input(""))
    except: 
        print("please enter a valid number \n")
        continue
    
    if ch == 1:

        acc_creation.acc_creation()
        
    elif ch == 2:
        
        balance.balance()

    elif ch == 3:
        
        deposit.deposit()

    elif ch == 4:
        
        withdrawal.withdrawal()
    
    elif ch == 5:

        transfer.transfer()
                
    elif ch == 6:

       deactivate.deactivate()
    elif ch == 7:
        print("--Runtime Terminated--\n\n")
    
    else:
        print("Invalid input given, please enter again")

global_var.final_summary()

makefile.export_json()