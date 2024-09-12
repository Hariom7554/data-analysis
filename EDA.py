import pandas as p
import numpy as n
import seaborn as sns
import matplotlib.pyplot as ply
data=p.read_csv("Employee.csv")
#for finding the number of row and column in data frame
print("the no of rows and columns in dataset")
print(data.shape)
#print(data)
#reading the top five column of dataset
print("data of top five data value")
print(data.head(5))
#print the last five values of dataset
print("data of last five data value")
print(data.tail(5))
#the process of data cleaning
#gathring the data information
print(data.info())
#deleting the complete colunmn from a dataet
data.drop(["HireDate","YearsInMostRecentRole",
"YearsSinceLastPromotion","YearsWithCurrManager"],axis=1,inplace=True)
#findind the null values  every column
print(p.isnull(data).sum())
#removing the null values from dataset
data.dropna()
#see the totalcolumns in a data set
print("the total columns in a dataset is")
data.columns
#rename the column name 
data.rename(columns={"YearAtCompany":"experinse years"},inplace=True)
#some mathmatical functions on data
print("max ,min,mean of the numric data columns")
print(data.describe())

#finding duplicate data in a dataset

data.duplicated()
#process of exploratry data anaylsis
#code for finding the numbers of male and female in dataset
ax=sns.countplot(x='Gender',data=data)
ply.xlabel("gender")
ply.ylabel("count of gender")
for bars in ax.containers:
    ax.bar_label(bars)
    ply.title("number of male and females in ognization ")
    ply.show()

#comprission of salary of males and feamales in company
x=data["Gender"]
y=data["Salary"]
ply.title("comprission of salary of males and feamales in company")
ply.xlabel("gender")
ply.ylabel("Salary")
ply.bar(x,y)

ply.show()
#see that how much job role in every field
s=data["JobRole"]
t=data["EducationField"]
ply.bar(s,t)
ply.xlabel("jobs of employes")
ply.ylabel("Education of emplotes")
ply.title("job roles according to the educational field in company")
ply.show()
#salary according to eduational field
d=data["Salary"]
e=data["EducationField"]
ply.xlabel("salary of employ")
ply.ylabel("education field of an employe")
ply.bar(e,d)
ply.title("salary acording to yhe educational fileld")
ply.show()
#vieew how much salary should taken by every department
ab=data["Salary"].sum()
ac=data["Department"]
ply.title("salary of employes according to the department")
ply.xlabel("salary")
ply.ylabel("educational field of employes")
sns.barplot(x=ab,y=ac,data=data)
ply.show()

print("summary report of the data:-")
print("Observation 1:-")

print("the total employes are working in the orgnization is:1470")
print("the numbers of Females are majority in the orgnization")
print("observation 2:-")

print("the distribution of salary is aproxmatly same for male and females ")
print("males are paid more then females acroding to their numbers")
print("the least salary is paid to the gender that is not prefer to say")

print("observation 3:-")
print("most of the jobs are of an engeenier in cs field  an compeny")
print("this is a softwware ornization")
print("in future the demand of data engineer shall happen in this orgnization")

print("observation 4:-")
print("the most salary is taken by a person who belongsto cs field")
print("theleast salary ig givento the person who has a technical degree")

print("observation 5:-")
print("all the department should take the same amount of salary")

print("conclusion:-")
print("#this is a compuer software based ogrnization ")
print("#in future it will hier many data engineeres")
print("#according to the numer of employes it is a lare orgnization")
print("#this orgnization is dealing withthe data.") 
print("beacuse it hierd most of the data enginners")





