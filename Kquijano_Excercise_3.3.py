#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Karoll Quijano - kquijano

ABE 651 - Environmental Informatics

Think Python - Chapter 3
Excercise 3.3

"""

# Excercise 3.3.1  - draw a 2*2 grid

def print_four (f):
    ''' Prints four times a function '''
    f()
    f()
    f()
    f()


def print_two(f,g):
    ''' Print two functions '''
    f()
    print_four(g)


def print_first ():
    ''' prints rows with + - '''
    print('+ - - - -', end = ' ')
    print('+ - - - - +' )
    
def print_last ():
    ''' Prints rows with | '''
    print('|        ', end = ' ')
    print('|         |' )

def do_box():
    ''' Combines functions to print a 2*2 box '''
    print_two(print_first, print_last)
    print_two(print_first, print_last)
    print_first()
    
    
do_box()


# Excercise 3.3.2  - draw a 4*4 grid  

def print_first2 ():
    ''' prints rows with + - '''
    print(*3*('+----'), end = ' ')
    print('+ - - - - +' )
    
def print_last2 ():
    ''' Prints rows with | '''
    print(*3*('|    '), end = ' ')
    print('|         |' )



def do_box4():
    ''' Combines functions to print a 4*4 box '''
    print_two(print_first2, print_last2)
    print_two(print_first2, print_last2)
    print_two(print_first2, print_last2)
    print_two(print_first2, print_last2)
    print_first2()
    
   
do_box4()