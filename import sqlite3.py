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
        for person_payer in self.payer_list: 
            self.money_payer = person_payer[1] 

            for person_debtor in self.debtor_list: 
                self.money_debtor = person_debtor[1]

                if self.money_payer == -(self.money_debtor) :
                    # p = self.payer_list.index(money)
                    # print(f"p is {p}")
                    # d = self.debtor_list.index(money)
                    # print(f"d is {d}")
                    print(f"{person_debtor[0]} to {person_payer[0]} : {self.money_payer}")
                    break





    def end(self):
        self.con.commit() 
        self.con.close()



amirSplit = Split()

# amirSplit.enter_tarakonesh()
amirSplit.show_data()
# amirSplit.balance()
amirSplit.end()
