#AUTHOR: PIYUSH SHARMA
#DATE: JANUARY 27, 2019
#DATABASE TO CSV PARSER

import sqlite3
import os
import csv

def main():

    #Initialization messages
    print('[+] Initializing DBParser by Piyush Sharma...')
    

    #Define file paths
    db_path = 'DATABASE FILE PATH'
    csv_path = 'CSV FILE PATH'

    #connect to the database
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    #create csv file object and open in write mode
    csv_file = open(csv_path, 'w')

    #initialize writer object to write to the csv file
    csv_writer = csv.writer(csv_file)
    
    #execute command
    student_info = c.execute('SELECT * FROM YOUR_TABLE_HERE;').fetchall()
    
    
    print('[+] Writing Database rows to CSV file')

    #Write to the csv file
    for i in student_info:
        csv_writer.writerow(i)


    #Finished
    print('[+] FINISHED! CSV file is now ready for use.')
    
    
#Call main function
main()
