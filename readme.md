# Problem Statement
**Understanding the reach of a topic on YouTube by Data Analysis**

We are planning to start a youtube channel about a specific topic on youtube. But before we start, we need to understand the reach of the topic and the currently available
data/videos in youtube to differentiate us from similar channels.So we need to implement an analysis system, the specs are given below.

#### Analyse the following
##### Tag Analysis
- Tag Vs number videos
- Tag with most videos, least videos etc
- Tag vs Avg duration of videos
- Tag with most video time, least video time etc
##### Tag Classification - Create Categories
- Classify tags as Tutorials, demos, live coding etc
- And calculate above data for each category

#### Additional
- Add other metrics/analysis useful for the requirement, eg, tags vs no. of comments, view count, likes count etc


### Output
spreadsheets with relevant information

---

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

---

# Usage
- Create "creds.json" in root folder with the following structure:
  ```
  {
      "api_key": "get your api key from: https://console.developers.google.com/marketplace/product/google/youtube.googleapis.com?q=search&referrer=search"
  }
  ```
- Install required libraries using: `pip install -r requirements.txt`
- Run `extract_metadata_from_yt_videos.py` for fetching the required data in JSON format
  - Search term can be passed in this call (see `__main__` block): 

      ```py
      youtube_search_data = get_search_results_data(api_key, <search_term_goes_here>, 700)
      ```
- Once data is extracted, use JupyterNotebook `analysis.ipynb` to perform the analysis by selecting "Restart Kernel and Run All Cells" option from "Kernel" menu.

### Output

- The output CSV files will be present in the root folder itself.
  - all_category_stats.csv
  - category_analysis.csv
  - tag_analysis.csv
  - tags_vs_video_count.csv

- The JSON files will also be present in root folder as well. They are stored at each preprocessing step for future reference or to analyze fault in case of error in pipeline.

---

# References
- [Create YouTube API](https://console.developers.google.com/marketplace/product/google/youtube.googleapis.com?q=search&referrer=search)
- [Restrict Key](https://console.developers.google.com/apis/credentials/key/53c0f5a0-1b8f-4c80-b44c-dac0d30a507e?project=folkloric-air-327006)
- [YouTube API Python Quickstart](https://developers.google.com/youtube/v3/quickstart/python)
- [Converting YouTube duration to Date Time](https://stackoverflow.com/a/16743442)
- [Pandas SettingWithCopy Warning](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy)
- [To check words in different languages](https://translate.google.com/)
- https://stackoverflow.com/questions/40339886/pandas-concat-generates-nan-values
- https://stackoverflow.com/questions/71284185/setting-values-in-one-column-using-another-in-pandas/71284229#71284229
- https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
- https://stackoverflow.com/questions/36370821/does-youtube-v3-data-api-have-a-limit-to-the-number-of-ids-you-can-send-to-vide

---

### Note
- We are not parsing playlists to avoid complexity in this POC.
- I used an anaconda installation for my JupyterNotebook setup and packages such as pandas, numpy, sklearn came from conda itself. Hence, there could be a version mismatch in requirements.txt or some commands in the notebook.
