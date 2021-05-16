from .Send_Email.Decorators import *
from .Send_Email.Database import *
from .Send_Email import *



@timed
@check_connection
def read_csv_func(path="Csv_file.csv",given_time = 30,name = 0,course_name = 0,score = 0,total = 0,email = 'abhishekqwerty919@gmail.com'):
    '''
    This is a read_csv.py file 

    it also contains two decorators timed and check connection

    this function can take 7 arguments:
        1) path of Csv file
        2) given_time which decides the wait time between the mails
        3) name of a person
        4) course_name 
        5) score he or she achieve
        6) total score of a course
        7) email of the person

    this function basically call create_certificate and send_email function with their respective arguments

    '''
    if name!= 0:
        name = name.title()
        create_certificate(name = name,score = score,email = email,course_name = course_name)
        send_emails(name = name,score = score,email = email,given_time = 30,course_name = course_name,total = total)
    else:
        d_ob = Database(path)
        s = len(d_ob)
        def rec(i=0):
            if i>=(s-1):
                return
            next_line = next(d_ob)
            name = next_line.Name.title()
            score = next_line.Score
            email = next_line.Email
            create_certificate(name,score,email)
            send_emails(name,score,email,given_time = given_time)
            i+=1
            return rec(i)
        rec()