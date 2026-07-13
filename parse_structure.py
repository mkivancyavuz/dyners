from html.parser import HTMLParser

class StructureParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.depth = 0
        self.in_body = False
    def handle_starttag(self, tag, attrs):
        if tag == 'body':
            self.in_body = True
        if self.in_body and self.depth < 4:
            attr_dict = dict(attrs)
            id_str = f" id='{attr_dict.get('id', '')}'" if 'id' in attr_dict else ""
            cls_str = f" class='{attr_dict.get('class', '')}'" if 'class' in attr_dict else ""
            print("  " * self.depth + f"<{tag}{id_str}{cls_str}>")
            self.depth += 1
        elif self.in_body:
            self.depth += 1
            
    def handle_endtag(self, tag):
        if self.in_body:
            self.depth -= 1
        if tag == 'body':
            self.in_body = False

with open('dyners_raw.html', 'r', encoding='utf-8') as f:
    html = f.read()

parser = StructureParser()
parser.feed(html)
