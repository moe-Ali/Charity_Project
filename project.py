import re
from datetime import datetime

def first_page():
    try:
        print("\n$$ Welcome To Charity Projects $$")
        first_input=input("1- Login\n2- Sign up\nEnter choice your: ")
        if int(first_input)==1:
            print("\n##Login page##\n")
            login()
        elif int(first_input)==2:
            print("\n##Sign up page##\n")
            signup()
        else:
            first_page()
    except:
        first_page()


################################# helpful check functions #####################
def check_user_email(x):
    file_user_r=open("user.txt", "r")
    for line in file_user_r:
        if x in line:
            print("!! Already used E-mail !!")
            enter_mail()
        else:
            pass

def check_user_phone(x):
    file_user_r=open("user.txt", "r")
    for line in file_user_r:
        if x in line:
            print("!! Already used phone number !!")
            phone_number()
        else:
            pass

def check_project_title(x):
    file_user_r=open("project.txt", "r")
    for line in file_user_r:
        if x in line:
            print("!! Already used title !!")
            project_create()
        else:
            pass
############################################# signup sub_page functions #########################################
def user_name():
    first_name=input("Please enter first name: ")
    last_name=input("Please enter last name: ")
    file_user=open("user.txt", "a")
    file_user.write("\n"+first_name+" "+last_name+":")
    


def  enter_mail():
        global email
        email = input ("enter Email :" )
        r_email = r'^([a-z]|[0-9]|\-|\_|\+|\.)+\@([a-z]|[0-9]){2,}\.[a-z]{2,}(\.[a-z]{2,})?$'
        if(re.fullmatch(r_email, email)):
            check_user_email(email)
            print("Valid Email")
            file_user=open("user.txt", "a")
            file_user.write(email+":")
        else:
            print("!! Invalid Email !!")
            enter_mail()


def password():
    passwd=input("Please enter password: ")
    passwd_check=input("Please confirm password: ")
    if passwd==passwd_check:
        print("Correct password")
        file_user=open("user.txt", "a")
        file_user.write(passwd+":")
    else:
        print("!! Incorect password !!")
        password()

def phone_number():
    ph_numb=input("Please enter Egyptian phone number: ")
    r_ph_numb = r'^01[0125][0-9]{8}$'
    if(re.fullmatch(r_ph_numb, ph_numb)):
        check_user_phone(ph_numb)
        print("Valid Egyptian phone number")
        file_user=open("user.txt", "a")
        file_user.write(ph_numb+":")
    else:
        print("!! Invalid Egyptian phone number !!")
        phone_number()

############################################# login sub_page functions #########################################
def project():
    try:
        print("\n$$ Welcome $$\n")
        first_input=input("1- Create \n2- View \n3- back \nEnter choice your: ")
        if int(first_input)==1:
            project_create()
            project()
        elif int(first_input)==2:
            project_view()
        elif int(first_input)==3:
            print("")
            first_page()
        else:
            project()
    except:
        project()

def start_date():
    try:
        s_date=input("please Enter project start date as dd-mm-yyyy : ")
        date_object = datetime.strptime(s_date, "%d-%m-%Y")
        return date_object
    except ValueError:
        print("!! Worng start date format !!")
        start_date()

def finish_date():
    try:
        f_date=input("please Enter project finish date as dd-mm-yyyy : ")
        date_object = datetime.strptime(f_date, "%d-%m-%Y")
        return date_object
    except ValueError:
        print("!! Worng start date format !!")
        finish_date()

#################### project functions #########################################
def project_create():
    try:
        print("\n#Now you are creating a new project \n")
        title=input("Please Enter project title: ")
        check_project_title(title)
        details=input("Please Enter project details: ")
        total_target=input("Please Enter project total target: ")
        s_date=start_date()
        f_date=finish_date()
        if s_date > f_date:
            print("!! Error in date !!")
            project_create()
        else:
            file_project_a=open("project.txt","a")
            file_project_a.write("\n"+login_email+":"+title+":"+details+":"+total_target+":"+str(s_date).split(" ")[0]+":"+str(f_date).split(" ")[0]+":")
    except:
        project_create()
    # project_view()

def project_view():
    try:
        print("\n#Here is all the projects:\n")
        file_project_r=open("project.txt","r")
        index=0
        index_picked=0
        index_list=[]
        for line in file_project_r:
            if index==0:
                pass
            else:
                print(str(index)+" "+line.split(":")[1])
                index_list.append(line.split(":")[1])
            index+=1
        picked_index=int(input("Please enter index: "))
        file_project_r_1=open("project.txt","r")
        for line in file_project_r_1:
            if picked_index>len(index_list):
                print("!! Please enter correct index !!")
                project_view()
            elif index_picked==picked_index:
                print("\n#Here is the project you pick informations:\n")
                print("Title: "+line.split(":")[1])
                print("Details: "+line.split(":")[2])
                print("Total target: "+line.split(":")[3])
                print("Star date: "+line.split(":")[4])
                print("finish date: "+line.split(":")[5])
                project()
            else:
                pass
            index_picked+=1
        project()
    except:
        project_view()
##################### main page functions ################################3
def login():
    global login_email
    login_email=input("Please enter your E-mail: ")
    login_passwd=input("Please enter your password: ")
    file_user_r=open("user.txt", "r")

    # for line in file_user_r.readlines():
    #     line_list=line.split(":")
    #     if login_email ==line_list[1] and login_passwd ==line_list[2]:
    #         project()
    #     else:
    #         pass
    # print("E-mail or Password incorect")
    # login()

    pass_mail_dic={}
    for line in file_user_r.readlines():
        line_list=line.split(":")
        pass_mail_dic[line_list[1]]=line_list[2]
    if pass_mail_dic.get(login_email)==login_passwd:
        project()
    else:
        print("!! E-mail or Password incorect !!")
        login()
    
    
def signup():
    try:
        user_name()
        enter_mail()
        password()
        phone_number()
    except KeyboardInterrupt:
        print("\n\n!!Key Interrupt used!!\n\n")
        file_user_r=open("user.txt","r")
        read_lines=file_user_r.readlines()
        for line in read_lines:
            line_list=line.split(":")
            if line_list[1]==email:
                i=read_lines.index(line)
                with open("user.txt","w") as f:
                    for line in read_lines:
                        if read_lines.index(line) !=i:
                            f.write(line)
        exit()
    print("Please log in")
    login()

############################ call function #####################
first_page()