LARGE XML file => Processing Machine (RAM Limit, cannot load at once) => Output. Solution?

1. Read small chunk (Buffer 64KB)
2. SAX Parser to detect the expected tags/data
3. Process and output incrementally
4. Discard processed data


cur_trans, cur_field, text_parts = None, None, []

def on_start_tag(tag):
	if tag == "trans": cur_trans = {}; return
	if tag in {"id", "amount", "user_id", "time", "note"}:
		cur_field = tag
		text_parts = []

def on_text(text):
	if cur_field: text_parts.append(text) # text can across buffs

def on_end_tag(tag)
	if tag == cur_field:
		cur_trans[tag] = "".join(text_parts)
		cur_field = None
		text_parts = []
		return
	if tag == "trans":
		write_trans(cur_trans)
		cur_trans = None

parser=SAXParser(on_start=on_start_tag, on_text=on_text, on_end=on_end_tag)

with open("l.xml", "rb") as file:
	while buffer := file.read(64*1024):
		parser.feed(buffer)
parser.finish

	