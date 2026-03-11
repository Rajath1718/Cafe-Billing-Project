from tkinter import *
from tkinter import messagebox
import random, math
from datetime import datetime
root =Tk()
root.geometry("1200x600")
root.title("FRANKEN PIZZAS")
root.resizable(False, False)
root['background']='#ebd7ce'
#root.iconphoto(False, PhotoImage(file="pizza2.png"))


Label(text="Frankenstein's Pizza", bg="#FFBF00",fg="#10A19D",font=("Baguet Script", 33,"italic"),  width="300", height="1").pack()


messagebox.showinfo("WELCOME", "WELCOME TO FRANKENSTEIN'S PIZZA!")




mp=[]
def p1():
    mp.append('Margherita')
    print(len(mp))

vs=[]
def p2():
    vs.append('veggie')
    print(len(vs))

hp=[]
def p3():
    hp.append('hawaii')
    print(len(hp))

mgw=[]
def p4():
    mgw.append('mexi')
    print(len(mgw))

sp=[]
def p5():
    sp.append('paneer')
    print(len(sp))


#=================Pizza menu

F1=LabelFrame(root, text="Pizzas", font=("Futura Bold", 25), fg="#7abaf8",bg="black")
F1.place(x=8, y=110, width="380", height="350")

p1_lbl=Label(F1, text="Margherita Pizza",bg="black", fg="#A8D1D1",font=("Futura bold", 15)).grid(row=0, column=0)
b1_lbl=Label(F1, text="   ₹199",bg="black", fg="#A8D1D1",font=("Futura bold", 15)).grid(row=0, column=3) 
#p1_txt=Entry(F1, width=7,bg="#FBF1D3", font=("Futura bold", 15), bd=5, relief=FLAT).grid(row=0, column=1, padx=10, pady=10)
p1_bt=Button(F1, text = 'Add Item', bg="#FBF1D3", activebackground="#A8D1D1", font=(" MS Serif", 10, "bold"), bd = '5', command = p1).grid(row=0, column=2, padx=10, pady=10)

p2_lbl=Label(F1, text="Veggie Sprinkle",bg="black", fg="#A8D1D1",font=("Futura bold", 15)).grid(row=1, column=0)
b2_lbl=Label(F1, text="   ₹280",bg="black", fg="#A8D1D1",font=("Futura bold", 15)).grid(row=1, column=3) 
#p2_txt=Entry(F1, width=7,bg="#FBF1D3", font=("Futura bold", 15), bd=5, relief=FLAT).grid(row=1, column=1, padx=10, pady=10)
p2_bt=Button(F1, text = 'Add Item', bg="#FBF1D3", activebackground="#A8D1D1", font=(" MS Serif", 10, "bold"),bd = '5',command = p2).grid(row=1, column=2, padx=10, pady=10)

p3_lbl=Label(F1, text="Hawaiian Pizza",bg="black", fg="#A8D1D1",font=("Futura bold", 15)).grid(row=2, column=0)
b3_lbl=Label(F1, text="   ₹350",bg="black", fg="#A8D1D1",font=("Futura bold", 15)).grid(row=2, column=3)
#p3_txt=Entry(F1, width=7,bg="#FBF1D3", font=("Futura bold", 15), bd=5, relief=FLAT).grid(row=2, column=1, padx=10, pady=10)
p3_bt=Button(F1, text = 'Add Item',bg="#FBF1D3", activebackground="#A8D1D1", font=(" MS Serif", 10, "bold"),bd = '5',command = p3).grid(row=2, column=2, padx=10, pady=10)

