#..................Total Recall.......................
#An app that gives you a print out of products that were recalled in your state
import pandas as pd 
from pandas import Series, DataFrame
#import and read data
xlx_path=r"C:\Users\edwar\Desktop\fda.xlsx"
df=pd.read_excel(xlx_path)
data=pd.DataFrame(df)
#Remove unwanted columns
data=data.drop(['Status','Recalling Firm City','Product Classification','Firm Profile','Center','Event Classification','Product ID','FEI Number','Event ID','Product Type','Distribution Pattern', 'Recalling Firm Country'],axis=1)
#rename columns
data=data.rename(columns={'Center Classification Date':'Recall Date','Recalling Firm Name': 'Company','Recall Details': 'Get More Info','Recalling Firm State': 'State','Product Description': 'Products','Reason for Recall': 'Reason',})
data_new=data.set_index('Company')
def get_input():
    search= input("Enter a state: ")
    x=(data_new.loc[data_new.State.isin([search])])
    print(x)    
get_input()
   



