data = {'Rank':[1, 2, 3, 4, 5, 6],
       'Language': ['Python', 'Java',
                   'Javascript',
                   'C#', 'PHP',
                   'C/C++'],
       'Share':[29.88, 19.05, 8.17,
               7.3, 6.15, 5.92],
       'Trend':[4.1, -1.8, 0.1, -0.1, -1.0, -0.2]}

df = pd.DataFrame(data)
display(df)

#scource: 
#https://www.marsja.se/how-to-convert-a-pandas-dataframe-to-a-numpy-array/
