import pandas as pd
import numpy as np
import glob

county_files = glob.glob("./cdc_county_fertility/*.txt")
state_files  = glob.glob("./cdc_state_fertility/*.txt")


def load_state_file(filename):
    table = pd.read_table(filename, sep='\t')
    print table.columns
    cohort = table[ (table['Notes']!='Total') &  ~np.isnan(table['Year'])]
    return  cohort[['Year','Age of Mother Year', 'Age of Mother Year Code','Births','Fertility Rate','State']].set_index("Year").convert_objects(convert_numeric=True)

def load_county_file(filename):
    table = pd.read_table(filename, sep='\t')
    print table.columns
    cohort = table[ (table['Notes']!='Total') &  ~np.isnan(table['Year'])]
    return cohort[['Year','Age of Mother Year', 'Age of Mother Year Code','Births','Fertility Rate','County']].set_index("Year").convert_objects(convert_numeric=True)

combined_state = pd.concat([ load_state_file(f) for f in state_files])
combined_state.to_csv('states_combined.csv')

combined_counties = pd.concat([ load_county_file(f) for f in county_files])
combined_counties.to_csv('counties_combined.csv')
