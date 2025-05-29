from services.yandex_api_parser import YandexAPIPlaylistParser
from services.soundcloud_public import SoundCloudPublic
from utils.export import export_links

def main():
    url = input("🔗 Вставь ссылку на плейлист Yandex: ").strip()
    parser = YandexAPIPlaylistParser()
    tracks = parser.parse(url)

    if not tracks:
        print("❌ Не удалось получить треки.")
        return

    sc = SoundCloudPublic()
    results = sc.process_tracks(tracks)
    export_links("playlist", results)

if __name__ == "__main__":
    main()
