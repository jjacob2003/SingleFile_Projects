import os
import pandas as pd
from googleapiclient.discovery import build
import wikipediaapi
import re  # Import the regular expressions module
from datetime import datetime

# Replace with your actual YouTube API key
api_key = "AIzaSyDZQp060eTNQq-BPUl38wcZWbMwFo1oGHw"
youtube = build('youtube', 'v3', developerKey=api_key)

# Initialize Wikipedia API
wiki_wiki = wikipediaapi.Wikipedia(
    language='en',
    extract_format=wikipediaapi.ExtractFormat.WIKI,
    user_agent="MyMovieRanker/1.0 (jjthadem@gmail.com)",
)

def fetch_wikipedia_data(movie_title):
    try:
        page = wiki_wiki.page(movie_title)
        return page.text
    except KeyError:
        return ""

def format_currency(number):
    # Format a number as currency with dollar sign and commas for thousands and millions
    return "${:,.0f}".format(number)

def get_latest_video_data(query, max_results=10):
    search_response = youtube.search().list(
        q=query,
        type='video',
        part='id',
        maxResults=max_results,
        order='date',  # Order by upload date to get the latest videos
    ).execute()

    video_ids = [item['id']['videoId'] for item in search_response['items']]

    data = []
    for video_id in video_ids:
        video_response = youtube.videos().list(
            id=video_id,
            part='statistics,snippet'  # Include video statistics and snippet (title, description, etc.)
        ).execute()

        statistics = video_response['items'][0]['statistics']
        snippet = video_response['items'][0]['snippet']

        likes = int(statistics.get('likeCount', 0))
        dislikes = int(statistics.get('dislikeCount', 0))
        comments = int(statistics.get('commentCount', 0))

        data.append({
            'video_id': video_id,
            'title': snippet['title'],
            'description': snippet['description'],
            'published_at': snippet['publishedAt'],
            'views': int(statistics.get('viewCount', 0)),
            'likes': likes,
            'dislikes': dislikes,
            'comments': comments
        })

    return data

# Example: Get the latest video data for a specific query (e.g., "movie trailers")
latest_video_data = get_latest_video_data(query="movie trailers", max_results=50)  # Increase max_results to get more videos

# Create a Pandas DataFrame from the fetched YouTube data
df = pd.DataFrame(latest_video_data)

# Convert 'published_at' column to datetime and extract the month name
df['month'] = pd.to_datetime(df['published_at']).dt.month_name()
df['year'] = pd.to_datetime(df['published_at']).dt.year

# Define a function to extract Wikipedia features for a given movie title
def extract_wikipedia_features(movie_title):
    wikipedia_data = fetch_wikipedia_data(movie_title)
    # Extract release date from Wikipedia data using regular expressions
    release_date_match = re.search(r'Release date(.*?)\n', wikipedia_data, re.IGNORECASE | re.DOTALL)
    release_date = release_date_match.group(1).strip() if release_date_match else "Date not found"

    # Implement your feature extraction logic from Wikipedia data here
    # For simplicity, let's assume a placeholder feature "Wikipedia Feature"
    wikipedia_feature = len(wikipedia_data)
    return {"Wikipedia Feature": wikipedia_feature, "Release Date": release_date}

# Apply the extract_wikipedia_features function to each movie title in the DataFrame
df['wikipedia_features'] = df['title'].apply(extract_wikipedia_features)

# Define a function to predict gross revenue and tickets sold (replace with your actual prediction logic)
def predict_gross_and_tickets(dataframe):
    # Create arbitrary coefficients (fictional)
    coefficient_likes = 1000
    coefficient_views = 500
    coefficient_dislikes = -200
    coefficient_comments = 50

    # Calculate fictional predictions for gross revenue and tickets sold
    dataframe['predicted_gross'] = (
        coefficient_likes * dataframe['likes'] +
        coefficient_views * dataframe['views'] +
        coefficient_dislikes * dataframe['dislikes'] +
        coefficient_comments * dataframe['comments']
    )
    
    # Modify coefficients and calculation for tickets sold
    coefficient_tickets = 10  # Adjust this coefficient as needed
    dataframe['predicted_tickets_sold'] = (
        coefficient_tickets * dataframe['likes'] +
        coefficient_tickets * dataframe['views'] +
        coefficient_tickets * dataframe['dislikes'] +
        coefficient_tickets * dataframe['comments']
    )

# Perform fictional predictions
predict_gross_and_tickets(df)

# Sort the DataFrame by predicted gross revenue in descending order
sorted_df = df.sort_values(by='predicted_gross', ascending=False)

# Print information for the top 5 movies
print("Prediction for the top 5 upcoming movies and their predicted revenue/tickets sold\n")
print("Top 5 Movies:")
top_5_movies = sorted_df.head(5)
for index, row in top_5_movies.iterrows():
    print(f"Movie: {row['title']}")
    print(f"Predicted Gross Revenue: {format_currency(row['predicted_gross'])}")
    print(f"Predicted Tickets Sold: {int(row['predicted_tickets_sold'])}")
    print("-" * 20)