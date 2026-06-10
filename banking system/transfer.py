import os
import global_var
import otp        
import log_csv

def transfer():
        os.system('cls')
        while True: 
            print("\n--- Transfer Money ---")

            try:
                trans1_acc = int(input("Enter Sender Account Number (or 0 to go back): "))
                if trans1_acc == 0: break
                
                if trans1_acc not in global_var.accs or not global_var.accs[trans1_acc]["activation"]:
                    print("Error: Sender account not found or deactivated.")
                    break 
                
                trans2_acc = int(input("Enter Recipient Account Number: "))
                if trans2_acc not in global_var.accs or not global_var.accs[trans2_acc]["activation"]:
                    print("Error: Recipient account not found or deactivated.")
                    continue

                if trans1_acc == trans2_acc:
                    print("Error: Cannot transfer to the same account.")
                    continue

                trans_amt = float(input(f"Enter Amount to transfer from {global_var.accs[trans1_acc]['holder']}: "))
                
                
                c=0
                for i in range(5):
                        otpp = otp.generate_otp()
                        otp.send_otp_email(global_var.accs[trans1_acc]["email"], otpp)
                        print("OTP sent to your email")

                        if otp.verify_otp(otpp):
                            print("OTP verified successfully")            

                            print("\n Holder name = ", global_var.accs[trans1_acc]["holder"], \
                                    "\n current balance = ", global_var.accs[trans1_acc]["balance"])
                            
                            if trans_amt > global_var.accs[trans1_acc]["balance"]:
                                print(f"Insufficient funds! Balance: {global_var.accs[trans1_acc]['balance']}")
                                break
                            elif trans_amt <= 0:
                                print("Amount must be positive.")
                                break
                            else:
                                global_var.accs[trans1_acc]["balance"] -= trans_amt
                                global_var.accs[trans2_acc]["balance"] += trans_amt
                                print(f"Transfer Successful! {trans_amt} sent to {global_var.accs[trans2_acc]['holder']}")

                                log_csv.log_to_csv(trans2_acc, f"Transfer from {trans1_acc}", trans_amt, global_var.accs[trans2_acc]["balance"])
                                break 
                            
                        else:
                            print("Invalid OTP")
                            c+=1
                            print("attempts remaining = ", 5-c)
                            if c == 5:
                                print("blocked - try again")
                                break
                break
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        Enter_to_exit = input("\n Press Enter to continue")
