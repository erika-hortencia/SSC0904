import anonimize
import tkinter as tk
from tkinter import filedialog, messagebox, ttk


#Initalise the tkinter GUI
ogDF = tk.Tk()
ogDF.title('Original Database')
ogDF.resizable(0, 0)

anonDF = tk.Tk()
anonDF.title('Anonimized Database')
anonDF.resizable(0, 0)

ogDF.geometry("800x300")
anonDF.geometry("800x300")

"""
Frame for TreeViews
"""
frame1 = tk.LabelFrame(ogDF, text="Original Data")
frame1.place(height=280, width=800)

frame2 = tk.LabelFrame(anonDF, text="Anonimized Data")
frame2.place(height=280, width=800)

"""
Treeviews Widget
"""
tv1 = ttk.Treeview(frame1)
tv1.place(relheight=1, relwidth=1) 

treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview) 
treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview) 
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) 
treescrollx.pack(side="bottom", fill="x") 
treescrolly.pack(side="right", fill="y") 

tv2 = ttk.Treeview(frame2)
tv2.place(relheight=1, relwidth=1) 

treescrolly2 = tk.Scrollbar(frame2, orient="vertical", command=tv2.yview) 
treescrollx2 = tk.Scrollbar(frame2, orient="horizontal", command=tv2.xview) 
tv2.configure(xscrollcommand=treescrollx2.set, yscrollcommand=treescrolly2.set) 
treescrollx2.pack(side="bottom", fill="x") 
treescrolly2.pack(side="right", fill="y") 

originalDF = anonimize.importOracleDB()
anonimizedDF = anonimize.anonimize_database(originalDF)

"""
Dataframes exhibition
"""
tv1["column"] = list(originalDF.columns)
tv1["show"] = "headings"
for column in tv1["columns"]:
    tv1.heading(column, text=column)

originalDF_rows = originalDF.to_numpy().tolist()
for row in originalDF_rows:
    tv1.insert("", "end", values=row)

tv2["column"] = list(anonimizedDF.columns)
tv2["show"] = "headings"
for column in tv2["columns"]:
    tv2.heading(column, text=column)

anonimizedDF_rows = anonimizedDF.to_numpy().tolist()
for row in anonimizedDF_rows:
    tv2.insert("", "end", values=row)


#print(originalDF)
#print(anonimizedDF)

ogDF.mainloop()
anonDF.mainloop()
