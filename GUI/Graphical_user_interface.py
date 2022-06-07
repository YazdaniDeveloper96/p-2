import sys
sys.path.insert(0,"C:/Users/MohammadReza/Desktop/p-2")
#------------------------------------------------------------------moudules
from tkinter import *
from tkinter import font                          # use for bolding font
from external_modules.play_song import *
from tkinter import ttk
#--------------------------------------------------------------------------
###########################################################################
###########################################################################
###########################################################################
###########################################################################
###########################################################################
#------------------------------------------------------------------main program
import os
os.system('cls')
#--------------------------------
class IranUniversity:
    @staticmethod
    def set_size(window,width,height):
        w=width
        h=height
        ws=window.winfo_screenwidth()
        hs=window.winfo_screenheight()
        x=(ws/2)-(w/2)
        y=(hs/2)-(h/2)
        window.geometry("%dx%d+%d+%d"%(w,h,x,y))

    def __init__(self):
        self.main_widget=Tk()                                                                                               
        self.main_widget.title('سیسـتم آشنایـی با دانشــگاه های ایران')                                                                             
        self.main_widget.iconbitmap('icon/iran_kkd_icon.ico')
        IranUniversity.set_size(self.main_widget,600,450)
        self.main_widget.resizable(width=False,height=False)
        self.music=playSong()
    ##################################################################### adding imageBackground for main widget
        self.bg = PhotoImage(file = "img/root_background1.png")
        self.enter_city = PhotoImage(file = "img/city_name_botton1.png")
        self.but_show = PhotoImage(file = "img/show_botton.png")
    ##################################################################### adding imageBackground for main widget
        self.canvas1 = Canvas(self.main_widget,width = 400,height = 400)
        self.canvas1.pack(fill = "both", expand = True)
        self.canvas1.create_image(0,0,image = self.bg,anchor="nw")
    ################################################################################################ add label 
        self.lab_enter_city=Label(master=self.canvas1,image=self.enter_city,borderwidth=0,bg='#000000',activebackground='#000000') 
        self.lab_enter_city.grid(row=0,column=0,padx=(15,0),pady=(380,0))
    ################################################################################################ add entrybox
        self.entry_box_city=Entry(master=self.canvas1,borderwidth=2,width=13,font=('tahoma',22,font.BOLD)) 
        self.entry_box_city.grid(row=0,column=1,padx=(5,0),pady=(380,0))
    ################################################################################################ add button
        self.button_show=Button(master=self.canvas1,image=self.but_show,borderwidth=1,bg='#ffffff') 
        self.button_show.grid(row=0,column=2,padx=(5,0),pady=(380,0))
    ################################################################################################ bind 
        self.button_show.bind('<Button-1>',lambda event:self.__show_result(event))


        self.main_widget.mainloop()

    def __show_result(self,event):
        second_page=Toplevel()
        second_page.title('نتایج جستو جو')
        second_page.iconbitmap('icon/iran_kkd_icon.ico')
        IranUniversity.set_size(second_page,900,300)
        second_page.resizable(width=False,height=False)
        tree=ttk.Treeview(second_page,column=("province state ",'web page'),show='headings',height=5)
        tree.grid(row=1,columnspan=1,padx=10,pady=20)
        tree.column('# 1',anchor=CENTER,width=300)
        tree.heading('# 1',text='نام دانشگاه')
        tree.column('# 2',anchor=CENTER,width=575)
        tree.heading('# 2',text='آدرس اینترنتی دانشگاه')

        #------get all products---------
        n=1
        try:
            for item in self.book:
                tree.insert('','end',text=str(n),values=(item[0],item[1]))
                n+=1
        except Exception as error:
            # messagebox.showwarning(book_window,message="متاسفانه دسترسی به دیتابیس امکان پذیر نیست")
            pass
