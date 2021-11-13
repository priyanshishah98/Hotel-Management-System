def data_entry():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, password TEXT)')
    username = uname.get()
    password = passwd.get()

    result = c.execute("SELECT * FROM userstable")

    if username != '' or password != '':

        for i in result:
            if i[0] == username:
                tkinter.messagebox.showerror("DUPLICATE", "USER ALREADY EXISTS!")
                break
        else:
            c.execute('INSERT INTO userstable (username, password) VALUES(?, ?)',(username,password))
            conn.commit()
            c.close()
            conn.close()
            another_clear()
            tkinter.messagebox.showinfo("Success", "User Created Successfully,\nPlease restart application.")

    else:
        tkinter.messagebox.showerror("ERROR", "Fill both fields!")