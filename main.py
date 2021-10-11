from tkinter import *
import webbrowser
from time import strftime
from PIL import ImageTk, Image
from datetime import date
import calendar
import csv

# Window options
height = 500
width = 640

b_width = 14
bgc = "light steel blue"

# Data
filename = "data/data.csv"
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        rows.append(row)


# Rows
row1 = int((height/20)*3)
row2 = int((height/20)*7)
row3 = int((height/20)*11)
row4 = int((height/20)*15)
row5 = int((height/20)*19)

# Columns
b_col = int((width/4)*1)+10
zoom_col = int((width/4)*3)
t_col = int((width/20)*14)

# Font
desc_font = ('calibri', 15, 'bold')

# Root window
root = Tk()
root.geometry("300x500")
root.title(str(rows[1]).replace("[","").replace("]","").replace("'",""))
root.resizable(width=False, height=False)
root.configure(bg=bgc)
root.geometry(str(width) + "x" + str(height))
root.iconbitmap('data/links.ico')

if int(str(rows[9]).replace("[","").replace("]","").replace("'","")):
    web_client = "https://pwa.zoom.us/wc/join/"
else:
    web_client = "https://pwa.zoom.us/j/"


# Clock
def timed():
    string = strftime('%I:%M %p').lstrip('0')
    clock_text.config(text=string)
    clock_text.after(1000, timed)

def enter_data():
    txt_name = zoom_ent.get()
    meeting_id = txt_name.replace(" ", "")
    if len(meeting_id) in (10,11):
        link = web_client+meeting_id
        error_message = Label(root, text="                                                     ", bg=bgc, fg="black")
        error_message.place(x=zoom_col, y=row3+20, anchor="center")
        error_message.config(font=('calibri', 15, 'bold'))
        webbrowser.open(link, 1)
    else:
        error_message = Label(root, text="Please enter a valid meeting ID", bg=bgc, fg="black")
        error_message.place(x=zoom_col, y=row3+20, anchor="center")
        error_message.config(font=('calibri', 15, 'bold'))

# Links
def jw_org():
    jw_org_link = "https://jw.org"
    webbrowser.open(jw_org_link, 1)

def wol():
    wol_link = "https://wol.jw.org"
    webbrowser.open((wol_link))

def zoom_mw():
    zoom_link = str(web_client+str(rows[3]).replace("[","").replace("]","").replace("'",""))
    # https://pwa.zoom.us/wc/join/ --Meeting ID
    webbrowser.open(zoom_link)

def zoom_we():
    zoom_link = str(web_client+str(rows[5]).replace("[","").replace("]","").replace("'",""))
    # https://pwa.zoom.us/wc/join/ --Meeting ID
    webbrowser.open(zoom_link)

def notice():
    notice_link = str(rows[7]).replace("[","").replace("]","").replace("'","")
    webbrowser.open(notice_link)

def meeting_choice():
    if calendar.day_name[date.today().weekday()] in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        zoom_mw()
    else:
        zoom_we()

# Images
width_i = 320
height_i = 100

pixel = PhotoImage(width=1, height=1)

enter_button_photo = Image.open("data/icons/enterb.png")  #300x900 (1/3)
enter_button_r = enter_button_photo.resize((120, 40), Image.ANTIALIAS)
enter_button = ImageTk.PhotoImage(enter_button_r)

jw_photo = Image.open("data/icons/jw_lrg.png")
jw_r = jw_photo.resize((width_i, height_i), Image.ANTIALIAS)
jw_image = ImageTk.PhotoImage(jw_r)

wol_photo = Image.open("data/icons/wol_lrg.png")
wol_r = wol_photo.resize((width_i, height_i), Image.ANTIALIAS)
wol_image = ImageTk.PhotoImage(wol_r)

zoom_photo = Image.open("data/icons/zoom_lrg.png")
zoom_r = zoom_photo.resize((width_i, height_i), Image.ANTIALIAS)
zoom_image = ImageTk.PhotoImage(zoom_r)

notice_photo = Image.open("data/icons/notice_lrg.png")
notice_r = notice_photo.resize((width_i, height_i), Image.ANTIALIAS)
notice_image = ImageTk.PhotoImage(notice_r)

# Buttons

jw_org = Button(root, image=jw_image, bg=bgc, borderwidth=0, highlightthickness=0, activebackground=bgc, command=jw_org)
jw_org.place(x=b_col, y=row1, anchor="center")

wol = Button(root, image=wol_image, bg=bgc, borderwidth=0, highlightthickness=0, activebackground=bgc, command=wol)
wol.place(x=b_col, y=row2, anchor="center")

zoom = Button(root, image=zoom_image, bg=bgc, borderwidth=0, highlightthickness=0, activebackground=bgc, command=meeting_choice)
zoom.place(x=b_col, y=row3, anchor="center")

noticeboard = Button(root, image=notice_image, bg=bgc, borderwidth=0, highlightthickness=0, activebackground=bgc, command=notice)
noticeboard.place(x=b_col, y=row4, anchor="center")

zoom_title = Label(root, text="Zoom Web", bg=bgc, fg="black", font=('calibri', 40, 'bold'))
zoom_title.place(x=zoom_col, y=row1, anchor="center")
zoom_info = Label(root, text="If you would like to join a meeting\nother than your congregation assigned ID\nplease enter it below", bg=bgc, fg="black", font=('calibri', 10, 'bold'))
zoom_info.place(x=zoom_col, y=int((row2+row1)/2), anchor="center")
zoom_ent = Entry(root, font=('calibri', 20), justify="center", width=14)
zoom_ent.place(x=zoom_col, y=row2+20, anchor="center")
enter_button_button = Button(root, image=enter_button, bg=bgc, borderwidth=0, highlightthickness=0, activebackground=bgc, width=160, height=60, command=enter_data)
enter_button_button.place(x=zoom_col, y=row3-20, anchor="center")


clock_text = Label(root, bg=bgc, fg="black", font=('calibri', 30, 'bold'))
clock_text.place(x=str(width/2), y=row5, anchor="center")

# Loop
if __name__ == "__main__":
    timed()
    root.mainloop()