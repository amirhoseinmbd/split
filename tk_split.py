from tkinter import *
from tkinter import ttk
from main import Split
from tkinter import messagebox






def tab_change(event):
    selected_tab = my_notebook.index(my_notebook.select())
    if selected_tab == 1:
        refresh_balance()
   


#def_buttons___________________________________________________________________

#payment_button :

def PaymentEnter():
    sp = Split()
    sp.pardakht(payment_payer_en.get(),payment_recieve_en.get(),float(payment_money_en.get()))
    sp.end()
    
    payment_frame.config(bg="green3")
    payment_frame.after(100, lambda: payment_frame.config(bg="SystemButtonFace"))

    messagebox.showinfo('Operation','Done')
    
    payment_payer_en.delete(0, END)
    payment_recieve_en.delete(0, END)
    payment_money_en.delete(0, END)
    
#_________________________________________________________________________________

#transaction_button :

def group():
     global describe_entry, payer_entry, contribute, cost_entry , deb_list
    
     contribute = int(person_contribute.get())
     for widget in transaction_frame.winfo_children():
         widget.destroy()
 
     deb_list = []

     
     for i in range(contribute):
        if i == 0 : 
            payer_label = Label(transaction_frame, text="Payer : ",pady=5,font=('Aharoni',10))
            payer_label.grid(row=i, column=0, pady=5, padx=30)
            payer_entry = Entry(transaction_frame)
            payer_entry.grid(row=i, column=1, pady=5, padx=30)


            cost_label = Label(transaction_frame, text="Cost : ",pady=5,font=('Aharoni',10))
            cost_label.grid(row=i+1, column=0, pady=5, padx=30)
            cost_entry = Entry(transaction_frame)
            cost_entry.grid(row=i+1, column=1, pady=5, padx=30)



            describe_label = Label(transaction_frame, text="Describe : ",pady=5,font=('Aharoni',10))
            describe_label.grid(row=i+2, column=0, pady=5, padx=30)
            describe_entry = Entry(transaction_frame)
            describe_entry.grid(row=i+2, column=1, pady=5, padx=30)

        else : 
            debtor_label = Label(transaction_frame, text="Debtor {}: ".format(i),pady=5,font=('Aharoni',10))
            debtor_label.grid(row=i+2, column=0, pady=5, padx=30)
            debtor_entry = Entry(transaction_frame)
            debtor_entry.grid(row=i+2, column=1, pady=5, padx=30)
            if debtor_entry.get().strip():
                variable_name = f"var{len(deb_list) + 1}"  
                deb_list.append({variable_name: debtor_entry.get()})  # 
                print(f"Added: {variable_name} = {debtor_entry.get()}")

        

        
     
        

           
     save_button = Button(transaction_frame, text="Save names", command=save)
     save_button.grid(row=contribute+3, columnspan=2, pady=10, padx=50)


# enter_tarakonesh(self,payer,cost,contribute,describe):




def save ():
    print(payer_entry.get())
    print(int(cost_entry.get()))
    print(contribute)
    print(describe_entry.get())
    print(len(deb_list))
    for i in deb_list : 
        print(i)
    
    payer = payer_entry.get()
    cost = int(cost_entry.get())
    describe = describe_entry.get()
     
    #  sp = Split()
    #  sp.enter_tarakonesh(payer,cost, contribute , describe, deb_list)
     
    #  for widget in transaction_frame.winfo_children():
    #      widget.destroy()


     
#__________________________________________________________________________________________________

#balance_tab 

def refresh_balance():

    for widget in balance_frame.winfo_children():
        widget.destroy()

    lbl_balance = Label(balance_frame, text ='Balance : ')
    lbl_balance.grid(row=0, column=0)

    sp = Split()
    balance = sp.balance()
    line = 1
    for tranaction in balance : 
        Label(balance_frame, text = tranaction).grid(row=line, column=0)
        line += 1
    sp.end()

