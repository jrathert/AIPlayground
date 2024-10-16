#
# small helper that uses fuzzywuzzy to identify similar entries in first column of an Excel file
# WARNING: current implementation is super inefficient
#
from typing import List
import pandas as pd
import re
from fuzzywuzzy import fuzz, process
import time

fname='allcomp.xlsx'
max_rows=None
similarity_threshold = 90


def standardize_name(old_name: str) -> str:
    name: str = str(old_name) # needed as type info get lost and "NaN" is converted to float?!
    name = name.lower()
    name = re.sub(r'[^\-a-z0-9#\s]', '', name) # keep only letters/number
    name = name = re.sub(r'\s+', ' ', name).strip() # remove any extra whitespace
    return name

def find_similar_names(name: str, all_names: List[str], threshold: int = similarity_threshold) -> List[str]:
    similar = process.extract(name, all_names, scorer=fuzz.token_sort_ratio)
    candidates = [match for match, score in similar if score >= threshold and match != name] 
    return [] if len(candidates) == 0 or len(candidates) > 3 else candidates



print(f"Reading Excel file '{fname}'...", end="")
start = time.perf_counter()
# df = pd.read_excel(fname, sheet_name='Sheet1', usecols=[0], engine='openpyxl', engine_kwargs={'read_only': True, 'keep_vba': False})  # not faster
df = pd.read_excel(fname, sheet_name='Sheet1', dtype=str, usecols=[0], names=["original_name"], nrows=max_rows)
end = time.perf_counter()
elapsed = end - start
print(f" done - read {len(df)} applications in {elapsed:.6f} seconds")


print(f"Standardizing names...", end="")
start = time.perf_counter()
df['standardized_name'] = df['original_name'].apply(standardize_name)
unique_names = df['standardized_name'].unique()
end = time.perf_counter()
elapsed = end - start
print(f" done - found {len(unique_names)} unique standardized names in {elapsed:.6f} seconds")


print(f"Assigning similar names...", end="")
start = time.perf_counter()
similar_applications = {name: find_similar_names(name, unique_names) for name in unique_names}
df['similar_applications'] = df['standardized_name'].map(similar_applications)
non_empty = [ name for name, similars in similar_applications.items() if len(similars) > 0]
end = time.perf_counter()
elapsed = end - start
print(f" done - found similarities for {len(non_empty)} applications in {elapsed:.6f} seconds")

candidates = df.loc[df['standardized_name'].isin(non_empty)]

print()
print(candidates)


