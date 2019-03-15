import easygui as g
import sqlite3
conn = sqlite3.connect('kcg6.db')
c = conn.cursor()

#c.execute('''CREATE TABLE s_details (name TEXT,roll_no TEXT,email TEXT,dept TEXT,year TEXT, psw TEXT)''')
#c.execute('''CREATE TABLE e_details (event_title TEXT,type_of_event TEXT,date TEXT,venue TEXT,no_days TEXT,no_part TEXT)''')
#c.execute('''CREATE TABLE w_details (event_type TEXT,event_name TEXT,s_name TEXT,roll_no TEXT,venue TEXT,date TEXT,prize TEXT)''')
def page():
    while 1:
        msg ="Select an option"
        title = "Admin controls"
        choices = ["Add members","Add event","Enter winner details","Generate report","Exit"]
        choice = g.choicebox(msg, title, choices)
        ch = choices.index(choice)
        if ch == 0:
            add_mem()
        elif ch == 1:
            add_eve()
        elif ch == 2:
            add_win()
        elif ch == 4:
            raise SystemExit()
        elif ch==3:
            gen_rep()
def gen_rep():
    msg ="Select a report to generate"
    title = "Generate report"
    choices = ["List of events","Winner details","All student deatils","Specific student report","Exit"]
    choice = g.choicebox(msg, title, choices)
    ch = choices.index(choice)
    if ch==0:
        c.execute('SELECT * FROM e_details')
        de=[]
        de=c.fetchall()
        f1,f2,f3,f4,f5,f6=zip(*de)
        op=True
        i=0
        l=len(f1)
        while op==True and i<l:
           
            msg=""
            msg+="Event name: {}. \n\n".format(f1[i])
            msg+="Type of event: {}. \n\n".format(f2[i])
            msg+="Date: {}. \n\n".format(f3[i])
            msg+="Venue: {}. \n\n".format(f4[i])
            msg+="Number of days: {}. \n\n".format(f5[i])
            msg+="Number of participants: {}. \n\n".format(f6[i])
            i=i+1
            op=g.ccbox(msg,title="Event details",choices=('Next','Close'))
        gen_rep()
    elif ch==1:
        c.execute('SELECT * FROM w_details')
        de=[]
        de=c.fetchall()
        f1,f2,f3,f4,f5,f6,f7=zip(*de)
        op=True
        i=0
        l=len(f1)
        while op==True and i<l:
           
            msg=""
            msg+="Event type: {}. \n\n".format(f1[i])
            msg+="Event name: {}. \n\n".format(f2[i])
            msg+="Student name: {}. \n\n".format(f3[i])
            msg+="Roll no: {}. \n\n".format(f4[i])
            msg+="Venue: {}. \n\n".format(f5[i])
            msg+="Date: {}. \n\n".format(f6[i])
            msg+="Prize: {}. \n\n".format(f7[i])
            i=i+1
            op=g.ccbox(msg,title="Winner details",choices=('Next','Close'))
        gen_rep()    
        
    elif ch==2:
        c.execute('SELECT * FROM s_details')
        de=[]
        de=c.fetchall()
        f1,f2,f3,f4,f5,f6=zip(*de)
        op=True
        i=0
        l=len(f1)
        while op==True and i<l:
            msg=""
            msg+="Name: {}. \n\n".format(f1[i])
            msg+="Roll number: {}. \n\n".format(f2[i])
            msg+="Email address: {}. \n\n".format(f3[i])
            msg+="Dept: {}. \n\n".format(f4[i])
            msg+="Year: {}. \n\n".format(f5[i])
            msg+="Password: {}. \n\n".format(f6[i])
            i=i+1
            op=g.ccbox(msg,title="Student details",choices=('Next','Close'))
        gen_rep()
    elif ch == 3:
        t= g.enterbox("Enter the roll number of the student")
        rn=[]
        rn.append(t)
        c.execute('SELECT * from s_details where roll_no = ?',rn)
        de=[]
        de=c.fetchall()
        f1,f2,f3,f4,f5,f6=zip(*de)
        msg=""
        msg+="Name: {}. \n\n".format(f1[0])
        msg+="Roll number: {}. \n\n".format(f2[0])
        msg+="Email address: {}. \n\n".format(f3[0])
        msg+="Dept: {}. \n\n".format(f4[0])
        msg+="Year: {}. \n\n".format(f5[0])
        msg+="Password: {}. \n\n".format(f6[0])
        g.msgbox(msg,"Details")
        gen_rep()
    elif ch == 4:
        page()
