import sqlite3

class Split :
    table = ''' 
CREATE TABLE IF NOT EXISTS split_table(
id  INT PRIMARY KEY NOT NULL,
name  TEXT   NOT NULL,
money REAL   NOT NULL
)
    '''

    def __init__(self):
        self.con = sqlite3.connect('split.db')
        self.cur = self.con.cursor()
        self.cur.execute(self.table)
        # self.enter_tarakonesh()
        # self.show_data()
        self.debtor_payer_list()
        
        

    
    def enter_tarakonesh(self):
        while (insert := input('Do you want to insert transaction : ') != 'no'):
            print(id := len(self.cur.execute('SELECT * FROM split_table').fetchall())+1) 
            self.id = id
            self.payer = input('Enter name of the payer : ')
            self.cost = float(input('Enter the cost : ')) 
            self.contribute = int(input('Enter the number of person evolve :  '))
            self.portion = self.cost / self.contribute
            self.enter_check_payer()
            

            for i in range (self.contribute-1):
                self.id += 1
                self.person = input('Enter the name : ')
                self.enter_check_debtor()

            if (qestion := input("continue yes/no ? ")) != 'no':...
            else:
                break

        
    def show_data(self):
        if (show := input('Do you want to see data base : ') != 'no'):
            self._show = self.cur.execute(' SELECT * FROM split_table').fetchall()
            for row in self._show :
                print(row)


    def enter_check_payer(self):
        exist = self.cur.execute('SELECT id,money FROM split_table WHERE name = ? ',(self.payer,)).fetchone()
        
        if exist : 
            updated_money = exist[1] + (self.portion * (self.contribute-1))
            self.cur.execute('UPDATE split_table SET money = ? WHERE id = ? ',(updated_money,exist[0]))

        else : self.cur.execute('INSERT INTO split_table VALUES (?,?,?)',(self.id, self.payer, self.portion * (self.contribute-1)))


    def enter_check_debtor(self):
        exist = self.cur.execute('SELECT id,money FROM split_table WHERE name = ? ',(self.person,)).fetchone()
        
        if exist : 
            updated_money = exist[1] + (-(self.portion))
            self.cur.execute('UPDATE split_table SET money = ? WHERE id = ? ',(updated_money,exist[0]))

        else : self.cur.execute('INSERT INTO split_table VALUES (?,?,?)',(self.id, self.person, -(self.portion)))

    def debtor_payer_list(self):
        self.payer_list = self.cur.execute('SELECT name,money FROM split_table WHERE money > 0').fetchall()
        self.payer_list.sort(key = lambda x : x[1], reverse=True)

        self.debtor_list = self.cur.execute('SELECT name,money FROM split_table WHERE money < 0').fetchall()
        self.debtor_list.sort(key = lambda x : x[1])
        print(self.payer_list)
        print(self.debtor_list)

    def balance(self): 
        # while True:
        for m in range (10):
            for i in range(len(self.payer_list)) : 
                money_payer = self.payer_list[i][1]
                if money_payer == 0 :
                    print(f'{self.money_payer[i][0]} is balanced. ')
                    self.payer_list.pop(i)

            for j in range(len(self.debtor_list)) : 
                money_debtor = self.debtor_list[j][1]
                if money_debtor == 0 :
                    print(f'{self.money_debtor[j][0]} is balanced. ')
                    self.debtor_list.pop(j)

                      
            # for person_payer in self.payer_list: 
            #     self.money_payer = person_payer[1] 

            #     for person_debtor in self.debtor_list: 
            #         self.money_debtor = person_debtor[1]

            #         if self.money_payer == -(self.money_debtor) :
            #             person_payer[1] = 0
            #             person_debtor[1] = 0
            #             print(f"{person_debtor[0]} to {person_payer[0]} : {self.money_payer}")



        
                    

    def pardakht(self):
        who_pay = input('Enter the payer : ')
        who_recieve = input('enter the reciever : ')
        amount = float(input('Enter the money : '))

        who_pay_money = self.cur.execute('SELECT money FROM split_table WHERE name = ? ',(who_pay,)).fetchone()
        who_recieve_money = self.cur.execute('SELECT money FROM split_table WHERE name = ? ',(who_recieve,)).fetchone()
        print(who_pay_money)
        print(who_recieve_money)

        self.cur.execute('UPDATE split_table SET money = ? WHERE name = ? ',((who_pay_money[0]+amount),who_pay))
        self.cur.execute('UPDATE split_table SET money = ? WHERE name = ? ',((who_recieve_money[0]-amount),who_recieve))





    def end(self):
        self.con.commit() 
        self.con.close()



amirSplit = Split()

# amirSplit.enter_tarakonesh()
amirSplit.balance()
# amirSplit.pardakht()
amirSplit.show_data()
amirSplit.end()
