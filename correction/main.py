import regex
import underthesea
import enchant
from flask import Flask, request
from transformers import pipeline
from flask_cors import CORS, cross_origin

corrector = pipeline("text2text-generation", model="bmd1905/vietnamese-correction")
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['POST'])
@cross_origin()
def find_mistake():
    text = request.get_data(as_text=True)
    mistakes = []

    p = regex.compile(" {2,}")
    for m in p.finditer(text):
        mistakes.append(
            {
                "text": m.group(),
                "desc": "Nhiều dấu cách",
                "bound": [(m.start(), m.end())],
                "fix": " ",
            }
        )

    p = regex.compile(" ([.,!?])")
    for m in p.finditer(text):
        mistakes.append(
            {
                "text": m.group(),
                "desc": "Khoảng cách trước dấu câu",
                "bound": [(m.start(), m.end())],
                "fix": m.group(1),
            }
        )

    p = regex.compile("([.,!?])(\S)")
    for m in p.finditer(text):
        mistakes.append(
            {
                "text": m.group(),
                "desc": "Thiếu khoảng cách ở cuối câu",
                "bound": [(m.start(), m.end())],
                "fix": m.group(1) + " " + (m.group(2) if m.group(2) != None else ""),
            }
        )

    p = regex.compile("(?<=[\.!?] )(\p{Ll})")
    for m in p.finditer(text):
        mistakes.append(
            {
                "text": m.group(),
                "desc": "Viết hoa khi bắt đầu câu",
                "bound": [(m.start(), m.end())],
                "fix": m.group(1).title(),
            }
        )

    tokens = underthesea.pos_tag(text)
    words = [token[0] for token in tokens if token[1] != "CH"]

    word_count = {}
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

    for word in (key for key, value in word_count.items() if value > 1):
        mistakes.append(
            {
                "text": word,
                "desc": "Lặp lại từ",
                "bound": [(m.start(), m.end()) for m in regex.finditer(word, text)],
                "fix": None,
            }
        )

    d = enchant.Dict("vi_VN")
    idx_text = text
    start = 0
    for word in words:
        if not d.check(word):
            fix = corrector(word)[0]['generated_text'].lower()[:-1] # replace with transformer thing
            if fix != word.lower():
                start += idx_text.find(word)
                mistakes.append(
                    {
                        "text": word,
                        "desc": "Lỗi chính tả",
                        "bound": (start, start + len(word)),
                        "fix": fix,
                    }
                )
            idx_text = idx_text[start:]

    return mistakes

if __name__ == '__main__':
    app.run(port=8008)