def add_mem():
    msg = "Enter the student information"
    title = "Add Club members"
    fieldNames = ["Name", "Roll number","Email Address", "Dept", "Year","Password"]
    fieldValues = g.multenterbox(msg, title, fieldNames)
    if fieldValues is None:
        page()
    while 1:
        errmsg = ""
        for i, name in enumerate(fieldNames):
            if fieldValues[i].strip() == "":
              errmsg += "{} is a required field.\n\n".format(name)
        if errmsg == "":
            break 
        fieldValues = g.multenterbox(errmsg, title, fieldNames, fieldValues)
        if fieldValues is None:
            break
    print("Reply was:{}".format(fieldValues))
    
    c.execute('INSERT INTO s_details values(?,?,?,?,?,?)',fieldValues)
    conn.commit()
    page()
def add_eve():
    msg = "Enter the event information"
    title = "Add event"
    fieldNames = ["Event title", "Type of event","Date", "Venue", "Number of days","Number of participants"]
    fieldValues = g.multenterbox(msg, title, fieldNames)
    if fieldValues is None:
        page()
    while 1:
        errmsg = ""
        for i, name in enumerate(fieldNames):
            if fieldValues[i].strip() == "":
              errmsg += "{} is a required field.\n\n".format(name)
        if errmsg == "":
            break 
        fieldValues = g.multenterbox(errmsg, title, fieldNames, fieldValues)
        if fieldValues is None:
            break
    print("Reply was:{}".format(fieldValues))
    c.execute('INSERT INTO e_details values(?,?,?,?,?,?)',fieldValues)
    conn.commit()
    page()
def add_win():
    msg = "Enter the winner information"
    title = "Winner Info"
    fieldNames = ["Event type","Event name", "Student name","Roll number", "Venue","Date", "Prize"]
    fieldValues = g.multenterbox(msg, title, fieldNames)
    if fieldValues is None:
        page()
    while 1:
        errmsg = ""
        for i, name in enumerate(fieldNames):
            if fieldValues[i].strip() == "":
              errmsg += "{} is a required field.\n\n".format(name)
        if errmsg == "":
            break 
        fieldValues = g.multenterbox(errmsg, title, fieldNames, fieldValues)
        if fieldValues is None:
            break
    print("Reply was:{}".format(fieldValues))
    c.execute('INSERT INTO w_details values(?,?,?,?,?,?,?)',fieldValues)
    conn.commit()
    page()
def login():
    image = "cse_1.png"
    msg = "\t\t\t\t    Login"
    choices = ["Student","Admin","Exit"]
    reply = g.buttonbox(msg, image=image, choices=choices)
    if reply == "Student":
        u_name = g.enterbox("Enter user name",title = "Username")
        psw = g.passwordbox("Enter the password",title = "Password")
        c.execute('SELECT roll_no,psw  FROM s_details')
        us=[]
        us=c.fetchall()
        uss, pas = zip(*us)
        rn=u_name
        if u_name in uss:
            i=uss.index(u_name)
            if psw==pas[i]:
                g.msgbox("Login success","Success!","Continue")
                c.execute("SELECT * FROM s_details WHERE roll_no = '%s'"%rn)
                de=[]
                de=c.fetchall()
                f1,f2,f3,f4,f5,f6=zip(*de)
                msg=""
                msg+="Name: {}. \n\n".format(f1[0])
                msg+="Roll number: {}. \n\n".format(f2[0])
                msg+="Email address: {}. \n\n".format(f3[0])
                msg+="Dept: {}. \n\n".format(f4[0])
                msg+="Year: {}. \n\n".format(f5[0])
                msg+="Password: {}. \n\n".format(f6[0])
                g.msgbox(msg,"Details","Exit")
            else:
                g.msgbox("Login failed, account does not exist. \n Please try again.")
                login()
    elif reply == "Admin":
        u_name = g.enterbox("Enter user name",title = "Username")
        psw = g.passwordbox("Enter the password",title = "Password")
        if u_name == "1" and psw == "1":
            g.msgbox("Welcome :)","Login successful")
            page()
        else:
            g.msgbox("Wrong details, please try again :(","Login failed")
            login()
    else:
        raise SystemExit()
login()
conn.commit()
conn.close()
