import os
import pandas as pd

IN_PATH = os.path.join("data", "countypres_2000-2020.csv")
OUTPUT_DIR = "artifacts"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "election_report_pandas.csv")

df = (
    pd.read_csv(IN_PATH)
    .loc[lambda df: df['year'] == 2020]
    .loc[lambda df: ~(df['totalvotes'].isna())]
    )

filtered_ = df.loc[:, ['year', 'state_po', 'candidate', 'candidatevotes']]

df_votesum = filtered_.groupby(['year', 'state_po', 'candidate'])['candidatevotes'].sum().to_frame()

sorted_votes = df_votesum.sort_values(['state_po', 'candidatevotes'], ascending = (True, False))

if __name__ == "__main__":
    sorted_votes.to_csv(OUTPUT_PATH)
