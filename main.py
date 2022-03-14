from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import random
from time import sleep
import threading


level_esay = ['nice' , 'yes' , 'who' ,'hello' , 'good' , 'cake' , 'cook' , 'one' , 'green' , 'blue' , ]
level_avrage = ['paltry' , 'known' , 'marked' , 'true' , 'witty' , 'phobic' , 'frail' , 'gusty' ,'frail']
level_hard = ['astonishing' , 'quarrelsome' , 'glistening' , 'stimulating' , 'stereotyped' , 'comprehensive' , 'overrated', 'dysfunctional']
time= 59
false_asw = 0
total_asw = 0
def timer():
    global time , total_asw , false_asw
    while time > 0:
        time -= 1
        sleep(1)
        lbl_time_num['text'] = str(time)
        main_page.update()
    if time == 0:
        main_page.withdraw()
        final_page.deiconify()
        sv_correct_anw.set(total_asw - false_asw)
        sv_total_anw.set(total_asw)
        sv_false_anw.set(false_asw)
        wpm_c = sv_correct_anw.get() / 5
        sv_wpm.set(float(wpm_c) / 60)
        if sv_correct_anw.get() >= 20:
            sv_rate.set("A")
        elif sv_correct_anw.get() >= 10:
            sv_rate.set("B")
        elif  5 <= sv_correct_anw.get() < 10:
            sv_rate.set("C")
        elif sv_correct_anw.get() < 5:
            sv_rate.set("F")
            
def start_test():
    global word_level
    Level = level_combo.get()
    if Level == "Esay":
        word_level = "Esay"
        sv_word.set(random.choice(level_esay))
        main_page.deiconify()
        app.withdraw()
        th_time.start()
    elif Level == "Avrage":
        word_level = "Avrage"
        sv_word.set(random.choice(level_avrage))
        main_page.deiconify()
        app.withdraw()
        th_time.start()
    elif Level == "Hard":
        word_level = "Hard"
        sv_word.set(random.choice(level_hard))
        main_page.deiconify()
        app.withdraw()
        th_time.start()
    else:
        messagebox.showinfo("Error" , "Please select a level !!")
def next_word(n):
    global word_level , total_asw , false_asw
    if word_level == "Esay":
        if entry_text.get() in level_esay:
            total_asw += 1
            entry_text.delete(0  , END)
            sv_word.set(random.choice(level_esay))
        else:
            false_asw += 1
            total_asw += 1
            entry_text.delete(0  , END)
            sv_word.set(random.choice(level_esay))
    elif word_level == "Avrage":
        if entry_text.get() in level_avrage:
            total_asw += 1
            entry_text.delete(0  , END)
            sv_word.set(random.choice(level_avrage))
        else:
            false_asw += 1
            total_asw += 1
            entry_text.delete(0  , END)
            sv_word.set(random.choice(level_avrage))
    elif word_level == "Hard":
        if entry_text.get() in level_hard:
            total_asw += 1
            entry_text.delete(0  , END)
            sv_word.set(random.choice(level_hard))
        else:
            false_asw += 1
            total_asw += 1
            entry_text.delete(0  , END)
            sv_word.set(random.choice(level_hard))
