#------------------------------------------------------------------moudules
from tkinter import *
from tkinter import font
import pygame                                                                  # use for bolding font
# from PIL import ImageTk,Image 
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
    @staticmethod
    def play_song(value='play'):
        if value=='play':
            pygame.mixer.init()
            pygame.mixer.music.load('music/Music relax Musiceto (10).mp3')
            pygame.mixer.music.play(loops=2)
        else:
            pygame.mixer.music.stop()
            
    def __init__(self):
        self.main_widget=Tk()                                                                                               
        self.main_widget.title('سیسـتم آشنایـی با دانشــگاه های ایران')                                                                             
        self.main_widget.iconbitmap('icon/iran_kkd_icon.ico')
        IranUniversity.set_size(self.main_widget,600,450)
        self.main_widget.resizable(width=False,height=False)
        self.music=IranUniversity.play_song()
        # pygame.mixer.init()
        # pygame.mixer.music.load('music/Music relax Musiceto (10).mp3')
        # pygame.mixer.music.play(loops=2)
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



























        self.main_widget.mainloop()
