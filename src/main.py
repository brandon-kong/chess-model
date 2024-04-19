import pandas as pd
import numpy as np

# max_chunks * chunksize = 50000 (total number of rows in the file)
chunksize = 1000
max_chunks = 10

def read_large_file_in_chunks():
    # Define the chunk size

    # Create an empty DataFrame to store the chunks
    df_chunk = pd.DataFrame()

    chunk_count = 0
    # Use the chunksize parameter to read the file in chunks
    for chunk in pd.read_json("data/lichess_db_eval.jsonl", lines=True, chunksize=chunksize):
        chunk_count += 1

        print(f"Processing chunk {chunk_count}...")

        # the 'evals' column is a list of dictionaries
        # we want to convert this to a dataframe
        # we'll do this by converting the list of dictionaries to a dataframe


        # Process each chunk as needed here
        # For example, you can filter rows, drop columns, etc.
        # append the rows to the empty DataFrame

        processed_chunk = pd.DataFrame()

        for index, row in chunk.iterrows():
            
            # Flatten the 'evals' list into a DataFrame
            evals_df = pd.json_normalize(row['evals'])

            # Flatten the 'pvs' list into a DataFrame
            pvs_df = pd.json_normalize(evals_df['pvs'].iloc[0])

            for pv in evals_df['pvs'].iloc[1:]:
                pv_df = pd.json_normalize(pv)
                pvs_df = pd.concat([pvs_df, pv_df], ignore_index=True)

                df = pd.concat([evals_df, pv_df], axis=1)

                df['fen'] = row['fen']

                processed_chunk = pd.concat([processed_chunk, df], ignore_index=True)

        # Drop the 'pvs' column
        processed_chunk = processed_chunk.drop(columns=['pvs'])
        
        df_chunk = pd.concat([df_chunk, processed_chunk], axis=0)


        if chunk_count >= max_chunks:
            break

    # Now df_chunk contains the entire file, read in chunks
    return df_chunk

def main ():
    # load the evaluations 
    
    # convert the .zst file to json
    # file = zst_to_csv("data/lichess_db_eval.jsonl.zst", "data/lichess_db_eval.jsonl")

    # convert the json to a pandas dataframe
    df = read_large_file_in_chunks()

    # print the first 5 rows of the dataframe
    print(df.head())

    # print the shape of the dataframe
    print(df.shape)

    # print the columns of the dataframe
    print(df.columns)

    # convert the dataframe to a csv file
    df.to_csv("data/lichess_db_eval.csv", index=False)

    pass
    


if __name__ == '__main__':
    main()