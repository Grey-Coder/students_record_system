import mysql.connector as qw
import os
print('Welcome')
print('Please wait .........')
for i in range(0,1000000):
    pass
print('Loading..........')
for i in range(0,10000000):
    pass
qwe='''If you have MySQL installed, Press 1
else Press 2'''
print(qwe)
u= int(input('Enter ur choice:'))
if u==2:
    os.system('mysql-5.5.60-win32.msi')
    print('Please restart the program')
elif u==1:
    print('Loading...')
    for i in range(0,10000000):
        pass
    print('Checking....')
    for i in range(0,10000000):
        pass
    p=input('Enter your SQL password= ')
    print('verifing user..')
    for i in range(0,10000000):
        pass
    #global xxx
    #xxx=3
    def sim():
        #if xxx>=1:
            try:
                c= qw.connect(host='localhost',user='root',passwd=p)
                if c.is_connected() :
                    print('Successfully connected!')
                    for i in range(0,10000000):
                        pass
                    x=c.cursor()
                    print('Please select a option')
                    print('If you are a new user, Press 1')
                    print('if you are a old user, Press 2')
                    se=int(input('Enter your choice:'))
                    if se==1:
                        x.execute('create database devildepz')
                        x.execute('use devildepz')
                        x.execute('create table class_XII (Sno integer unique , Name varchar(60), Rollno integer, AdmissionNo integer primary key, Address varchar(90), Father_or_Mother_Name varchar(60), Birthday varchar(20), Sex varchar(6), Caste varchar(10), Mobile varchar(14))')
                    elif se==2:
                        x.execute('use devildepz')
                    
                
                    def add():
                    
                        sno=int(input('Enter Sno.= '))
                        nam=input('Enter Name= ')
                        roll=int(input('Enter Roll No.= '))
                        adm=int(input('Enter Admission No.= '))
                        ad=input('Enter the Address= ')
                        FM=input('Enter Father/Mothers Name= ')
                        Birthday=input('Enter Date of Birth = ')
                        sex=input('Enter Sex= ')
                        cast=input('Enter Caste= ')
                        mob=input('Enter Mobile No.= ')
                        try:
                            x.execute("insert into class_XII(Sno, Name, Rollno, AdmissionNo, Address, Father_or_Mother_Name, Birthday,Sex, Caste, Mobile) values({},'{}',{},{},'{}','{}','{}','{}','{}','{}')".format(sno,nam,roll,adm,ad,FM,Birthday,sex,cast,mob))    
                            c.commit()
                            print('Your data will be added')

                        except:
                            print('Error!')
                    def update():
                        print('Sno, Name, Rollno, AdmissionNo, Address, Father_or_Mother_Name, Birthday,Sex, Caste, Mobile')
                        print('This are the field names')
                        try:
                            kl=input('Enter the feild name to be changed(i.e. where):')
                            kp=input('Enter the field name that u want to update(i.e. set):')
                            print('Select the data type')
                            print('1. For integer')
                            print('2. For String')
                            ui=int(input('Enter your choice='))
                            if ui==1:
                                ki=int(input('Enter the Data in Integer='))
                                jh=int(input('Enter the incorrect data='))
                            elif ui==2:
                                ki=input('Enter the Data in string=')
                                jh=input('Enter the incorrect data=')
                            else:
                                print('Incorrect Choice')
                            x.execute('update class_XII set {ac}={ab} where {ad}={ae}'.format(ac=kp,ab=ki,ad=kl,ae=jh))
                            c.commit()
                            print('Successfully updated')
                        except:
                            print('Error!')
                            
                    def view():
                        print('Select your choice')
                        print('1. To view the whole data')
                        print('2. To view the latest data added')
                        print('3. To view customised data')
                        ty=int(input('Enter your choice:'))
                        if ty==1:
                            x.execute('select * from class_XII')
                            data=x.fetchall()
                            count=x.rowcount
                            print('Total number of data retrived:',count)
                            for row in data:
                                print(row)
                        elif ty==2:
                            x.execute('select * from class_XII')
                            data=x.fetchone()
                            count=x.rowcount
                            print('Total number of data retrived:',count)
                            print(data)
                        elif ty==3:
                            x.execute('select * from class_XII')
                            ass=int(input("Enter the number of data you want to retrive="))
                            data=x.fetchmany(ass)
                            count=x.rowcount
                            print('Total number of data retrived:',count)
                            for row in data:
                                print(row)
                        else:
                            print('Incorrect Choice')

                        
                    def delete():
                        print('Select the data type')
                        print('1. For particular Row')
                        print('2. For Whole table data')
                        print('3. For Whole database (Caution: Your whole database will be deleted)')
                        xyz=int(input('Enter your Choice='))
                        if xyz==1:
                                de=int(input('Enter the Serial No. of that particular row:'))
                                try:
                                    x.execute('delete from class_XII where Sno={}'.format(de))
                                    
                                    print('Successfully deleted')
                                except:
                                    print('Error!')
                                
                        elif xyz==2:
                                try:
                                    x.execute('delete from class_XII')
                                    print('Successfully deleted')
                                except:
                                    print('Error!')
                        elif xyz==3:
                                print('Caution!!!!!!!!  This will delete the database and \n you have to restart the program as new user')
                                p=input('Do you want to continue(y/n):')
                                if p=='y' or 'Y':
                                    try:
                                        x.execute('drop database devildepz')
                                        print('successfully deleted')
                                    except:
                                        print('Error!')
                                else:
                                    pass
                        else:
                            print('Incorrect Data')

                    #__main__
                    
                    print('This software is subjected to copyright')
                    print("KENDRIYA VIDYALAYA ONGC SRIKONA COMPUTER SCIENCE OFFICIAL")
                    def main():

                        print("1.Add")
                        print("2.Update")
                        print("3.View")
                        print("4.Delete")
                        print("5.Exit")
                        ch=int(input("Enter your choice (1-5):"))
                        if ch==1 :
                             add()
                             main()
                        elif ch==2 :
                             update()
                             main()
                        elif ch==3 :
                             view()
                             main()
                        elif ch==4 :
                             delete()
                             main()
                        elif ch==5 :
                            print('Thanks for using my project')
                            print('Created By Amit')
                            for i in range(0,40000000):
                                pass
                        else:
                            print('Invaild input')
                            main()
                    main()
            except:
                print('Not Connected, the entered was incorrect')
                #print("Enter the correct password")
                print("Restart the program & enter the correct password")
                #xxx-=1
                #print('Only',xxx,'attempt(s) are left')

        #else:
            #print("Your attempts are over \n Try again later.")
    sim()
        
