#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from collections import Counter


# In[2]:


heros = pd.read_csv("/Users/wuyanxu/Desktop/CWCL201901DATA4/04-Pandas/Homework/Instructions/HeroesOfPymoli/Resources/purchase_data.csv")


# In[3]:


heros.head()


# In[4]:


#Total number of players
counts = heros["SN"].unique()
print(len(counts))


# In[5]:


#Number of unqiue purchase item is 179
unique_item = heros["Item Name"].unique()
print(len(unique_item))
#Average purchase price
price = heros["Price"].describe()
print(price["mean"])
# Total number of purchase 
print(price["count"])
#Total Revene
revene = heros["Price"].sum()
print(revene)
#dataframe
unique = pd.DataFrame({"Number of unique item": ["179"],
                       "Average purchase price": ["3.05"],
                       "Total number of purchase": ["780"],
                       "Total Revene": ["2379.77"]

}
)
print(unique)


# In[6]:


#Percentage and Count of Male Players & Percentage and Count of Female Players & Percentage and Count of Other / Non-Disclosed
hero_unique = heros.drop_duplicates(subset="SN", keep='first', inplace=False)
hero_unique
tc = hero_unique["Gender"].value_counts()
print(tc)
percent_male = 484/576
percent_female = 81/576
percent_other = 11/576
print(percent_male)
print(percent_female)
print(percent_other)
#dataframe
malefemale = pd.DataFrame({"Gender": ["Male", "Female", "Other"],
                           "Total Count": ["484", "81", "11"],
                           "Percentage": ["84%", "14%", "1.9%"]
}
)
print(malefemale)


# In[7]:


#Purchasing Analysis(Gender)
hero_price = heros[["Gender", "Price"]]
male_price = heros.loc[heros["Gender"] == "Male", :]
male_total_purchase_value  = male_price["Price"].sum()
male_total_purchase_count = male_price["Price"].count()
male_total_purchase_average = male_price["Price"].mean()
ave_total_purchase_per_male = male_total_purchase_value/484
print(male_total_purchase_value)
print(male_total_purchase_count)
print(male_total_purchase_average)
print(ave_total_purchase_per_male)

female_price = heros.loc[heros["Gender"] == "Female", :]
female_total_purchase_value  = female_price["Price"].sum()
female_total_purchase_count = female_price["Price"].count()
female_total_purchase_average = female_price["Price"].mean()
ave_total_purchase_per_female = female_total_purchase_value/81
print(female_total_purchase_value)
print(female_total_purchase_count)
print(female_total_purchase_average)
print(ave_total_purchase_per_female)

other_price = heros.loc[heros["Gender"] == "Other / Non-Disclosed", :]
other_total_purchase_value  = other_price["Price"].sum()
other_total_purchase_count = other_price["Price"].count()
other_total_purchase_average = other_price["Price"].mean()
ave_total_purchase_per_other = other_total_purchase_value/15
print(other_total_purchase_value)
print(other_total_purchase_count)
print(other_total_purchase_average)
print(ave_total_purchase_per_other)

#dataframe

pag = pd.DataFrame({"Gender": ["Male", "Female", "Other"],
                    "Purchase Value": ["1967.64", "361.94", "50.19"],
                    "Purchase Count": ["652", "113", "15"],
                    "Average": ["3.02", "3.20", "3.35"],
                    "Per one": ["4.07", "4.47", "3.35"]
    
}
)

print(pag)


# In[8]:


