import pandas as pd

# Replace function to remove any character
def replaceLyricsChars(df, what, to, regex=False):
    df['lyrics'] = df['lyrics'].str.replace(what, to, regex=regex)
    return df

# Search in lyrics for a specific word
def searchLyrics(df, word):
    return df[df['lyrics'].str.contains(word, case=False)]

def load_data(file_path, chunksize=10000):
    """
    Load and process a large CSV file in chunks.

    :param file_path: Path to the CSV file.
    :param chunksize: Number of rows per chunk to process.
    :return: A single DataFrame containing the processed data.
    """
    processed_chunks = []

    # Read the CSV file in chunks
    for chunk in pd.read_csv(file_path, chunksize=chunksize):
        # Drop rows with missing lyrics in the current chunk
        chunk = chunk.dropna(subset=['lyrics'])
        # Append the processed chunk to the list
        processed_chunks.append(chunk)

    # Concatenate all chunks into a single DataFrame
    combined_data = pd.concat(processed_chunks, ignore_index=True)
    return combined_data