p4_lbl=Label(F1, text="Mexican Green Wave",bg="black", fg="#A8D1D1",font=("Futura bold", 15)).grid(row=3, column=0)
b4_lbl=Label(F1, text="   ₹299",bg="black", fg="#A8D1D1",font=("Futura bold", 15)).grid(row=3, column=3) 
#p4_txt=Entry(F1, width=7,bg="#FBF1D3", font=("Futura bold", 15), bd=5, relief=FLAT).grid(row=3, column=1, padx=10, pady=10)
p4_bt=Button(F1, text = 'Add Item',bg="#FBF1D3", activebackground="#A8D1D1", font=(" MS Serif", 10, "bold"),bd = '5',command = p4).grid(row=3, column=2, padx=10, pady=10)

p5_lbl=Label(F1, text="Spicy Paneer",bg="black", fg="#A8D1D1",font=("Futura bold", 15)).grid(row=4, column=0)
b5_lbl=Label(F1, text="  ₹250",bg="black", fg="#A8D1D1",font=("Futura bold", 15)).grid(row=4, column=3) 
#p5_txt=Entry(F1, width=7,bg="#FBF1D3", font=("Futura bold", 15), bd=5, relief=FLAT).grid(row=4, column=1, padx=10, pady=10)
p5_bt=Button(F1, text = 'Add Item',bg="#FBF1D3", activebackground="#A8D1D1", font=(" MS Serif", 10, "bold"),bd = '5',command = p5).grid(row=4, column=2, padx=10, pady=10)

a=len(mp)
price=a*199

def tot():
    messagebox.showinfo("Total Items in Your Cart", message= "Margherita pizzas \t"+str(len(mp))+"\nVeggie Sprinkle \t"+str(len(vs))+"\nHawaiian Pizza \t"+str(len(hp))+"\nMexiacan GW \t"+str(len(mgw))+"\nSpicy Paneer \t"+str(len(sp))+"\nGarlic Bread \t"+str(len(gb))+"\nTacos \t\t"+str(len(tc))+"\nNachos \t\t"+str(len(nc))+"\nCoke \t\t"+str(len(ck))+"\nFrench fries \t"+str(len(ff)))
    print(len(mp)*199)

tot_bt=Button(root, text = 'Check Cart', bg="#10A19D", activebackground="#A8D1D1",fg="#31302f", font=(" MS Serif", 15, "bold"), bd = '5', command = tot)
tot_bt.place(x=100,y=500)

gb=[]
def s1():
    gb.append('Garlic Bread')
    print(len(gb))

tc=[]
def s2():
    tc.append('Tacos')
    print(len(tc))

nc=[]
def s3():
    nc.append('Nachos')
    print(len(nc))

ck=[]
def s4():
    ck.append('Coke')
    print(len(ck))

ff=[]
def s5():
    ff.append('french fries')
    print(len(ff))

#=================Side menu

F3=LabelFrame(root, text="Sides", font=("Futura Bold", 25), fg="#7abaf8",bg="black")
F3.place(x=425, y=110, width="340", height="350")

s1_lbl=Label(F3, text="   Garlic bread",bg="black", fg="#A8D1D1",font=("Futura bold", 15)).grid(row=0, column=0)
a1_lb=Label(F3,text="₹120",bg="black",fg="#A8D1D1",font=("Futura bold", 15)).grid(row=0, column=3, padx=10, pady=10)
#p1_txt=Entry(F1, width=7,bg="#FBF1D3", font=("Futura bold", 15), bd=5, relief=FLAT).grid(row=0, column=1, padx=10, pady=10)
s1_bt=Button(F3, text = 'Add Item', bg="#FBF1D3", activebackground="#A8D1D1", font=(" MS Serif", 10, "bold"), bd = '5', command = s1).grid(row=0, column=2, padx=10, pady=10)

s2_lbl=Label(F3, text="Tacos",bg="black", fg="#A8D1D1",font=("Futura bold", 15)).grid(row=1, column=0)
a2_lbl=Label(F3, text="₹99",bg="black", fg="#A8D1D1",font=("Futura bold", 15)).grid(row=1, column=3)
#p2_txt=Entry(F1, width=7,bg="#FBF1D3", font=("Futura bold", 15), bd=5, relief=FLAT).grid(row=1, column=1, padx=10, pady=10)
s2_bt=Button(F3, text = 'Add Item', bg="#FBF1D3", activebackground="#A8D1D1", font=(" MS Serif", 10, "bold"),bd = '5',command = s2).grid(row=1, column=2, padx=10, pady=10)

