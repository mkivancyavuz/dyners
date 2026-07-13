from bs4 import BeautifulSoup

with open('dyners_raw.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Since bs4 wasn't found before, let's just use html.parser but we don't have a built-in pretty printer that easily.
# Actually let's use python's built-in xml.dom.minidom if we can, or just print the tags and their children properly.
import html.parser
class Formatter(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.out = []
        self.depth = 0
    def handle_starttag(self, tag, attrs):
        attrs_str = " ".join([f'{k}="{v}"' for k,v in attrs])
        self.out.append("  " * self.depth + f"<{tag} {attrs_str}>")
        self.depth += 1
    def handle_endtag(self, tag):
        self.depth -= 1
        self.out.append("  " * self.depth + f"</{tag}>")
    def handle_data(self, data):
        data = data.strip()
        if data:
            self.out.append("  " * self.depth + data)

formatter = Formatter()
formatter.feed(html)

with open('formatted_dyners.html', 'w', encoding='utf-8') as f:
    f.write("\n".join(formatter.out))
