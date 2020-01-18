# -*- coding: utf-8 -*-
"""
Karoll Quijano - kquijano

ABE 651 - Environmental Informatics

Think Python - Chapter 3
Exercise 3.2

"""


def do_twice(f): 
    ''' Prints a function twice '''
    f()
    f()
    
def print_spam(): 
    ''' Prints spam '''
    print('spam')
    

do_twice(print_spam)

############# Modify do_twice function  ###################

def print_twice(s): 
    ''' Prints an argument twice '''
    print(s)
    print(s)
    

def do_twice(f,s):  
    ''' Prints function f twice using the argument s '''
    f(s)



do_twice(print_twice,"spam")  


def do_four(f,s): 
    ''' Prints function f four times  using the argument s '''
    f(s)
    f(s)

do_four(print_twice, 'spam')
