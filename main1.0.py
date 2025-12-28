from customtkinter import *
from PIL import Image
import socket 
import threading


#створи картинки CTKImage
FON = CTkImage(light_image=Image.open("fon.png"),size=(300,400))   #fon 350,400
CONF =CTkImage(light_image=Image.open("conf.png"),size=(50,50))#conf 20,20
USER =CTkImage(light_image=Image.open("user.png"),size=(20,20)) #user 20,20
ICONS = [] #user icons 20,20
for i in range(7):
    ICONS.append(CTkImage(light_image=Image.open(f"{i}.png"),size = (85,85)))
#кольори
BLUE= "#5D89EA"
CYAN = "#2EB3E4"
PURPULE = "#B43EF5"
MEDIUMBLUE = "#8D60F0"
PHLOX = "#EB0EFC"

class MyLbl(CTkLabel):
    def __init__(self, master,   text = "CTkLabel", size=16, image = None):
        super().__init__(master,text_color ="#f2f2f2" , text = "PHLOX",
                          font=("Arial",16), image =image )

class MyBtn(CTkButton):
    def __init__(self, master, width = 140, height = 30,text = "CTkButton", 
                  image = None,  command = None):
        super().__init__(master, width = width, height = height, corner_radius = 20,
                             text_color = "white",fg_color=MEDIUMBLUE,hover_color=BLUE,
                                text =text, font = ("Arial",16,"bold"), image = image, command=command)



class Mess(CTkLabel):
    def __init__(self,master,user,icon,text,anchor):
        icon = CTkImage(light_image=Image.open(f"{icon}.png"),size = (25,25))

        super().__init__(master = master,fg_color="#fdcccc",
                         text_color="#000000",font = ("Arial",16,"bold"),
                         image= icon, compound= "left", corner_radius=20,
                         padx = 10, pady = 10,text = f"{user}:{text}")
        
        self.pack(padx = 50,pady=2,anchor=anchor)
        



