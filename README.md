# Movie Scraping Tool

A Python script that scrapes movie information from Rotten Tomatoes using the Beautiful Soup library. This tool allows users to search for movies based on different criteria, such as genre, platform, and ratings.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Functionality](#functionality)
- 
## Features

- **Search by Genre**: Find movies by specifying a genre such as Action, Comedy, etc.
- **Search by Platform**: Search for movies available on specific streaming platforms like Netflix or Hulu.
- **Search by Ratings**: Filter movies based on their ratings (e.g., PG, R).
- **Combined Search**: Search using a combination of genre, platform, and ratings.

## Requirements

- Python 3.x
- Beautiful Soup 4
- Requests

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/movie-scraping-tool.git
   cd movie-scraping-tool

2 - Install the required packages:
```bash
pip install beautifulsoup4 requests
```

## Usage

1 - Run the script using Python:
```bash
python scrapping_project.py
```
2 - Follow the prompts to search for movies based on your criteria:
- You can search by Genre, Platform, Ratings, or All.

3 - The script will display a list of movies based on the selected criteria.

## Functionality
The script defines a function `search_movies()` that handles the movie search functionality. It performs the following:

- Takes user input for the desired search criteria (Genre, Platform, Ratings, or All).
- Makes an HTTP request to the Rotten Tomatoes website using the selected criteria.
- Parses the HTML response using Beautiful Soup to extract movie titles and release dates.
- Displays the requested number of movies based on user input.

## Key Functions:
- `search_movies(Question)`: Handles different search criteria and retrieves the relevant movie information.







