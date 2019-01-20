import pandas as pd
import numpy as np
energy = pd.read_excel('Energy Indicators.xls')
#print(energy)
energy = energy[16:243]
energy = energy.drop(energy.columns[[0, 1]], axis=1)
energy.rename(columns={'Environmental Indicators: Energy': 'Country','Unnamed: 3':'Energy Supply','Unnamed: 4':'Energy Supply per Capita','Unnamed: 5':'% Renewable'}, inplace=True)
energy.replace('...', np.nan,inplace = True) #replace for NaN
energy['Energy Supply'] *= 1000000 # convert for gigajoules
def remove_digit(data):
    newData = ''.join([i for i in data if not i.isdigit()])
    i = newData.find('(')
    if i>-1: newData = newData[:i]
    return newData.strip()
energy['Country'] = energy['Country'].apply(remove_digit)
di = {"Republic of Korea": "South Korea",
"United States of America": "United States",
"United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
"China, Hong Kong Special Administrative Region": "Hong Kong"}
energy.replace({"Country": di},inplace = True)

GDP = pd.read_csv('world_bank.csv', skiprows=4)
GDP.rename(columns={'Country Name': 'Country'}, inplace=True)
di = {"Korea, Rep.": "South Korea",
"Iran, Islamic Rep.": "Iran",
"Hong Kong SAR, China": "Hong Kong"}
GDP.replace({"Country": di},inplace = True)

ScimEn = pd.read_excel('scimagojr.xlsx')
df = pd.merge(pd.merge(energy, GDP, on='Country'), ScimEn, on='Country')

# We only need 2006-2015 data
df.set_index('Country',inplace=True)
df = df[['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]
df = (df.loc[df['Rank'].isin([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])])
df.sort('Rank',inplace=True)
#print(df)

def answer_one():
    return df

#Question 2:
def answer_two():
    # Union a, b, c - intersection a,b,c
    union = pd.merge(pd.merge(energy, GDP, on='Country', how='outer'), ScimEn, on='Country', how='outer')
    intersect = pd.merge(pd.merge(energy, GDP, on='Country'), ScimEn, on='Country')
    return len(union)-len(intersect)

#Question 3:
def answer_three():
    Top15 = answer_one()
    years = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
    return (Top15[years].mean(axis=1)).sort_values(ascending=False).rename('avgGDP')

#Questions 4:
def answer_four():
    Top15 = answer_one()
    Top15['avgGDP'] = answer_three()
    Top15.sort_values(by='avgGDP', inplace=True, ascending=False)
    return abs(Top15.iloc[5]['2015']-Top15.iloc[5]['2006'])

#Questions 5:
def answer_five():
    Top15 = answer_one()
    print()
    return Top15['Energy Supply per Capita'].mean()

#Quesiton 6:
def answer_six():
    Top15 = answer_one()
    ct = Top15.sort_values(by='% Renewable', ascending=False).iloc[0]
    return (ct.name, ct['% Renewable'])

#Question 7:
def answer_seven():
    Top15 = answer_one()
    Top15['Citation_ratio'] = Top15['Self-citations']/Top15['Citations']
    ct = Top15.sort_values(by='Citation_ratio', ascending=False).iloc[0]
    return ct.name, ct['Citation_ratio']