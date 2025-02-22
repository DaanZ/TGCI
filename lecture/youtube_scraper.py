import os
from urllib.parse import urlparse, parse_qs

import rootpath
from youtube_transcript_api import YouTubeTranscriptApi

from core.chatgpt import llm_summarize
from core.vault.json_vault import JSONVault


def extract_video_id(url):
    try:
        parsed_url = urlparse(url)
        if parsed_url.netloc in ["www.youtube.com", "youtube.com"]:
            query_params = parse_qs(parsed_url.query)
            return query_params.get("v", [None])[0]
        elif parsed_url.netloc == "youtu.be":  # For shortened URLs
            return parsed_url.path.lstrip("/")
    except Exception as e:
        print(f"Error: {e}")

    return None


def youtube_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return "\n".join([f"{entry['text']}" for entry in transcript])
    except Exception as e:
        print("Error " + str(e))
        return None


class YoutubeScraper:

    def __init__(self):
        pass

    def scrape(self, url: str):
        video_id = extract_video_id(url)
        request = {"url": url}
        if not video_id:
            request["error"] = "Could not find video ID from URL"
            return request

        request["text"] = youtube_transcript(video_id).replace("\n", " ")
        request["summary"] = llm_summarize(request["text"], "Summarize into 3 paragraphs")
        return request


class YoutubeCache:

    def __init__(self):
        self.path = os.path.join(rootpath.detect(), "data", "youtube")
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def scrape(self, url: str):
        vault = JSONVault(url, self.path)
        response = vault.get("response", {})
        if response:
            return response

        response = YoutubeScraper().scrape(url)
        vault.set("response", response)

        return response


if __name__ == "__main__":
    links = ["https://www.youtube.com/watch?v=xNKEc0Xn5T8"]
    scraper = YoutubeCache()
    for link in links:
        request = scraper.scrape(link)
        print(request)