s3_lbl=Label(F3, text="Nachos",bg="black", fg="#A8D1D1",font=("Futura bold", 15)).grid(row=2, column=0)
a3_lbl=Label(F3, text="₹85",bg="black", fg="#A8D1D1",font=("Futura bold", 15)).grid(row=2, column=3)
#p3_txt=Entry(F1, width=7,bg="#FBF1D3", font=("Futura bold", 15), bd=5, relief=FLAT).grid(row=2, column=1, padx=10, pady=10)
s3_bt=Button(F3, text = 'Add Item',bg="#FBF1D3", activebackground="#A8D1D1", font=(" MS Serif", 10, "bold"),bd = '5',command = s3).grid(row=2, column=2, padx=10, pady=10)

s4_lbl=Label(F3, text="Coke",bg="black", fg="#A8D1D1",font=("Futura bold", 15)).grid(row=3, column=0)
a4_lbl=Label(F3, text="₹30",bg="black", fg="#A8D1D1",font=("Futura bold", 15)).grid(row=3, column=3) 
#p4_txt=Entry(F1, width=7,bg="#FBF1D3", font=("Futura bold", 15), bd=5, relief=FLAT).grid(row=3, column=1, padx=10, pady=10)
s4_bt=Button(F3, text = 'Add Item',bg="#FBF1D3", activebackground="#A8D1D1", font=(" MS Serif", 10, "bold"),bd = '5',command = s4).grid(row=3, column=2, padx=10, pady=10)

s5_lbl=Label(F3, text="   French Fries",bg="black", fg="#A8D1D1",font=("Futura bold", 15)).grid(row=4, column=0)
a5_lbl=Label(F3, text="₹50",bg="black", fg="#A8D1D1",font=("Futura bold", 15)).grid(row=4, column=3) 
#p5_txt=Entry(F1, width=7,bg="#FBF1D3", font=("Futura bold", 15), bd=5, relief=FLAT).grid(row=4, column=1, padx=10, pady=10)
s5_bt=Button(F3, text = 'Add Item',bg="#FBF1D3", activebackground="#A8D1D1", font=(" MS Serif", 10, "bold"),bd = '5',command = s5).grid(row=4, column=2, padx=10, pady=10)

                                                                            
#=============================Price Calculation AND BILL DISPLAY==========================================
#Pizzas :

