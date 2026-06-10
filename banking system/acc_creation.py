import os
import global_var
import otp
import log_csv
# create acc
def acc_creation():
    os.system('cls')
    c = 0
    while True:
            print("accunt creation :-")
            
            name = input("enter name\n")
            email = input("enter email for contact\n")
            re_email = input("enter email again for verification\n")
            if email == re_email:
                try:
                    balance = float(input("\n enter opening balance\n"))
                    if balance >0:
                        try:
                            print("\n\n new account details :"\
                                "\n name : ",name,\
                                "\n balance : ", balance, \
                                "\n email : ", email,\
                                "\n\n enter 1 to proceed, "\
                                "\n 2 to change details, \n")

                            choicecreate = int(input("Enter choice\n"))
                            if choicecreate == 1:
                                accs_add = {global_var.new_acc_no :{
                                    "acc_no" : global_var.new_acc_no,
                                    "holder" : name,
                                    "balance" : balance,
                                    "email" : email,
                                    "activation" : True
                                    }}
                                c=0
                                for i in range(5):
                                    otpp = otp.generate_otp()
                                    otp.send_otp_email(accs_add[global_var.new_acc_no]["email"], otpp)
                                    print("OTP sent to your email")
                                    if otp.verify_otp(otpp):
                                        print("OTP verified successfully")
                                        global_var.accs = global_var.accs | accs_add

                                        print("\n new account created success \n new acc number is = ", global_var.accs[global_var.new_acc_no]["acc_no"])

                                        log_csv.log_to_csv(global_var.new_acc_no, "Account Opened", balance, balance)
                                        global_var.new_acc_no += 1
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
                                continue
                                
                        except: 
                            print("\n error recorded -- please try again")
                            continue
                    else:
                        print("\n account cant be crated with negative or zero balance amount")
                        continue
                except: 
                    print("\n please enter balance as number format")
                    continue
            else:
                print("re-enter email - not matching,")
                x = input("enter to continue - press 0 to exit")
                if x == 0: break
                
    Enter_to_exit = input("Press Enter to continue")