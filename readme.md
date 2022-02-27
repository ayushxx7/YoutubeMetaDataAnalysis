# Problem Statement
Understanding the reach of a topic on YouTube by Data Analysis

# Approach
## Extract Data from YouTube
- Extract YouTube search results data for topic via YouTube Data API
- Parse the JSON response to keep only relevant information

## Analyzing Video Metadata
- We will be using Jupyter Notebooks for this part of the analysis
- Analyse the JSON data by putting into a Pandas dataframe

### Part 1: Analyzing Tags
- tag vs number of videos: most videos, least videos
- tag vs duration: most duration, least duration, average duration
- Dump the information in a csv file for further insights

### Part 2: Analyzing Categories

#### Topic Modelling 
- Unsupervised Topic Clustering to figure out which tags belong together. 
- Assigning an appropriate category manually.
- Assigning Categories to each video based on it's tags list

#### Category analysis
- category vs number of videos: most videos, least videos
- category vs duration: most duration, least duration, average duration
- Dump the information in a csv file for further insights

# References
- [Create YouTube API](https://console.developers.google.com/marketplace/product/google/youtube.googleapis.com?q=search&referrer=search)
- [Restrict Key](https://console.developers.google.com/apis/credentials/key/53c0f5a0-1b8f-4c80-b44c-dac0d30a507e?project=folkloric-air-327006)
- [YouTube API Python Quickstart](https://developers.google.com/youtube/v3/quickstart/python)
- [Converting YouTube duration to Date Time](https://stackoverflow.com/a/16743442)
- [Pandas SettingWithCopy Warning](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy)
- https://stackoverflow.com/questions/40339886/pandas-concat-generates-nan-values
- https://stackoverflow.com/questions/71284185/setting-values-in-one-column-using-another-in-pandas/71284229#71284229

### Note
We are not parsing playlists to avoid complexity in this POC
