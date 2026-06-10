# withdraw money
import os
import global_var
import log_csv
import otp

def withdrawal():
        os.system('cls')
        while True:
            print("withdrawal :-")
            try:
                w_acc = int(input("\n\n Enter the account number you want to withdraw amount in :   "))
            except:
                print("enter correct account number")
                continue

            if w_acc in global_var.accs:

                print("\nConfirm holder name =", global_var.accs[w_acc]["holder"])

                choicew = input("\nEnter 1 to confirm\nEnter 2 for wrong entry\n")

                if choicew == "1":

                    if global_var.accs[w_acc]["activation"] == False:
                        print("--Account has been deactivated--")
                        print("--contact bank for withdrawal in this acc--")
                        break

                    print("\nHolder name =", global_var.accs[w_acc]["holder"])
                    print("Current balance =", global_var.accs[w_acc]["balance"])

                    # OTP Step
                    c=0
                    for i in range(5):
                        otpp = otp.generate_otp()
                        otp.send_otp_email(global_var.accs[w_acc]["email"], otpp)

                        if otp.verify_otp(otpp):
                            try:
                                w_amt = float(input("Enter amount to withdraw: "))

                                if w_amt > 0 and  w_amt <= global_var.accs[w_acc]["balance"]:
                                    global_var.accs[w_acc]["balance"] -= w_amt
                                    print("final balance after withdrawal  =  ", global_var.accs[w_acc]["balance"])
                                    log_csv.log_to_csv(w_acc, "Withdrawal", w_amt, global_var.accs[w_acc]["balance"])
                                    break

                                else:
                                    print("withdrawal should be above 0 and above the balance in account ")
                                    break

                            except ValueError:
                                print("Enter amount in numbers")
                        else:
                            print("Invalid OTP")
                            c+=1
                            print("attempts remaining = ", 5-c)
                            if c == 5:
                                print("blocked - try again")
                                break
                    break
                else:
                    print("Enter details again")
                    continue

            else:
                print("Account number not found")

        Enter_to_exit = input("\nPress Enter to continue")
