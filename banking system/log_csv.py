import os
import csv
from datetime import datetime

def log_to_csv(acc_id, action, amount, balance):
    folder = "C:/Users/mohammed/Desktop/DEKSTOP/college/python/banking system/account_logs"
    if not os.path.exists(folder):
        os.makedirs(folder)
        
    filename = f"{folder}/acc_{acc_id}.csv"
    file_exists = os.path.isfile(filename)
    
    # Define our columns
    headers = ['Timestamp', 'Action', 'Amount', 'Balance']
    
    # 'a' means append mode - it adds to the bottom without deleting
    with open(filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        
        # If the file is new, write the header first
        if not file_exists:
            writer.writeheader()
            
        # Write the transaction row
        writer.writerow({
            'Timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'Action': action,
            'Amount': f"{amount:.2f}",
            'Balance': f"{balance:.2f}"
        })