# def cancel_main():
#     global false_asw , total_asw , time
#     false_asw = 0
#     total_asw = 0
#     time = 60
#     main_page.withdraw()
#     app.deiconify()
# windows=============================
app = Tk()
main_page = Toplevel(app)
final_page = Toplevel(app)
app.resizable(False  , False)
main_page.resizable(False , False)
final_page.resizable(False , False)
app.geometry('350x150')
main_page.geometry('370x120')
final_page.geometry('200x300')
final_page.configure(bg="#292826")
app.configure(bg="#292826")
main_page.configure(bg="#292826")
main_page.withdraw()
final_page.withdraw()
final_page.title('Final')
app.title('Typing Test')
main_page.title('Main Page')
# threading=========================
th_time = threading.Thread(target=timer)
# page1=============================
Label(app , text="Select Level" , bg="#292826" , fg="#F9D142" ,font=('Times' , 15)).pack(pady=5)
level_combo = Combobox(app ,state="readonly" ,values=["Esay" , "Avrage" , "Hard"])
level_combo.pack(pady=5)
btn_start = Button(app , text="Start" ,bg="#292826" ,activebackground="#292826",fg="#F9D142",font=('Times' , 10) ,command=start_test)
btn_start.place(x= 105 , y = 100 , width=50)
btn_cancel = Button(app , text="Exit" ,bg="#292826" , activebackground="#292826",fg="#F9D142",font=('Times' , 10) , command=app.destroy)
btn_cancel.place(x= 195 , y = 100 , width=50)
# page2==============================
Label(main_page , text="Word :" , bg="#292826" , fg="#F9D142",font=('Times' , 15)).place(x= 0, y=15)
Label(main_page , text="——————————————————" , bg="#292826" , fg="#F9D142",font=('Times' , 15)).place(x= 0 , y=40)
sv_word =StringVar()
entry_text = Entry(main_page ,font=('bold' , 17))
lbl_word = Label(main_page , textvariable=sv_word , bg="#292826" , fg="#F9D142",font=('Times' , 15))
lbl_time = Label(main_page , text='Time :' , bg="#292826" , fg="#F9D142",font=('Times' , 15))
lbl_time_num = Label(main_page , text='60', bg="#292826" , fg="#F9D142",font=('Times' , 15))
btn_cancel2 = Button(main_page , text="Cancel",bg="#292826" ,activebackground="#292826", fg="#F9D142",font=('Times' , 10) , command=app.destroy)
entry_text.bind('<Return>' , next_word)
lbl_time_num.place(x=60 , y=70)
entry_text.place(x= 210 , y= 13, width=150 , height=30)
lbl_time.place(x=0 , y=70)
btn_cancel2.place(x= 260 , y = 70, width=50)
lbl_word.place(x=60, y=15)
# page3==============================
sv_rate = StringVar()
sv_total_anw = IntVar()
sv_false_anw = IntVar()
sv_correct_anw = IntVar()
sv_wpm = IntVar()
lbl_rate = Label(final_page , textvariable=sv_rate, bg= "#292826", fg="#F9D142" ,font=('bold' ,50))
lbl_total_anw = Label(final_page , textvariable=sv_total_anw, bg= "#292826", fg="#F9D142" ,font=('Times' , 15))
lbl_false_anw = Label(final_page , textvariable=sv_false_anw, bg= "#292826", fg="#F9D142" ,font=('Times' , 15))
lbl_correct_anw = Label(final_page , textvariable=sv_correct_anw, bg= "#292826", fg="#F9D142" ,font=('Times' , 15))
lbl_wpm = Label(final_page , textvariable=sv_wpm, bg= "#292826", fg="#F9D142" ,font=('Times' , 15))
Label(final_page , text="——————————————————" , bg="#292826" , fg="#F9D142",font=('Times' , 15)).place(x= 0 , y=70)
Label(final_page, text="Total Answers :" , bg="#292826" , fg="#F9D142",font=('Times' , 10)).place(x= 30, y=100)
Label(final_page, text="Correct Answers:" , bg="#292826" , fg="#F9D142",font=('Times' , 10)).place(x= 23 , y=130)
Label(final_page, text="False Answers :" , bg="#292826" , fg="#F9D142",font=('Times' , 10)).place(x= 30 , y=160)
Label(final_page, text="WPM :" , bg="#292826" , fg="#F9D142",font=('Times' , 10)).place(x= 76, y=190)
Button(final_page , text="OK" ,bg="#292826" ,activebackground="#292826" ,fg="#F9D142",font=('Times' , 10) , command=app.destroy).place(x= 85 , y=250)
sv_false_anw.set(0)
sv_correct_anw.set(0)
sv_total_anw.set(0)
sv_wpm.set(0)
lbl_wpm.place(x=140,y=190)
lbl_total_anw.place(x=140 , y=100)
lbl_correct_anw.place(x=140 , y =130)
lbl_false_anw.place(x=140, y =160)
lbl_rate.pack()
# end================================
mainloop()