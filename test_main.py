
import pytest
import random
import string
import os
import os.path
from os import path
import pathlib
import inspect
import re
import math
import time
import main
import read
import read.Send_Email as Send_Email
import read.Send_Email.Decorators as Decorator_pack
import read.read_csv as read_csv
import read.Send_Email.create_certificate as create_certificate
import read.Send_Email.send_email as send_email
import read.Send_Email.Database as database
import read.Send_Email.Decorators.decorators as decorators
# import read.Send_Email.Decorators.decorators.check_connection as check_connection
# import read.Send_Email.Decorators.decorators.timed as timed


README_CONTENT_CHECK_FOR = [
    'read',
    'read_csv.py',
    'Send_Email',
    'create_certificate.py',
    'send_email.py',
    'Database.py',
    'Decorators',
    'decorator.py',
    '__init__.py',
]



def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 300 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 8

def test_function_name_had_cap_letter_main():
    functions = inspect.getmembers(main, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_function_name_had_cap_letter_read_csv():
    functions = inspect.getmembers(read_csv, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_function_name_had_cap_letter_create_certificate():
    functions = inspect.getmembers(create_certificate, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_function_name_had_cap_letter_send_email():
    functions = inspect.getmembers(send_email, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_function_name_had_cap_letter_database():
    functions = inspect.getmembers(database, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_function_name_had_cap_letter_decorators():
    functions = inspect.getmembers(decorators, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_module_read_csv_has_doc():
    doc = read_csv.read_csv_func.__doc__
    assert doc != None,"it does not contain docstring"

def test_module_create_certificate_has_doc():
    doc = create_certificate.__doc__
    assert doc != None,"it does not contain docstring"

def test_module_send_email_has_doc():
    doc = send_email.send_emails.__doc__
    assert doc != None,"it does not contain docstring"

def test_module_send_email_has_doc():
    doc = send_email.send_emails.__doc__
    assert doc != None,"it does not contain docstring"

def test_module_database_has_doc():
    doc = database.__doc__
    assert doc != None,"it does not contain docstring"

def test_module_decorators_check_connection_has_doc():
    doc = decorators.check_connection.__doc__
    assert doc != None,"it does not contain docstring"

def test_module_decorators_timed_has_doc():
    doc = decorators.timed.__doc__
    assert doc != None,"it does not contain docstring"

def test_for_init_file_read():
    assert path.exists(os.path.join(pathlib.Path().absolute(),"read","__init__.py")) == True, "__init__ file does not exist in read package"

def test_for_init_file_send_email():
    assert path.exists(os.path.join(pathlib.Path().absolute(),"read","Send_Email","__init__.py")) == True, "__init__ file does not exist in send_email package"

def test_for_init_file_decorators():
    assert path.exists(os.path.join(pathlib.Path().absolute(),"read","Send_Email","Decorators","__init__.py")) == True, "__init__ file does not exist in Decorators package"

def test_for_main_module():
    assert path.exists(os.path.join(pathlib.Path().absolute(),"main.py")) == True, "main module does not exists"

def test_for_read_csv_module():
    assert path.exists(os.path.join(pathlib.Path().absolute(),"read","read_csv.py")) == True, "read_csv module does not exists"

def test_for_create_certificate_module():
    assert path.exists(os.path.join(pathlib.Path().absolute(),"read","Send_Email","create_certificate.py")) == True, "create_certificate module does not exists"

def test_for_send_email_module():
    assert path.exists(os.path.join(pathlib.Path().absolute(),"read","Send_Email","send_email.py")) == True, "send_email module does not exists"

def test_for_Database_module():
    assert path.exists(os.path.join(pathlib.Path().absolute(),"read","Send_Email","Database.py")) == True, "Database module does not exists"

def test_for_Decorators_module():
    assert path.exists(os.path.join(pathlib.Path().absolute(),"read","Send_Email","Decorators","decorators.py")) == True, "Decorators module does not exists"

def test_for_generated_certificate_folder():
    assert path.exists(os.path.join(pathlib.Path().absolute(),"generated_certificate")) == True, "generated_certificate folder does not exists"

def  test_database_len():
    d_obj = database("Csv_file.csv")
    assert len(d_obj) == 11,"len function is not working properly"

def  test_database_next_name():
    d_obj = database("Csv_file.csv")
    assert next(d_obj).Name == "Abhishek","it did not iterate CSV file"

def  test_database_next_score():
    d_obj = database("Csv_file.csv")
    assert next(d_obj).Score == "97","it did not iterate CSV file"

def  test_database_next_email():
    d_obj = database("Csv_file.csv")
    assert next(d_obj).Email == "abhishekqwerty919@gmail.com","it did not iterate CSV file"

def  test_database_next_iterate_name():
    d_obj = database("Csv_file.csv")
    next(d_obj)
    assert next(d_obj).Name == "Naman","it did not iterate CSV file"

def  test_database_next_iterate_score():
    d_obj = database("Csv_file.csv")
    next(d_obj)
    assert next(d_obj).Score == "96","it did not iterate CSV file"

def  test_database_next_iterate_email():
    d_obj = database("Csv_file.csv")
    next(d_obj)
    assert next(d_obj).Email == "a.bhishekqwerty919@gmail.com","it did not iterate CSV file"

def  test_database_next_last_iterate_name():
    d_obj = database("Csv_file.csv")
    for i in range(len(d_obj)-2):
        next(d_obj)
    assert next(d_obj).Name == "Rahul","it did not iterate CSV file"

def  test_database_next_last_iterate_score():
    d_obj = database("Csv_file.csv")
    for i in range(len(d_obj)-2):
        next(d_obj)
    assert next(d_obj).Score == "88","it did not iterate CSV file"

def  test_database_next_last_iterate_email():
    d_obj = database("Csv_file.csv")
    for i in range(len(d_obj)-2):
        next(d_obj)
    assert next(d_obj).Email == "abhishekq.werty919@gmail.com","it did not iterate CSV file"

def  test_database_header():
    d_obj = database("Csv_file.csv")
    assert d_obj.header() == ['Name', 'Score', 'Email'],"it did not show required header"

def  test_database_header_name():
    d_obj = database("Csv_file.csv")
    assert d_obj.header()[0] == 'Name',"it did not show required header name"

def  test_database_header_score():
    d_obj = database("Csv_file.csv")
    assert d_obj.header()[1] == 'Score',"it did not show required header score"

def  test_database_header_email():
    d_obj = database("Csv_file.csv")
    assert d_obj.header()[2] == 'Email',"it did not show required header Email"

def  test_database_repr():
    d_obj = database("Csv_file.csv")
    assert d_obj.__repr__() == 'Database(Size=11)',"it did not show required header Email"

def test_create_certificate():
    create_certificate("Aditi","99","abhishekqwerty919@gmail.com")
    assert path.exists(os.path.join(pathlib.Path().absolute(),"generated_certificate","Aditi.jpg")) == True, "create certificate did not create certificate"

def test_create_certificate_store_generated_folder():
    create_certificate("Aditi","99","abhishekqwerty919@gmail.com")
    assert path.exists(os.path.join(pathlib.Path().absolute(),"generated_certificate","Aditi.jpg")) == True, "create certificate did not create certificate"

def test_create_certificate_not_work_again():
    output = create_certificate("Aditi","99","abhishekqwerty919@gmail.com")
    assert output == "Already Exists", "it is creating certificate again"


def test_read_package():
    output = read.__package__
    assert output == "read","does not give desired output"

def test_send_email_package():
    output = Send_Email.__package__
    assert output == "read.Send_Email","does not give desired output"

def test_decorators_package():
    output = Decorator_pack.__package__
    assert output == "read.Send_Email.Decorators","does not give desired output"

def test_read_file():
    output = read.__file__
    assert output == os.path.join(pathlib.Path().absolute(),"read","__init__.py"),"does not give desired output"

def test_send_email_file():
    output = Send_Email.__file__
    assert output == os.path.join(pathlib.Path().absolute(),"read","Send_Email","__init__.py"),"does not give desired output"

def test_decorators_file():
    output = Decorator_pack.__file__
    assert output == os.path.join(pathlib.Path().absolute(),"read","Send_Email","Decorators","__init__.py"),"does not give desired output"


