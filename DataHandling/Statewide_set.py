import pandas as pd

def load_and_clean_data(file_path):
    """
    Load and clean the data from the specified CSV file.
    
    Parameters:
    file_path (str): The path to the CSV file.
    
    Returns:
    pd.DataFrame: Cleaned DataFrame with renamed columns and date parsing.
    """
    # Load the data
    df = pd.read_csv(file_path)
    #alue = file_path.split('/')[-1].split('.')[0]
    # Rename columns for consistency
    #df.columns = ['observation_date', value]
    
    # Convert observation_date to datetime
    df['observation_date'] = pd.to_datetime(df['observation_date'])
    
    # Convert value to numeric, coercing errors to NaN
    #df[value] = pd.to_numeric(df[value], errors='coerce')
    
    return df

def merge_dataframes(df_list):
    """
    Merge a list of DataFrames on the observation_date column.
    
    Parameters:
    df_list (list): List of DataFrames to merge.
    
    Returns:
    pd.DataFrame: Merged DataFrame.
    """
    merged_df = df_list[0]
    for df in df_list[1:]:
        merged_df = pd.merge(merged_df, df, on='observation_date', how='outer')
    
    return merged_df

def main():
    # List of file paths to load
    file_paths = [
        'Data/Statewide-Monthly/FEDInterestRate.csv',
        'Data/Statewide-Monthly/Construction_Wage.csv',
        'Data/Statewide-Monthly/Construction_Employees.csv',
        'Data/Statewide-Monthly/Contruct_GDP_q_seasonal.csv',
        'Data/Statewide-Monthly/CA_Unemployment.csv',
        'Data/Statewide-Monthly/CA_investment_a.csv',
        'Data/Statewide-Monthly/USTOTALCPI.csv'
        'Data/Statewide-Monthly/StateCorpTax_a.csv',
        'Data/Statewide-Monthly/CA_energyprice_a.csv',
        'Data/Statewide-Monthly/Mfg_Employees.csv',
        'Data/Statewide-Monthly/Mfg_Wage.csv',
        'Data/Statewide-Monthly/Min_Wage_a.csv',
        'Data/Statewide-Monthly/ProducerPriceIndexUSA.csv',
        'Data/Statewide-Monthly/avg_tarrif_a.csv', 
        'Data/Statewide-Monthly/EnergyGen.csv',
        'Data/Statewide-Monthly/Mfg_GDP_q_seasonal.csv'
    ]
    
    # Load and clean each DataFrame
    df_list = [load_and_clean_data(file_path) for file_path in file_paths]
    
    # Merge all DataFrames
    final_df = merge_dataframes(df_list)
    
    # Display the final DataFrame
    print(final_df)

if __name__ == "__main__":
    main()