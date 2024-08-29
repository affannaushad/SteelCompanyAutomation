import pandas as pd 

df = pd.read_csv('/Users/affan/Desktop/SteelCompanyExcelAutomation.csv')
df.columns = df.columns.str.strip()
df['Name'] = df['Name'].str.strip()

mask = df['Name'].str.len() >= 3

df = df[mask]
df.reset_index(drop=True, inplace=True)

def process_name(df):
    for i in range(len(df)):
        # Check if 'Name' column contains a comma
        if ',' in df.loc[i, 'Name']:
            # Split the value into title and company name
            title, company_name = df.loc[i, 'Name'].split(',', 1)
            title = title.strip()
            company_name = company_name.strip()
            
            # Place the values in the row above if it exists
            if i > 0:
                df.loc[i - 1, 'Title'] = title
                df.loc[i - 1, 'Company Name'] = company_name
            
            # Clear the 'Name' column in the current row
            df.loc[i, 'Name'] = ''
    
    return df

# Apply the function to the DataFrame
df = process_name(df)

# Remove any rows where the 'Name' column is empty after processing
df = df[df['Name'] != '']

# Reset the index of the DataFrame
df.reset_index(drop=True, inplace=True)


df.head(10)

df.to_csv('Yay.csv')