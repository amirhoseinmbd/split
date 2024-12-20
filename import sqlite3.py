import sqlite3
from datetime import date

class Split :
    table = ''' 
CREATE TABLE IF NOT EXISTS split_table(
id  INT PRIMARY KEY NOT NULL,
name  TEXT   NOT NULL,
money REAL   NOT NULL
)
'''

    table2 = '''
CREATE TABLE IF NOT EXISTS history_table (
Payer TEXT  NOT NULL,
Cost   REAL   NOT NULL,
Date  TEXT    NOT NULL,
Debtor  TEXT   NOT NULL,
Describtion TEXT  
)

'''
    

    def __init__(self):
        self.con = sqlite3.connect('split.db')
        self.cur = self.con.cursor()
        self.cur.execute(self.table)
        self.cur.execute(self.table2)
        self.debtor_payer_list()
        # self.enter_tarakonesh()
        # self.show_data()
        
    
    def enter_tarakonesh(self):
       while (input('Do you want to insert transaction : ') != 'no'):
            try:
                self.id = len(self.cur.execute('SELECT * FROM split_table').fetchall())+1 
                self.payer = input('Enter name of the payer : ')
                self.cost = float(input('Enter the cost : ')) 
                self.contribute = int(input('Enter the number of person evolve :  '))
                self.describe = input('Description : ...')
                self.portion = self.cost / self.contribute
                self.enter_check_payer()
                    
                self.all = []
                for i in range (self.contribute-1):
                    self.id += 1
                    self.person = input('Enter the name : ')
                    self.all.append(self.person)
                    self.enter_check_debtor()

                print(self.all)
                self.allStr = ' , '.join(self.all)
                print(self.allStr)
                self.history()

            
            except ValueError : 
                print('Error! Enter right values') 
                continue

        
    def show_data(self):
        if (input('Do you want to see data base : ') != 'no'):
            self._show = self.cur.execute(' SELECT * FROM split_table').fetchall()
            for row in self._show :
                print(row)


    def enter_check_payer(self):
        exist = self.cur.execute('SELECT id,money FROM split_table WHERE name = ? ',(self.payer,)).fetchone()
        
        if exist : 
            updated_money = exist[1] + (self.portion * (self.contribute-1))
            self.cur.execute('UPDATE split_table SET money = ? WHERE id = ? ',(round(updated_money,3),exist[0]))

        else : self.cur.execute('INSERT INTO split_table VALUES (?,?,?)',(self.id, self.payer, round(self.portion * (self.contribute-1),3)))


    def enter_check_debtor(self):
        exist = self.cur.execute('SELECT id,money FROM split_table WHERE name = ? ',(self.person,)).fetchone()
        
        if exist : 
            updated_money = exist[1] + (-(self.portion))
            self.cur.execute('UPDATE split_table SET money = ? WHERE id = ? ',(round(updated_money,3),exist[0]))

        else : self.cur.execute('INSERT INTO split_table VALUES (?,?,?)',(self.id, self.person , round(-(self.portion),3)))


    def debtor_payer_list(self):
        self.payer_list = self.cur.execute('SELECT name,money FROM split_table WHERE money > 0').fetchall()
        self.payer_list.sort(key = lambda x : x[1], reverse=True)

        self.debtor_list = self.cur.execute('SELECT name,money FROM split_table WHERE money < 0').fetchall()
        self.debtor_list.sort(key = lambda x : x[1])
        


    def balance(self):
        while True:
            if len(self.debtor_list) == 0 : print('_____Now All are Balance_____') ; break

            else :
                for i in range(len(self.payer_list)) : 
                    money_payer = self.payer_list[i][1]
                    if money_payer == 0 :
                        self.payer_list.pop(i)

                for j in range(len(self.debtor_list)) : 
                    money_debtor = self.debtor_list[j][1]
                    if money_debtor == 0 :
                        self.debtor_list.pop(j)

                        
                for person_payer in self.payer_list: 
                    self.money_payer = person_payer[1] 

                    for person_debtor in self.debtor_list: 
                        self.money_debtor = person_debtor[1]

                        if self.money_payer == -(self.money_debtor) :
                            self.payer_list.pop(self.payer_list.index((person_payer[0],person_payer[1])))
                            self.debtor_list.pop(self.debtor_list.index((person_debtor[0],person_debtor[1])))
                            print(f"{person_debtor[0]} to {person_payer[0]} : {self.money_payer}")

                if len(self.debtor_list) == 0 : print('_____Now All are Balance_____') ;break

                else : 
                    if -(self.debtor_list[0][1]) > self.payer_list[0][1]:
                        print(f"{self.debtor_list[0][0]} to {self.payer_list[0][0]} : {self.payer_list[0][1]}")
                        remain = self.debtor_list[0][1] + self.payer_list[0][1]
                        self.debtor_list.append((self.debtor_list[0][0],remain))
                        self.debtor_list.pop(0)
                        self.payer_list.pop(0)


                    elif self.payer_list[0][1] > -(self.debtor_list[0][1]): 
                        print(f"{self.debtor_list[0][0]} to {self.payer_list[0][0]} : {-(self.debtor_list[0][1])}")
                        remain = self.payer_list[0][1] + self.debtor_list[0][1]
                        self.payer_list.append((self.payer_list[0][0],remain))
                        self.debtor_list.pop(0)
                        self.payer_list.pop(0)
                    
                    self.payer_list.sort(key = lambda x : x[1], reverse=True)
                    self.debtor_list.sort(key = lambda x : x[1])
                    

    def pardakht(self):
        who_pay = input('Enter the payer : ')
        who_recieve = input('enter the reciever : ')
        amount = float(input('Enter the money : '))

        who_pay_money = self.cur.execute('SELECT money FROM split_table WHERE name = ? ',(who_pay,)).fetchone()
        who_recieve_money = self.cur.execute('SELECT money FROM split_table WHERE name = ? ',(who_recieve,)).fetchone()
        
        self.cur.execute('UPDATE split_table SET money = ? WHERE name = ? ',((who_pay_money[0]+amount),who_pay))
        self.cur.execute('UPDATE split_table SET money = ? WHERE name = ? ',((who_recieve_money[0]-amount),who_recieve))

    def history(self):
        self.date = date.today()
        self.record_history = (self.payer, self.cost,self.date, self.allStr, self.describe)
        self.cur.execute('INSERT INTO history_table VALUES (?,?,?,?,?)',(self.record_history))

    def show_history(self):
        self.cur.row_factory = sqlite3.Row
        r = self.cur.execute('SELECT * FROM history_table')
        rows = r.fetchall()

        headers = [description[0] for description in self.cur.description]
        print(" | ".join(headers)) 
        
        for row in rows:
            print(' | ' .join(str(row[x]) for x in headers))
        
         

    def end(self):
        self.con.commit() 
        self.con.close()








amirSplit = Split()
# amirSplit.enter_tarakonesh()
# amirSplit.balance()
# amirSplit.pardakht()
# amirSplit.show_data()
amirSplit.show_history()
amirSplit.end()
