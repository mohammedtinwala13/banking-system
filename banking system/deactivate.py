 # Deactivate account
import os
import global_var
import otp

def deactivate():
        os.system('cls')
        while True:
            print("account deactivation :- ")
            try:
                deac_acc = int(input("\n\n Enter the account number you want to deactivate :   "))
            except:
                print("enter correct account number")
                continue

            if deac_acc in global_var.accs:
                print("\n Confirm holder name as = ", global_var.accs[deac_acc]["holder"])
                
                try:
                    choicedeac = int(input("\n Enter 1 to confirm or 2 for wrong entry\n"))
                        
                except:
                    print("please enter correct choice")
                    continue

                if choicedeac == 1:
                    print("\n Holder name = ", global_var.accs[deac_acc]["holder"], \
                          "\n current balance = ", global_var.accs[deac_acc]["balance"])
                    
                    c=0
                    for i in range(5):
                        otpp = otp.generate_otp()
                        otp.send_otp_email(global_var.accs[deac_acc]["email"], otpp)
                        print("OTP sent to your email")
                        if otp.verify_otp(otpp):
                            print("OTP verified successfully")            
                            if global_var.accs[deac_acc]["balance"] > 0:
                                if global_var.accs[deac_acc]["activation"] == False:
                                    print("--account has already been deactivated and cannot be deactivated further--")
                                    break
                                else:
                                    print("account has balance and cannot be deactivated \n please withdraw all balance first")
                                    break
                            else:
                                global_var.accs[deac_acc]["activation"] = False
                                print("account number = ", deac_acc,\
                                      "\n successfully deactivated ")
                                break
                        else:
                            print("Invalid OTP")
                            c+=1
                            print("attempts remaining = ", 5-c)
                            if c == 5:
                                print("blocked - try again")
                                break
                    break
                else:
                    print("enter acc number again")

        Enter_to_exit = input("\n Press Enter to continue")

