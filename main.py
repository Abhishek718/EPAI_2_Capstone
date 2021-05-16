import argparse
import read.read_csv 


'''
This is main.py
Basically it helps to call our app through command line
There are several ways to call this app:

- you can call this app by three way :
  Each time you can either provide --given_time or not by default it will take 30 sec

  1) either provide path of CSV file that contain (Name, Score, Email)

  2) or you can provide arguments like :
        --given_time = Which will send email in the given gap (by default it is 30 sec)
        --name = Provide name of the person
        --course_name = Provide course name
        --score = Provide score
        --total = Provide total marks
        --email = Provide email

  3) or provide nothing it will take default CSV file
'''

print()
print("Welcome to Python app that Supports certificate generation and sending email ")
print("-----------------------------------------------------------------------------------------------------")
print()
print("you can call this app by three way :")
print("    Each time you can either provide --given_time or not by default it will take 30 sec")
print("-----------------------------------------------------------------------------------------------------")
print()
print("either provide path of CSV file that contain (Name, Score, Email)")
print("-----------------------------------------------------------------------------------------------------")
print()
print("or you can provide arguments like :")
print("    --given_time = Which will send email in the given gap (by default it is 30 sec)")
print("    --name = Provide name of the person")
print("    --course_name = Provide course name")
print("    --score = Provide score")
print("    --total = Provide total marks")
print("    --email = Provide email")
print("-----------------------------------------------------------------------------------------------------")
print()
print("or provide nothing it will take default CSV file")
print()



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='from here you can call')
    parser.add_argument('--path', type=str, help='you can provide path for the CSV file')
    parser.add_argument('--given_time', type=int, help='ccan provide time duration also')
    parser.add_argument('--name', type=str, help='provide name')
    parser.add_argument('--course_name', type=str, help='can provide course name')
    parser.add_argument('--score', type=str, help='provide score')
    parser.add_argument('--total', type=str, help='give total marks')
    parser.add_argument('--email', type=str, help='provide genuine email id')


    args = parser.parse_args()

    print("=====================================================")
    path = args.path
    print("path = {}".format(path))
    given_time = args.given_time
    print("given_time = {}".format(given_time))
    name = args.name
    print("name = {}".format(name))
    course_name = args.course_name
    print("course_name = {}".format(course_name))
    score = args.score
    print("score = {}".format(score))
    total = args.total
    print("total = {}".format(total))
    email = args.email
    print("email = {}".format(email))
    
    print("=====================================================")


    if path != None:
        if given_time != None:
            read.read_csv.read_csv_func(path = path, given_time = given_time)
        else:
            read.read_csv.read_csv_func(path = path)

    elif name != None:
        if given_time != None:
            read.read_csv.read_csv_func(given_time = given_time,name = name,course_name = course_name,score = score,total = total,email = email)
        else:
            read.read_csv.read_csv_func(name = name,course_name = course_name,score = score,total = total,email = email)

    else:
        if given_time != None:
            read.read_csv.read_csv_func(given_time = given_time)
        else:
            read.read_csv.read_csv_func()