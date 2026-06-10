import os
import global_var
import otp

def balance():
        os.system('cls')

        while True:
            print("accunt balance checking :-")
            try:
                search_acc = int(input("\n \n Enter the account number you want to search balance for :   "))
            except:
                print("enter correct account number")
                continue
            
            if search_acc in global_var.accs:

                print("\n Confirm holder name as = ", global_var.accs[search_acc]["holder"])

                choiceb = int(input("\n Enter 1 to confirm \n"  \
                                "2 for wrong entry\n"))
                
                if choiceb == 1:
                    c=0
                    for i in range(5):
                        otpp = otp.generate_otp()
                        otp.send_otp_email(global_var.accs[search_acc]["email"], otpp)
                        print("OTP sent to your email")
                        if otp.verify_otp(otpp):
                            print("OTP verified successfully")            
                            print("\n Holder name = ", global_var.accs[search_acc]["holder"], \
                                    "\n current balance = ", global_var.accs[search_acc]["balance"])
                            break
                        else:
                            print("Invalid OTP")
                            c+=1
                            print("attempts remaining = ", 5-c)
                            if c == 5:
                                print("blocked - try again")
                                break
                    if global_var.accs[search_acc]["activation"] == False:
                        print("--account has been deactivated and cannot be used further--")
                    break
                else:
                    continue
            else:
                print("\n account number not found")

        Enter_to_exit = input("\n Press Enter to continue")