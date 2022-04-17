


from tkinter import *  # means imporing all the modules
site = Tk()      # creating base of tkinter window     site is name given to window
dia_1 = site.geometry('700x300')   # used to set the size or dimensions of tkinter window
main_title_1=site.title("Website Blocker Project")
label_1=Label(site, text ='Website Blocker', font ='arial 20 bold')
label_1.pack()
label_2=Label(site, text ='Enter Sites\nName: ', font ='arial 13 bold', fg='red').place(x=17, y=60)
text_box_1 = Text(site, font ='arial 10', height='2', width ='40' , highlightthickness=2 , highlightbackground='teal')
text_box_1 .place(x= 170,y = 60)
label_3=Label(site, text=' Enter Another\nName: ', font='arial 13 bold', fg='green').place(x=12, y=110)
text_box_2 = Text(site, font='arial 10', height='2', width='40' , highlightthickness=2 , highlightbackground='teal')
text_box_2.place(x= 168, y=120)
host_path = r"C:\Windows\System32\drivers\etc\hosts"   # it store the path of host file which id bydefault present in our systeam
ip_address = '127.0.0.1'    #it store the ip address used by localhost which is declared in host file.
def Blocker():     # here i have defined the blocker command
    website_lists = [ text_box_1.get(1.0,END) , text_box_2.get(1.0,END) ]     # it is used to get all the sites which is  enter by the users
    #in above line 1.0 means that the input should be read from line one and char 0(which define start position)  ,
    # END means to read until the end of the text box is reached(which specifies the end position)
    with open (host_path , 'r+') as host_file:      # with open statement it will open the file by using the given path location
        # r+_ is used to read and write the file
        file_content = host_file.read()    # here read command is assingned to file content
        for web in website_lists:            # the variable named as web is iterate over list named as wesite_lists
            if web in file_content:
                Label(site, text ='Already Blocked', font ='arial 12 bold').place(x=230, y=260)
                pass
            else:
                 host_file.write(ip_address + " " + web + '\n')
                 Label(site, text ="Successfully Blocked", font ='arial 12 bold').place(x=220, y =260)
c = Button(site, text ='Block', font ='arial 12 bold', command = Blocker, height=2, width = 7, bg ='royal blue')
# in above line whenever we press the button Blocker command get called
c.place(x = 250, y = 200)
site.mainloop()
+-