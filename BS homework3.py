#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 19:32:09 2019

@author: wuyanxu
"""

import os
import csv
from collections import Counter

csvpath = os.path.join('/Users/wuyanxu/Desktop/03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print("CSV Header: {csv_header}")
    count = 0
    total_profit = 0
    new_list = []
    profit = []
    tmp = 0
    total_diff = 0
    change = []
    
    for row in csvreader:
        print(row)
        print(count)
        count = count + 1 
        profit.append(row[1])
        print(profit)
        total_profit = total_profit +int(row[1])
        if tmp != 0:
            difference = int(row[1]) - tmp
        else:
            difference = 0
        total_diff = total_diff + difference
        print(total_profit)
        new_list.append(row[1])
        print(new_list)
        tmp = int(row[1])
        print(total_diff)
        average_change = total_diff / 85
        print(average_change)
        change.append(difference)
        print(change)
        print(max(change))
        print(min(change))
        
##PyPoll
csvpath_poll = os.path.join('/Users/wuyanxu/Desktop/03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv')
with open(csvpath_poll, newline='') as csvfile:


    csvreader_poll = csv.reader(csvfile, delimiter=',')

    print(csvreader_poll)

 
    csv_header_poll = next(csvreader_poll)
    print(f"CSV Header: {csv_header_poll}")
    namelist = []
    count = 0
    stat = Counter()
    khan = []
    correy = []
    li = []
    Tooley = []
    for row in csvreader_poll:
        print(row)
        print(count)
        count = count + 1
        stat[row[2]] += 1 
        namelist.append(row[2])
        
    print(count) 
    print(set(namelist))
    #print(stat)
    
    for row in namelist:
      if row == "Khan":
        khan.append(row)
    print(len(khan))
    
    for row in namelist:
        if row == "Correy":
            correy.append(row)
    print(len(correy))
    
    for row in namelist:
        if row == "Li":
            li.append(row)
    print(len(li))
    
    for row in namelist:
        if row == "O'Tooley":
            Tooley.append(row)
    print(len(Tooley))
    
    khanvote = len(khan) / count  
    print(khanvote)
   
    correyvote = len(correy) / count 
    print(correyvote)
   
    livote = len(li) / count
    print(livote)
   
    tooleyvote = len(Tooley) / count 
    print(tooleyvote)
   
    #winner khan.