def total():
    
    mp_cost =  float((len(mp)*199) )
    vs_cost =  float((len(vs)* 280))
    hp_cost =  float((len(hp)* 350))
    mgw_cost = float((len(mgw)* 299))
    sp_cost =  float((len(sp)* 250) )
    tot_piza_price=float(mp_cost+vs_cost+hp_cost+mgw_cost+sp_cost)

    #Sides:
    gb_cost =  float((len(gb)* 120))
    tac_cost = float((len(tc)* 99))
    nac_cost = float((len(nc)* 85))
    cok_cost = float((len(ck)* 30))
    ff_cost =  float((len(ff)*  50))
    tot_side_price=float(gb_cost+tac_cost+nac_cost+cok_cost+ff_cost)
    total_cart_price=tot_side_price+tot_piza_price
    gst=float(0.11*total_cart_price)
    TOTAL=float(math.ceil(float(gst+total_cart_price)))
    if total_cart_price == 0:
        messagebox.showerror("EMPTY CART !", message="Your Cart is Empty :(")

    else:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        y=order_no=random.randint(100,999)
        txt.insert(END, "\n          WELCOME TO FRANKEN'S")
        txt.insert(END, "\n---------------------------------------")
        txt.insert(END, f"\nORDER NO: {order_no}                  {current_time}")
        txt.insert(END, "\n========================================")
        txt.insert(END, "\nPRODUCT\t\t  QTY\t\tPRICE")
        txt.insert(END, "\n========================================")
        #txt.insert(END, "\nMargherita P\t\t  3\t\t650")
        #pizza bill 
        if len(mp) !=0:
            txt.insert(END,f"Margherita P\t\t   {len(mp)}\t\t{mp_cost}" )
        if len(vs) !=0:
            txt.insert(END,f"\nVeggie Sprinkle\t\t  {len(vs)}\t\t{vs_cost}" )    
        if len(hp) !=0:
            txt.insert(END,f"\nHawaiian P\t\t   {len(hp)}\t\t{hp_cost}" )
        if len(mgw) !=0:
            txt.insert(END,f"\nMexican Green W\t\t  {len(mgw)}\t\t{mgw_cost}" )
        if len(sp) !=0:
            txt.insert(END,f"\nSpicy Paneer\t\t   {len(sp)}\t\t{sp_cost}" )
        if len(gb) !=0:
            txt.insert(END,f"\nGarlic Bread\t\t   {len(gb)}\t\t{gb_cost}" )
        if len(tc) !=0:
            txt.insert(END,f"\nTacos\t\t   {len(tc)}\t\t{tac_cost}" )    
        if len(nc) !=0:
            txt.insert(END,f"\nNachos\t\t   {len(nc)}\t\t{nac_cost}" )
        if len(ck) !=0:
            txt.insert(END,f"\nCoke Regular\t\t   {len(ck)}\t\t{cok_cost}" )
        if len(ff) !=0:
            txt.insert(END,f"\nFrench Fries\t\t   {len(ff)}\t\t{ff_cost}" )
    
        txt.insert(END, "\n\n---------------------------------------")
        txt.insert(END, f'\n\t\t Sub Total: \t\t {total_cart_price}')
        txt.insert(END, f"\n\t\t GST @11% \t\t {gst}")
        txt.insert(END, "\n---------------------------------------")
        txt.insert(END, f'\n\t\t TOTAL: \t\t {TOTAL}')
        txt.insert(END, "\n========================================")
        txt.insert(END, "    Thank you for ordering @Franken's")
        txt.insert(END, "\n========================================\n")
   

bill_bt=Button(root, text = '   BILL   ', bg="#10A19D", activebackground="#FFBF00",fg="#31302f", font=(" MS Serif", 15, "bold"), bd = '5', command = total)
bill_bt.place(x=300, y=500)   


#============================================== ========================================


#=============BILL AREA================


F2 = LabelFrame(root, bd=5, relief=GROOVE)
F2.place(x=830, y=110, width=355, height=400)
bill_title=Label(F2,text="Frankenstein's",font="arial 15 bold",fg="#46C2CB", bd=7, relief=GROOVE).pack(fill=X)
scrol_y=Scrollbar(F2, orient="vertical")
txt=Text(F2, yscrollcommand=scrol_y.set)
scrol_y.pack(side=RIGHT, fill=Y)
scrol_y.config(command=txt.yview)
txt.pack()



#Clear Cart Button ====================================

def clear():
    res=messagebox.askquestion('CLEAR CART', 'Do you really want to clear the items in your cart?')
    if res == 'no' :
        return
    else :
        mp.clear()
        sp.clear()
        vs.clear()
        mgw.clear()
        hp.clear()
        gb.clear()
        ck.clear()
        tc.clear()
        nc.clear()
        ff.clear()
        
    
    
    
clear_bt=Button(root, text = 'Clear Cart', bg="#FD8A8A", activebackground="#A8D1D1",fg="#31302f", font=(" MS Serif", 15, "bold"), bd = '5', command = clear)
clear_bt.place(x=480, y=500) 


root.mainloop()