bins = [0, 9, 14, 19, 24, 29, 34, 39, 100]
group_name = ["<10", "10-14", "15-19","20-24", "25-29", "30-34", "35-39","40+"]
heros["Age summary"] = pd.cut(heros["Age"], bins, labels=group_name)
hero_unique = heros.drop_duplicates(subset="SN", keep='first', inplace=False)
hero_unique.head()
hero_unique_= hero_unique.loc[hero_unique["Age summary"] == "<10", :]
print(hero_unique_.count()["SN"])
hero_unique_1014 = hero_unique.loc[hero_unique["Age summary"] == "10-14", :]
print(hero_unique_1014.count()["SN"])
hero_unique_1519 = hero_unique.loc[hero_unique["Age summary"] == "15-19", :]
print(hero_unique_1519.count()["SN"])
hero_unique_2024 = hero_unique.loc[hero_unique["Age summary"] == "20-24", :]
print(hero_unique_2024.count()["SN"])
hero_unique_2529 = hero_unique.loc[hero_unique["Age summary"] == "25-29", :]
print(hero_unique_2529.count()["SN"])
hero_unique_3034 = hero_unique.loc[hero_unique["Age summary"] == "30-34", :]
print(hero_unique_3034.count()["SN"])
hero_unique_3539 = hero_unique.loc[hero_unique["Age summary"] == "35-39", :]
print(hero_unique_3539.count()["SN"])
hero_unique_40 = hero_unique.loc[hero_unique["Age summary"] == "40+", :]
print(hero_unique_40.count()["SN"])
percentage_ = 17/576
print(percentage_)
percentage_1014 = 22/576
print(percentage_1014)
percentage_1519 = 107/576
print(percentage_1519)
percentage_2024 = 258/576
print(percentage_2024)
percentage_2529 = 77/576
print(percentage_2529)
percentage_3034 = 52/576
print(percentage_3034)
percentage_3539 = 31/576
print(percentage_3539)
percentage_40 = 12/576
print(percentage_40)

#dataframe
agedata = pd.DataFrame({"Age summary": ["<10","10-14","15-19","20-24", "25-29", "30-34", "35-39","40+"],
                       "Count": ["17", "22", "107", "258", "77", "52", "31", "12"],
                       "percentage": ["2.95%", "3.82%", "18.58%", "44.79%", "13.37%", "9.03%", "5.38%", "2.08%"]
    
}
)
print(agedata)


# In[9]:


#Top spender
hero_sn = heros.groupby(['SN'])
purchase_value = hero_sn["Price"].sum()
print(purchase_value)
#purchase value sort
pvs = purchase_value.sort_values(ascending=False).head(5)
print(pvs)
#purchase count
hero_sn_ = pd.DataFrame(hero_sn["SN"].count(), columns = ["SN"])
hero_sn_.loc["Lisosia93", :]
hero_sn_.loc["Idastidru52", :]
hero_sn_.loc["Chamjask73", :]
hero_sn_.loc["Iral74", :]
hero_sn_.loc["Iskadarya95", :]
#averager purchase value
lisosia = 18.96/5
idastidru = 15.45/4
chamjask = 13.83/3
iral = 13.62/4
iskadarya = 13.10/3
print(lisosia)
print(idastidru)
print(chamjask)
print(iral)
print(iskadarya)
#dataframe
sorting_by_purchase_value = pd.DataFrame({"SN":["Lisosia93", "Idastidru52", "Chamjask73", "Iral74", "Iskadarya95"],
                                          "Purchase Count": ["5", "4", "3", "4", "3"],
                                          "Total Purchase Value": ["18.96", "15.45", "13.83", "13.62", "13.10"],
                                          "Average Purchase Value": ["3.792", "3.8625", "4.61", "3.405", "4.367"]
                                    
}
)

print(sorting_by_purchase_value)


# In[10]:


#most pupular item
hero_popular_item = heros.groupby(['Item Name'])
hero_popular_item_ = hero_popular_item.count()
hero_popular_item_["SN"].sort_values(ascending = False).head(5)


# In[11]:


#most profitted item
hero_profitted_item = heros.groupby(['Price'])
hero_profitted_item_ = hero_profitted_item.count()
hero_profitted_item_["SN"].sort_values(ascending = False).head(5)


# In[ ]:





# In[ ]:




