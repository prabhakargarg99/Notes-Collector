from tkinter import *
import os


def destroy_screen2():
    screen4.destroy()


def destroy_screen3():
    screen5.destroy()


def saved():
    screen10 = Toplevel(screen)
    
    screen10.title("Saved")
    screen10.geometry("100x100")

    Label(screen10, text="").pack()
    Label(screen10, text="Saved").pack()

    filename_entry.delete(0, END)
    notes_entry.delete(0, END)


def save():
    filename = raw_filename.get()
    notes = raw_notes.get()

    data = open(filename, "w")
    data.write(notes)
    data.close()

    saved()


def create_notes():
    global raw_notes
    global notes_entry
    global raw_filename
    global filename_entry
    
    raw_filename = StringVar()
    raw_notes = StringVar()

    screen9 = Toplevel(screen)
    
    screen9.title("Info")
    screen9.geometry("300x250")

    Label(screen9, text="").pack()
    Label(screen9, text="Enter a filename for the note below :").pack()
    
    filename_entry = Entry(screen9, textvariable=raw_filename)
    filename_entry.pack()
    
    Label(screen9, text="").pack()
    Label(screen9, text="Enter the notes for the file below :").pack()
    
    notes_entry = Entry(screen9, textvariable=raw_notes)
    notes_entry.pack()
    
    Label(screen9, text="").pack()
    Button(screen9, text="Save", command=save).pack()


def view():
    filename1 = raw_filename1.get()
    data = open(filename1, "r")
    data1 = data.read()

    screen12 = Toplevel(screen)
    
    screen12.title("Notes")
    screen12.geometry("400x400")

    Label(screen12, text="").pack()
    Label(screen12, text=data1).pack()

    filename_entry1.delete(0, END)


def delete():
    filename2 = raw_filename2.get()
    os.remove(filename2)

    screen14 = Toplevel(screen)
    
    screen14.title("Notes")
    screen14.geometry("400x400")

    Label(screen14, text="").pack()
    Label(screen14, text=filename2+" removed").pack()

    filename_entry3.delete(0, END)


def view_notes():
    global raw_filename1
    global filename_entry1
    
    raw_filename1 = StringVar()

    screen11 = Toplevel(screen)
    
    screen11.title("Info")
    screen11.geometry("250x250")

    all_files = os.listdir()
    
    Label(screen11, text="").pack()
    Label(screen11, text="Please use one of the filename below :").pack()
    Label(screen11, text="").pack()
    Label(screen11, text=all_files).pack()
    
    filename_entry1 = Entry(screen11, textvariable=raw_filename1)
    filename_entry1.pack()
    
    Label(screen11, text="").pack()
    Button(screen11, text="OK", command=view).pack()


def delete_notes():
    global raw_filename2
    global filename_entry3
    
    raw_filename2 = StringVar()
    screen13 = Toplevel(screen)
    
    screen13.title("Info")
    screen13.geometry("250x250")

    all_files = os.listdir()
    
    Label(screen13, text="").pack()
    Label(screen13, text="Please use one of the filename below :").pack()
    Label(screen13, text="").pack()
    Label(screen13, text=all_files).pack()
    
    filename_entry3 = Entry(screen13, textvariable=raw_filename2)
    filename_entry3.pack()
    
    Label(screen13, text="").pack()
    Button(screen13, text="OK", command=delete).pack()


def session():
    screen8 = Toplevel(screen)
    
    screen8.title("Dashboard")
    screen8.geometry("400x400")

    Label(screen8, text="").pack()
    
    Label(screen8, text="Welcome To The Dashboard").pack()
    Label(screen8, text="").pack()
    
    Button(screen8, text="Create Note", command=create_notes).pack()
    Label(screen8, text="").pack()
    
    Button(screen8, text="View Note", command=view_notes).pack()
    Label(screen8, text="").pack()
    
    Button(screen8, text="Delete Note", command=delete_notes).pack()


def login_success():
    session()


def password_not_matched():
    global screen4
    
    screen4 = Toplevel(screen)
    
    screen4.title("Login Fail")
    screen4.geometry("150x100")

    Label(screen4, text="").pack()
    Label(screen4, text="Password Doesn't Match", fg="green", font=("Calibri", 11)).pack()
    Label(screen4, text="").pack()
    
    Button(screen4, text="OK", command=destroy_screen2).pack()


def user_not_found():
    global screen5
    
    screen5 = Toplevel(screen)
    
    screen5.title("Login Fail")
    screen5.geometry("150x100")

    Label(screen5, text="").pack()
    Label(screen5, text="User Not Found", fg="green", font=("Calibri", 11)).pack()
    Label(screen5, text="").pack()
    
    Button(screen5, text="OK", command=destroy_screen3).pack()


def register_user():
    username_info = username.get()
    password_info = password.get()
    
    file = open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="").pack()
    Label(screen1, text="Registration Sucessful", fg="green", font=("Calibri", 11)).pack()


def login_user():
    username_info1 = username_verify.get()
    password_info1 = password_verify.get()

    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    
    if username_info1 in list_of_files:
        file1 = open(username_info1, "r")
        verify = file1.read().splitlines()
        
        if password_info1 in verify:
            Label(screen2, text="Login Sucessful", fg="green", font=("Calibri", 11)).pack()
            login_success()
            
        else:
            password_not_matched()
            
    else:
        user_not_found()


def register():
    print("Register Session Started")
    
    global screen1
    global username
    global password
    global username_entry
    global password_entry
    
    screen1 = Toplevel(screen)
    
    screen1.title("Register")
    screen1.geometry("300x250")
    
    username = StringVar()
    password = StringVar()

    Label(screen1, text="").pack()
    Label(screen1, text="Please Enter Details Below :").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username").pack()
    
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    
    Label(screen1, text="").pack()
    Label(screen1, text="Password").pack()
    
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width="10", height="1", command=register_user).pack()
    
    screen1.mainloop()


def login():
    print("Login Session Started")
    
    global screen2
    global username_verify
    global password_verify
    global username_entry1
    global password_entry1
    
    screen2 = Toplevel(screen)
    
    screen2.title("Login")
    screen2.geometry("300x250")

    Label(screen2, text="").pack()
    Label(screen2, text="Please Enter Details Below :").pack()
    Label(screen2, text="").pack()
    
    username_verify = StringVar()
    password_verify = StringVar()

    Label(screen2, text="Username").pack()
    
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    
    Label(screen2, text="").pack()
    Label(screen2, text="Password").pack()
    
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width="10", height="1", command=login_user).pack()
    
    screen2.mainloop()


def main_screen():
    global screen
    
    screen = Tk()
    
    screen.geometry("300x250")
    screen.title("Notes 1.0")

    Label(text="Notes 1.0", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    
    Button(text="Login", width="30", height="2", command=login).pack()
    Label(text="").pack()
    
    Button(text="Register", width="30", height="2", command=register).pack()

    screen.mainloop()


if __name__ == "__main__":
    main_screen()
