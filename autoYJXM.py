# ©️ YJXM Data Management, all rights reserved by the author. 
# Contact author: jinghc2@uci.edu, at Irvine, California, USA
# This package was developed and is currently being maintained by Jinghao Chen, at the request of Frank Tung.

import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Heiti TC'] # Or any other Chinese characters

looop = 'yes'

while looop == 'yes':
    m1 = input('Type month (1-12): ')
    m2 = input('Type another month (1-12): ')
    start_date = input('Type the start date (1-31): ')
    end_date = input('Type the end date (1-31): ')
    
    m1 += '月'
    m2 += '月'
    start_date = int(start_date)
    end_date = int(end_date)
    
    df1 = pd.read_excel('遇见厦门每日销售额.xlsx',sheet_name=m1)
    df2 = pd.read_excel('遇见厦门每日销售额.xlsx',sheet_name=m2)
    
    namesRaw1 = list(df1.iloc[0]) 
    namesRaw2 = list(df2.iloc[0])
    names1 = [x for x in namesRaw1[1:] if str(x)!='nan'] # from 1 because df1.iloc[0,0] is 日期/店铺
    names2 = [x for x in namesRaw2[1:] if str(x)!='nan']

    names = []
    for x in names1:
        if x in names2:
            names.append(x)
    
    days = list(range(start_date,end_date+1))

    for name in names:
        idx1 = namesRaw1.index(name)
        idx2 = namesRaw2.index(name)
        x1 = list(df1.iloc[start_date:end_date+1,idx1]) 
        x2 = list(df2.iloc[start_date:end_date+1,idx2]) 
        x = [x1,x2]
        
        fig = plt.figure(figsize=(20,5))
        plt.plot(days,x1,'-o',label = m1)
        plt.plot(days,x2,'-o',label = m2)
        plt.xlabel("日期")
        plt.ylabel("销售额")
        plt.title(name)
        plt.legend()
        plt.xticks(range(min(days), max(days)+1,2))
        plt.table(cellText=x, colLabels=days, rowLabels=(m1,m2), bbox = [0, -.5, 1, .3])
        
        table = df1.iloc[start_date:end_date+1,idx1]
        
    plt.show()
    
    looop = input('Another task? (yes/no): ')
    
    
