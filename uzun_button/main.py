from tkinter import*
import threading


root = Tk()

root.geometry("525x550+350+150")
root.resizable(width=False, height=False)
root.title('PyCircuitCenter | MTAcademy')
target_width = 400  # Hedef genişlik
step = 4 # Her adımda genişlik artışı
current_width = 0
lower_width = 400

def frame_animation_up():
    global current_width
    print(lower_width)
    if current_width < target_width:
        kullanici_frame.config(height=current_width)
        current_width += step
        root.after(2, frame_animation_up)
    else:
        current_width = 0  # Animasyon bittiğinde current_width'ı sıfırla

           

def frame_animation_down():
    global lower_width
    if 0 < lower_width:
        print(lower_width)
        kullanici_frame.config(height=lower_width)
        lower_width -= step
        root.after(2, frame_animation_down)
    else:
        lower_width = 400  # Animasyon bittiğinde current_width'ı sıfırla
        kullanici_frame.place_forget()


  
kullanici_frame = Frame(root, height=0, width=525, highlightbackground='lightblue', highlightthickness=4)

def start_thread(event):
    thread = threading.Thread(target=thread_function, args=(event,))
    thread.start()

    
def thread_function(event):
        kodlanmis_metin = event.encode('utf-8')
    
        if kodlanmis_metin == b'\xe2\x80\x94 Kullan\xc4\xb1c\xc4\xb1 Ekle':
            uzun_buton.config(text='▽ Kullanıcı Ekle')
            frame_animation_up()
            kullanici_frame.place(x=0, y=50)
            kullanici_lf = LabelFrame(kullanici_frame, text='Kullanıcı Olustur ve Düzenle')
            kullanici_lf.place(relx=0.05, rely=0.05, relwidth=0.9,relheight=0.9 )
        
        else:
            uzun_buton.config(text='— Kullanıcı Ekle')
            frame_animation_down()
        

    
frame = Frame(root,height=50, width=525)
frame.pack(anchor='n',fill=X, expand=True)
frame.pack_propagate(FALSE)

uzun_buton = Button(frame, 
                    width=600, 
                    bg='#ff8800',
                    relief='raised', 
                    activebackground='#ff8800', 
                    activeforeground='white',
                    text='— Kullanıcı Ekle',
                    fg='white',
                    anchor='w',
                    font='Helvetica 10'
                    )

                  
uzun_buton.place(x=0, width=525, height=40)


uzun_buton.bind("<Button-1>", lambda event: start_thread(uzun_buton.cget('text')))


butonFrame = Frame(frame, height=30, width=300, background='#ff8800')
butonFrame.place(in_=uzun_buton, x=230, y=3)

kisa_buton_1 = Button(frame, text='+ Listele', width=12, bg='#56909c', font='Helvetica 9', fg='black', relief='raised', activebackground='#56909c')
kisa_buton_1.grid(in_= butonFrame, column=0, row=0, sticky='nsew', padx=2)

kisa_buton_2 = Button(frame, text='✓ Kaydet ', width=12, bg='#acb78e', font='Helvetica 9', fg='black', relief='raised', activebackground='#acb78e')
kisa_buton_2.grid(in_= butonFrame, column=1, row=0)

kisa_buton_3 = Button(frame, text='× İptal  ', width=12, bg='#ff0033', font='Helvetica 9', fg='black', relief='raised', activebackground='#ff0033')
kisa_buton_3.grid(in_= butonFrame, column=2, row=0, padx=2)



root.mainloop()