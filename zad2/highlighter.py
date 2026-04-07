STYLES = {
    "KEYWORD": "color: blue; font-weight: bold;",
    "IDENTIFIER": "color: black;",
    "NUMBER": "color: red;",
    "STRING": "color: green;",
    "OPERATOR": "color: purple;",
    "SEPARATOR": "color: gray;",
    "COMMENT": "color: #888; font-style: italic;",
    "WHITESPACE": ""
}

def highlight(tokens):
    html = ""

    for token in tokens:
        style = STYLES[token.type]

        if token.type == "WHITESPACE":
            html += token.value
        else:
            html += f'<span style="{style}">{token.value}</span>'

    return html


def wrap_html(content):
    return f"""
<html>
<head>
<meta charset="UTF-8">
<title>Syntax Highlight</title>
</head>
<body>
<pre>
{content}
</pre>
</body>
</html>
"""