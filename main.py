import time
import feedparser
import requests

# URL of the Nitter RSS feed
nitter_rss_url = "https://nitter.net/wegonlove/rss"

# Initialize the last updated time to a past time
last_updated = time.time()

while True:
    # Calculate the time since the last update
    time_since_last_update = time.time() - last_updated

    # If it's time to check for updates (e.g., every 10 seconds)
    if time_since_last_update >= 10:
        # Fetch the RSS feed
        response = requests.get(nitter_rss_url)

        if response.status_code == 200:
            # Parse the RSS feed
            feed = feedparser.parse(response.text)

            # Process the feed data here
            # For example, you can print the titles of the new entries:
            for entry in feed.entries:
                # Check if the entry was published after the last update
                entry_time = time.mktime(entry.published_parsed)
                if entry_time > last_updated:
                    print(entry.title)

            # Update the last_updated time
            last_updated = time.time()

    # Sleep for a short interval (e.g., 1 second) before checking for updates again
    time.sleep(1)
