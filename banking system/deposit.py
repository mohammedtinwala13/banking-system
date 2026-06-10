# deposit money in acc
import os
import global_var
import otp
import log_csv

def deposit():
        os.system('cls')

        while True:
            print("deposit :-")

            try:
                dep_acc = int(input("\n\nEnter the account number you want to deposit amount in: "))
            except ValueError:
                print("Enter correct account number")
                continue

            if dep_acc in global_var.accs:

                print("\nConfirm holder name =", global_var.accs[dep_acc]["holder"])

                choiced = input("\nEnter 1 to confirm\nEnter 2 for wrong entry\n")

                if choiced == "1":

                    if global_var.accs[dep_acc]["activation"] == False:
                        print("--Account has been deactivated--")
                        break

                    print("\nHolder name =", global_var.accs[dep_acc]["holder"])
                    print("Current balance =", global_var.accs[dep_acc]["balance"])

            # OTP Step
                    c=0
                    for i in range(5):
                        otpp = otp.generate_otp()
                        otp.send_otp_email(global_var.accs[dep_acc]["email"], otpp)

                        if otp.verify_otp(otpp):
                            
                            try:
                                dep_amt = float(input("Enter amount to deposit: "))

                                if dep_amt > 0:
                                    global_var.accs[dep_acc]["balance"] += dep_amt

                                    log_csv.log_to_csv(dep_acc, "Deposit", dep_amt, global_var.accs[dep_acc]["balance"])

                                    print("Final balance =", global_var.accs[dep_acc]["balance"])
                                    break
                                else:
                                    print("Deposit should be above 0")

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