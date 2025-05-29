import requests
from urllib.parse import quote

class SoundCloudPublic:
    def __init__(self):
        self.client_id = "2t9loNQH90kzJcsFCODdigxfp325aq4z"

    def search_track(self, track):
        queries = [
            f"{track.artist} {track.title}",
            f"{track.title} {track.artist}",
            f"{track.title}",
        ]
        for query in queries:
            url = f"https://api-v2.soundcloud.com/search/tracks?q={quote(query)}&client_id={self.client_id}&limit=3"
            r = requests.get(url)
            if r.ok:
                for item in r.json().get("collection", []):
                    if 'permalink_url' in item:
                        return item
        return None

    def process_tracks(self, tracks, playlist_name="playlist"):
        found = []
        for t in tracks:
            result = self.search_track(t)
            title = f"{t.artist} - {t.title}"
            if result:
                url = result.get("permalink_url")
                print(f"✅ Найдено: {title} → {url}")
            else:
                url = None
                print(f"❌ Не найдено: {title}")
            found.append({"title": title, "url": url})
        return found
