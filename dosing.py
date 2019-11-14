import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
pio.renderers.default = "browser"
import sys

# left merge two dataframes on two columns
def df_left_merge(df1, df2, col1, col2):
    df_merged = pd.merge(df1, df2, on=[col1, col2], how='left', suffixes=('', '_y'))
    return df_merged

# filter based on requirements from input arguments
def df_filter(df1, df2, col1, col2, col3, col1_val, col2_val, col3_val):
    df_filtered = df1[(df2[col1]==col1_val) & 
                          (df2[col2]==col2_val) &
                          (df1[col3]!=col3_val)].reset_index(drop=True)
    return df_filtered

# check the number of input arguments
if len(sys.argv) != 5 or (not sys.argv[3].isdigit()):
    print("Please enter the 4 command line arguments in the order " +
          "VISCODE SVDOSE ECSDSTXT PATH_TO_OUTPUT_FILE.")
    print("\n Example from a python terminal:" +
          "\n runfile('./dosing.py', wdir='./', " + 
          "args='w02 Y 280 output/directory/for/results/')")
    print("\n Example from a bash terminal:" +
          "\n python dosing.py w02 Y 280 output/directory/for/results/")
    
else:
    print(sys.argv)
    
    # request parameters from the command line  
    viscode_input = sys.argv[1] # viscode
    svdose_input = sys.argv[2] # svdose
    ecsdstxt_input = int(sys.argv[3]) # ecsdstxt
    path_to_output = sys.argv[4] # 'output/directory/of/results.csv'
    
    # read the data and import as dataframes
    ec = pd.read_csv("t2_ec 20190619.csv") 
    registry = pd.read_csv("t2_registry 20190619.csv") 
    
    # filter the records for the pie chart
    registry_query = registry[(registry['SVPERF']=='Y') & 
                              (registry['VISCODE']!='bl')]
    
    # produce a pie chart
    labels = registry_query['VISCODE'].value_counts().index
    values = registry_query['VISCODE'].value_counts().values
    fig = go.Figure(data=[go.Pie(labels=labels, 
                           values=values,
                           hovertemplate = "Viscode: <b>%{label}</b> " + 
                           "<br>Count: <b>%{value} " + 
                           "(%{percent}</b>) <extra></extra>")])
    fig.update_layout(
        title = "Viscodes from Registry")
    fig.show()
    
    # left merge the two dataframes
    t2 = df_left_merge(registry, ec, 'RID', 'VISCODE')
    
    # filter based on the requirements
    t2_filtered = df_filter(t2, registry, 'VISCODE', 'SVDOSE', 'ECSDSTXT',
                            viscode_input, svdose_input, ecsdstxt_input)
    
    # keep only specified columns ID, RID, USERID, VISCODE, SVDOSE, ECSDSTXT
    t2_final = t2_filtered[['ID','RID','USERID','VISCODE','SVDOSE','ECSDSTXT']]
    t2_final.columns = ['ID','RID','USERID','VISCODE','SVDOSE','ECSDSTXT']
    
    # write to csv
    t2_final.to_csv(path_to_output + r'results.csv', index=False)