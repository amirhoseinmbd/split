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
        self._list = []
        self.con = sqlite3.connect('split.db')
        self.cur = self.con.cursor()
        self.cur.execute(self.table)
        Split.enter_tarakonesh(self)
        Split.show_data(self)
        self.con.commit() 
        self.con.close()
        

    
    def enter_tarakonesh(self):
        while True:
            print(id := len(self.cur.execute('SELECT * FROM split_table').fetchall())+1) 
            self.id = id
            self.payer = input('Enter name of the payer : ')
            self.cost = float(input('Enter the cost : ')) 
            self.contribute = int(input('Enter the number of person evolve :  '))
            self.portion = self.cost / self.contribute

            self.cur.execute('INSERT INTO split_table VALUES (?,?,?)',(self.id, self.payer, self.portion * (self.contribute-1)))

            for i in range (self.contribute-1):
                self.id += 1
                self.person = input('Enter the name : ')
                self.cur.execute('INSERT INTO split_table VALUES (?,?,?)',(self.id, self.person, -(self.portion)))
            if (qestion := input("continue yes/no ? ")) != 'no':...
            else:
                break

        
    def show_data(self):
        if (show := input('Do you want to see data base : ') != 'no'):
            self._show = self.cur.execute(' SELECT * FROM split_table').fetchall()
            for row in self._show :
                print(row)


    def create_group(self):...

Split()