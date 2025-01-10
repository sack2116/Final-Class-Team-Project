from utilities import replaceLyricsChars

def clean_lyrics_df(df):
    df = df.dropna()

    replacements = [
        {"original": "n't", "replacement": " not", "use_regex": False},
        {"original": "'m", "replacement": " am", "use_regex": False},
        {"original": "'s", "replacement": " is", "use_regex": False},
        {"original": "'ve", "replacement": " have", "use_regex": False},
        {"original": "\'", "replacement": "", "use_regex": False},
        {"original": "\n", "replacement": " ", "use_regex": False},
        {"original": "pre-chorus:", "replacement": " ", "use_regex": False},
        {"original": "chorus:", "replacement": " ", "use_regex": False},
        {"original": "\d\w{2} verse:", "replacement": "", "use_regex": True}, # Any ver text with a number before (1st, 2nd)
        {"original": "\[intro.*\]", "replacement": " ", "use_regex": True},
        {"original": "\[verse.*\]", "replacement": " ", "use_regex": True},
        {"original": "\[\s*\]", "replacement": "", "use_regex": True}, # Empty brackets with no or many spaces
    ]

    for replacement in replacements:
        df = replaceLyricsChars(df, what=replacement["original"], to=replacement["replacement"], regex=replacement["use_regex"])

    return df