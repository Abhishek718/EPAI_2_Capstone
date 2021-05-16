# Welcome to an amazing Python app.

#### This app basically can send customize certificate in a specific format to the number of given users.

There are three ways to call this app:\
  Each time you can either provide --given_time or not by default it will take 30 sec.

  1. either provide path of CSV file that contain (Name, Score, Email).

  2. or you can provide arguments like :

        * given_time = Which will send email in the given gap (by default it is 30 sec).
        * name = Provide name of the person
        * course_name = Provide course name
        * score = Provide score
        * total = Provide total marks
        * email = Provide email

  3) or provide nothing it will take default CSV file.

The default email i used is - "abhishekqwerty919@gmail.com"


#### The basic structure of this app:

  ```bash
    - main.py ................................. (module)
        - read ................................ (package)
            - __init__.py
            - read_csv.py
            - Send_Email ...................... (package)
                - __init__.py
                - create_certificate.py
                - send_email.py
                - Database.py
                - Decorators .................. (package)
                    - __init__.py
                    - decorators.py
```

Now lets talk about this file one by one.

# main.py

```bash
This is main.py.
Basically it helps to call our app through command line.
There are several ways to call this app as explained above.
```
# read

```bash
It is Package that contain __init__.py, read_csv.py and a package named Send_Email.
```

# read_csv.py
```bash
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
```

# Send_Email
```bash
This is also a package present inside read package it includes:
     - __init__.py
     - create_certificate.py
     - send_email.py
     - Database.py 
And another package named Decorators.
```
# create_certificate.py
```bash
This is create_certificate.py file

it will basically create certificate according to the given data.

it can contain 4 areguments:
   1) name of a person
   2) score he or she achieve
   3) email of a person
   4) course_name

and at last store the certificate in Generate certificate folder.
```
# send_email.py
```bash
This is send_email.py file

it is basically use to send an email to the respective person with their details and with attachment as a certificate

it can have 6 arguments:
   1) name of a person
   2) score of a person
   3) email of a person 
   4) given_time which is basically wait time between the mail
   5) course_name
   6) total score of a course
```
# Database.py
```bash
This is a Database.py file

It is basically read the given CSV file.

it is a lazy iterator class and give the len() , next(), repr() like function.
   1) len() - give the no. of lines CSV file have.
   2) next() -  give the second line of CSV file.
   3) repr() - represent some relevent text of the Database class

it has one argument - Path ( the path of the CSV file )
```
# Decorators
```bash
This is another package present inside the Send_Email package it includes:
   1) __init__.py
   2) decoretors.py
```
# decorator.py
```bash
This file contain basically two decorators:
   1) check_connection:
      This is check_connection decorator basically it will check the connection.
      if connection is there then it will return -- "Connected to the Internet"
      if not then -- "No internet connection."
      take argument as a function

   2) timed:
      This is timed decorator basically it will calculate the running time of the given function.
      take argument as a function
```
# __init__.py
```bash
This is basically a file which will immediately run as soon as the respective package is called.
it basically helps a lot in importing packages and modules.
```