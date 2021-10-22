import getpass
import os

usr = str(getpass.getuser())

directory = "multi_link_app"
icon = "/data/links.ico"
app1 = "main.py"
app1name = "Congregation Links"
app1name2 = app1name.lower().replace(" ","_")+".desktop"
app2 = "settings.py"
app2name = "Links Settings"
app2name2 = app2name.lower().replace(" ","_")+".desktop"

f1 = open(app1name2, "x")
f2 = open(app2name2, "x")

mv1 = "mv " + app1name2 + " ~/Desktop/"
mv2 = "mv " + app2name2 + " ~/Desktop/"

ex1 = "chmod +x ~/Desktop/" + app1name2
ex2 = "chmod +x ~/Desktop/" + app2name2
tru1 = "gio set ~/Desktop/" + app1name2 + " metadata::trusted true"
tru2 = "gio set ~/Desktop/" + app2name2 + " metadata::trusted true"

if __name__ == '__main__':
    f1.write("[Desktop Entry]\nVersion=1.0\nName=" + app1name + "\nComment=Opens application\nExec=python3 /home/" + usr + "/" + directory + "/" + app1 + "\nIcon=/home/" + usr + "/" + directory + "/" + icon + "\nTerminal=false\nType=Application\nCategories=Application;")
    f1.write("[Desktop Entry]\nVersion=1.0\nName=" + app1name + "\nComment=Opens application\nExec=python3 /home/" + usr + "/" + directory + "/" + app1 + "\nIcon=/home/" + usr + "/" + directory + "/" + icon + "\nTerminal=false\nType=Application\nCategories=Application;")
    os.system(mv1)
    os.system(mv2)
    os.system("cd")
    os.system(ex1)
    os.system(ex2)
    os.system(tru1)
    os.system(tru2)