#______________________________________________________________________________________________















root =Tk()
root.title('Split App')
root.geometry('500x400')
root.resizable(width=False, height=False)
root.iconbitmap('mytk.ico')

my_notebook = ttk.Notebook(root)
my_notebook.pack()

transaction_frame =  Frame(my_notebook, width=500, height=400)
balance_frame =  Frame(my_notebook, width=500, height=400)
payment_frame =  Frame(my_notebook, width=500, height=400)
history_frame =  Frame(my_notebook, width=500, height=400)


transaction_frame.pack(fill='both', expand=1)
balance_frame.pack(fill='both', expand=1)
payment_frame.pack(fill='both', expand=1)
history_frame.pack(fill='both', expand=1)

my_notebook.add(transaction_frame, text='Transaction')
my_notebook.add(balance_frame, text='Balance')
my_notebook.add(payment_frame, text='Payment')
my_notebook.add(history_frame, text='History')

my_notebook.bind("<<NotebookTabChanged>>", tab_change)





#payment_tab____________________________________________________________________________________

#Labels:
payment_payer_lbl = Label(payment_frame, text='Name of the payer : ',font=('Aharoni',10))
payment_recieve_lbl = Label(payment_frame, text='On whose account : ', font=('Aharoni',10))
payment_money_lbl = Label(payment_frame, text='How much money : ', font=('Aharoni',10))

#Entry:
payment_payer_en = Entry(payment_frame, width=30)
payment_recieve_en = Entry(payment_frame, width=30)
payment_money_en = Entry(payment_frame, width=30)

#Button:
payment_btn = Button(payment_frame, text='Enter', command=PaymentEnter, bg='SkyBlue1',width=10,font=(15))

#Locate : 
payment_payer_lbl.grid(row=0 , column=0, padx=10, pady=10)
payment_recieve_lbl.grid(row=1, column=0, padx=10, pady=10)
payment_money_lbl.grid(row=2, column=0, padx=10, pady=10)

payment_payer_en.grid(row=0 , column=1, padx=10, ipady=5)
payment_recieve_en.grid(row=1 , column=1, padx=10, ipady=5)
payment_money_en.grid(row=2 , column=1, padx=10, ipady=5)

payment_btn.grid(row=3, columnspan=2, column=1,  padx=30, pady=80)

#transaction_tab____________________________________________________________________________________

#variable : 


contribution_names= []

#spinbox :
person_contribute = Spinbox(transaction_frame, from_=1, to=20, width=10)
person_contribute.pack(padx=20, pady=20)

#button: 
button = Button(transaction_frame, text="submit", width=10, command=group)
button.pack(padx=20 , pady= 15 )



#history_tab____________________________________________________________________________________


tree = ttk.Treeview(history_frame)
tree.delete(*tree.get_children())

tree["columns"] = ('Payer', 'Cost','Date', 'Debtors', 'Describtion')

tree.column("#0", width=40, minwidth=30) 
tree.column("Payer", anchor=W, width=80)
tree.column("Cost", anchor=CENTER, width=50)
tree.column("Date", anchor=W, width=80)
tree.column("Debtors", anchor=W, width=130)
tree.column("Describtion", anchor=W, width=100)

# Create headings
tree.heading("#0", text="Num", anchor=W)
tree.heading("Payer", text="Payer", anchor=W)
tree.heading("Cost", text="Cost", anchor=CENTER)
tree.heading("Date", text="Date", anchor=W)
tree.heading("Debtors", text="Debtors", anchor=W)
tree.heading("Describtion", text="Describtion", anchor=W)

# Add data
sp = Split()
sp.show_history()
c=1
for i in sp.row_of_transactions:
    tree.insert(parent="", index="end", iid= c, text= c , values= i[0:5])   
    c += 1           
sp.end()

# Place Treeview in the window
tree.pack(pady=20, fill="both", expand=True)


#_______________________________________________________________________________________________________


root.mainloop()





