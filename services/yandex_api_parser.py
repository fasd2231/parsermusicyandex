import requests
import re
from models.track import Track

class YandexAPIPlaylistParser:
    def parse(self, url):
        print(f"🌐 Загружаем плейлист: {url}")
        match = re.search(r'yandex\.ru/users/([^/]+)/playlists/(\d+)', url)
        if not match:
            print(f"❌ Неверный формат ссылки ({url})")
            return []

        user, playlist_id = match.groups()
        api_url = f"https://music.yandex.ru/handlers/playlist.jsx?owner={user}&kinds={playlist_id}&light=true"
        headers = {"User-Agent": "Mozilla/5.0"}

        try:
            r = requests.get(api_url, headers=headers)
            playlist_data = r.json().get("playlist", {})
            track_items = playlist_data.get("tracks", [])
        except Exception as e:
            print("❌ Ошибка загрузки плейлиста:", e)
            return []

        tracks = []

        for item in track_items:
            try:
                track_id = item["id"]
                albums = item.get("albums", [])
                if not albums:
                    print(f"⚠️ Пропуск трека {track_id} — нет альбома")
                    continue

                album_id = albums[0]["id"]

                # Уже есть всё нужное — не нужен второй запрос
                title = item.get("title", "").strip()
                artists = item.get("artists", [])
                artist = ", ".join([a.get("name", "") for a in artists])

                if title and artist:
                    tracks.append(Track(title=title, artist=artist))
            except Exception as e:
                print(f"⚠️ Пропуск трека: {e}")
                continue

        print(f"✅ Успешно получено {len(tracks)} треков")
        return tracks
