from tkinter import *
from fpdf import FPDF
#tkinter layout

window=Tk()
window.title("Invoice generator")

mediciens={
    "Medicine A":10,
    "Medicine B":20,
    "Medicine C":15,
    "Medicine D":25
}
#shopping cart
invoice_items=[]

def calculate_total():
    total=0.0
    for item in invoice_items:
        total=total+item[2]
    return total
def add_medicines():
    #ANCHOR means getting asccess to selected item
    selected_medicine=medicine_listbox.get(ANCHOR)
    quantity=int(quantity_entry.get())
    price=mediciens[selected_medicine]*quantity
    invoice_items.append((selected_medicine,quantity,price))
    total_amount_entry.delete(0,END) #entry widget indexes 0,1,END
    total_amount_entry.insert(END,str(calculate_total()))
    update_invoice_text()

def update_invoice_text():
    invoice_text.delete(1.0,END) #1.0 means 1st line and 0th column (first line and first character ) to end
    for item in invoice_items:
        invoice_text.insert(END,f"Medicine name : {item[0]},quantity : {item[1]},item Total : {item[2]}\n")

def generate_invoice():
    customer_name=customer_entry.get()

    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica",size=12) #must
    
    #adding heading
    pdf.cell(0,10,txt="Invoice",new_x="LMARGIN",new_y="NEXT",align="C")#width #height #new_x,new_y says where the cursor should move after printing

    pdf.cell(0,10,txt="Customer:"+customer_name,new_x="LMARGIN",new_y="NEXT",align="L")
    #empty space
    pdf.cell(0,10,txt="",new_x="LMARGIN",new_y="NEXT")

    for y in invoice_items:
        medicine_name,quantity,item_total=y
        pdf.cell(0,10,text=f"Medicine: {medicine_name}, quantity: {quantity},item Total: {item_total}",new_x="LMARGIN",new_y="NEXT",align="L")

    pdf.cell(0,10,text="Total Cart amount: "+str(calculate_total()),new_x="LMARGIN",new_y="NEXT",align="L")

    pdf.output(f"{customer_name}_invoice.pdf")
#creating a layout
#creating a label
medicine_label=Label(window,text="Medicine: ")
medicine_label.pack()


#display multiple items from a list
#listbox
medicine_listbox=Listbox(window,selectmode=SINGLE)
for x in mediciens:
    #END mens index where medicine needs to be inserted
    #END always points to the position after the current last item
    medicine_listbox.insert(END,x)
medicine_listbox.pack()

#quantity label
quantity_label=Label(window,text="Quantity")
quantity_label.pack()
#quantity entry
quantity_entry=Entry(window)
quantity_entry.pack()

#button to add
add_button=Button(window,text="Add medicine",command=add_medicines) #add_medicines has no parameters so no lambda
add_button.pack()

#total amount label
total_amount_label=Label(window,text="Cart total amount")
total_amount_label.pack()
#total amount entry
total_amount_entry=Entry(window)
total_amount_entry.pack()

#customer label
customer_label=Label(window,text="Customer Name:")
customer_label.pack()
#customer entry
customer_entry=Entry(window)
customer_entry.pack()

#final button
generate_button=Button(window,text="Generate Invoice",command=generate_invoice)
generate_button.pack()

#text widget
# for displaing the generated invoice
invoice_text=Text(window,height=10,width=50)
invoice_text.pack()



window.mainloop()