import json

def export_links(name, links):
    with open(f"{name}.txt", "w", encoding="utf-8") as f:
        for item in links:
            line = item['title']
            if item.get('url') and "http" in item['url']:
                line += f" ({item['url']})"
            f.write(line + "\n")

    with open(f"{name}.json", "w", encoding="utf-8") as f:
        json.dump(links, f, ensure_ascii=False, indent=2)

    print(f"📁 Сохранено: {name}.txt и {name}.json")