class App(CTk):
    def __init__(self):
        super().__init__()
        self.USER = "anonim"
        self.ICON = 0
        self.geometry("600x400")
        self.configure(fg_color = "#504646")
        self.title("logik")
        self.iconbitmap("icon.ico")
        self.resizable(False,False)
        self.HOST = "0"
        self.PORT= 8080



        self.lbl = MyLbl(self,text = "WELCOM",size = 40, image=FON)
        self.lbl.place(x=0,y=0)
        lbl2 = MyLbl(self,text="logiks",size=20)
        lbl2.place(x = 450,y=50)



        self.frame_start = CTkFrame(self,width=600,height=400,fg_color="#7a50b2")
        self.frame_start.place(x=0,y=0)


        self.box_port = CTkEntry(self.frame_start, width = 250,height=50,fg_color="#34dd97",
                                 corner_radius=25,placeholder_text="port")
        self.box_port.place(x = 100,y = 150)

        self.box_host = CTkEntry(self.frame_start, width = 250,height=50,fg_color="#34dd97",
                                 corner_radius=25,placeholder_text="host")
        self.box_host.place(x = 100,y = 220)


        self.btn_begin = MyBtn(self.frame_start,text ="begin", command = self.begin)
        self.btn_begin.place(x = 100, y = 300)

    def begin(self):
        self.PORT = int(self.box_port.get())
        self.HOST = int(self.box_host.get())
        self.frame_start.destroy()



        self.btn_name = MyBtn(self,text = "Entr", image=USER,command = self.open_name)
        self.btn_name.place(x = 405,y = 150)

        self.btn_icon = MyBtn(self,text = "Entr icom", image=USER, command = self.open_icon)
        self.btn_icon.place(x = 405,y = 200)

        self.btn_chat = MyBtn(self,width= 100,
                              text = "Entr c")
        self.btn_chat.configure(fg_color=PHLOX,text_color ="grey",command = self.open_chat)
        self.btn_chat.place(x=420,y=250)


        self.frame_name = CTkFrame(self,width = 350,
                                    height= 400,fg_color="#d68e8e")
        self.frame_name.place(x =-350, y = 0)




        lbl3 = MyLbl(self.frame_name, text = "enter name", size = 20,)
        lbl3.place (x = 50,y = 100)
        self.box_name = CTkEntry(self.frame_name, width = 250,height=50,fg_color="#34dd97",
                                 corner_radius=25,)
        self.box_name.place(x = 50,y = 150)
        self.btn_save_name = MyBtn(self.frame_name,text ="save_name", command = self.save_name)
        self.btn_save_name.place(x = 100, y = 220)

        self.frame_icon = CTkFrame(self,width = 350,
                                    height= 400,fg_color="#d68e8e")
        self.frame_icon.place(x =-350, y = 0)
        c,r = 0,0
        for i in range(1,7):
            if i%2 ==0:
                c = 1
            else:
                c = 0
            btn = MyBtn(self.frame_icon, text = "", image = ICONS[i],
                        width = 80, height = 80,command=lambda i = i:self.save_icon(i)) 

            btn.grid(row =int(r), column = c,padx = 23,pady=23)
           
            r += 0.5



        self.frame_chat = CTkFrame(self, fg_color="#7d7979", width=600,
                                   height=400)
        self.frame_chat.place(x = 0, y = -400)
        self.all_mess = CTkScrollableFrame(self.frame_chat,
                                           fg_color="#7d7979"
                                           ,width=580,height=300)
        self.all_mess.place(x = 0, y =0)



        self.inp_mess = CTkTextbox(self.frame_chat,width=350,height=50,fg_color= BLUE,
                                   corner_radius=30)
        self.inp_mess.place(x = 20,y = 320)



        self.btn_send_mess= MyBtn(self.frame_chat,width=50,height=50,text = "send", command =self.send_mess)
        self.btn_send_mess.place(x = 400,y =320)

        

            


    def open_name(self):
        self.nx = -350
        def anime():
            self.nx += 10
            self.frame_name.place (x = self.nx,y = 0 ) 
            if self.nx < 0 :
                self.after(10,anime)

        anime()


    def close_name(self):
        self.nx = 0
        def anime():
            self.nx -= 10
            self.frame_name.place (x = self.nx,y = 0 ) 
            if self.nx > -350 :
                self.after(10,anime)
        anime()



    def save_name (self):
        self.USER = self.box_name.get()
        print(self.USER)
        self.close_name()

    def open_icon (self):
        self.nx = -350
        def anime():
            self.nx += 10
            self.frame_icon.place (x = self.nx,y = 0 ) 
            if self.nx < 0 :
                self.after(10,anime)

        anime()


    def close_icon(self):
        self.nx = 0
        def anime():
            self.nx -= 10
            self.frame_icon.place (x = self.nx,y = 0 ) 
            if self.nx > -350 :
                self.after(10,anime)
        anime()
    def save_icon(self,i):
        self.ICON =i
        self.close_icon()



    def open_chat(self):
        try:

            self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.socket.connect((f"{self.HOST}.tcp.eu.ngrok.io",self.PORT))
            self.socket.send(f"{self.USER}|{self.ICON}".encode())
            Mess(self.all_mess,self.USER,self.ICON,"welcom chat!","w")
            input = threading.Thread(target=self.input_mess, daemon=True)
            input.start()
            self.ny = -400
            def anime():
                self.ny += 10
                self.frame_chat.place (x = 0,y = self.ny ) 
                if self.ny < 0 :
                    self.after(10,anime)

            anime()
        except:

            self.lbl.configure(text = "sorry, chat do not work")

    def input_mess(self):
        while True:
            try:
                mess = self.socket.recv(1024).decode
                user,icon,mess = mess.split("|")
                Mess(self.all_mess,user,icon,mess,"e")
            except:
                Mess(self.all_mess,"server",0,"sorry,Goodbye")
                self.after(100,self.close)
    def close(self):
        self.socket.close()
        self.destroy()



    def send_mess(self):
        mess = self.inp_mess.get("1.0","end").strip
        self.inp_mess.delete("1.0","end")
        try:
            self.socket.send(mess.encod())
            Mess(self.all_mess,self.USER,self.ICON,mess, "w")
        except:
            Mess(self.all_mess,"server",0,"sorry,Goodbye","w")
            self.after(100,self.close)



app = App()
app.mainloop()