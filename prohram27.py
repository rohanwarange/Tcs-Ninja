### -*- coding: utf-8 -*-
##"""
##Created on Fri Jul  9 11:19:51 2021
##
##@author: ROHAN
##"""
##
##Question 11
##
##Consider the below series:
##1, 2, 1, 3, 2, 5, 3, 7, 5, 11, 8, 13, 13, 17…..
##
##This series is a mixture of 2 series fail the odd terms in this series form a Fibonacci series and all the 
#even terms are the prime numbers in ascending order
##
##Write a program to find the Nth term in this series
##
##The value N in a positive integer that should be read from mm. The Nth term that is calculated by the
# program should be written to STDOUT Otherthan the value of Nth term , no other characters / string or message 
# should be written to STDOUT.
##
##For example, when N:14, the 14th term in the series is 17 So only the value 17 should be printed to STDOUT

n=int(input())
a=1
b=2
if n%2==0:
    n=n//2
    print(b+n//2)
else:
    n=n//2
    print(n-1)
    