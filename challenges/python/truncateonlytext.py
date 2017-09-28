"""
Alex was assigned with the following task last week: he needs to truncate a text with HTML tags up to the given position. The trick is, the 
string must be truncate only by plain text, ignoring tags.

Can you help Alex with his assignment?

It is guaranteed that text contains valid HTML tags, for each opening tag there is a closing tag, and there are no nested tags. It is also 
guaranteed that symbols < and > appear only in HTML tags.

The returned text should also contain only valid HTML tags. If the text should be truncated in the middle of some text wrapped into the tags, 
the resulting string should not contain this tag.

Example

For text = "You ordered <b>two</b> pizzas with <i>mushrooms</i> and vanilla <i>milkshake</i>."
and position = 50, the output should be

truncateOnlyText(text, position) = 
  "You ordered <b>two</b> pizzas with <i>mushrooms</i> and vanilla "
Input/Output

[time limit] 4000ms (py)
[input] string text

Text with HTML tags.

Contraints:
1 ≤ text.length ≤ 700.

[input] integer position

A positive integer representing the position to truncate the text on. It is guaranteed that its value is smaller than the total length of plain 
text in the given string.

[output] string

Truncated text.

# Challenge's link: https://codefights.com/challenge/Cd7C88jKTp4SsrA5S/main #
"""
def truncateOnlyText(text, position):
    available_space = position
    res = []
    
    i = 0
    while available_space > 0:
        char = text[i]
        if char == '<':
            elem = get_html_element(i, text)
            content = extract_content(elem)
            i += len(elem) - 1
            
            if len(content) <= available_space:
                res.append(elem)
                available_space -= len(content)
            else:
                res.append(content[:available_space])
                break
        else:
            res.append(char)
            available_space -= 1
        i += 1
    return ''.join(res)
            

def extract_content(html_element):
    pattern = r'<.+>(.+)</.+>'
    elem = re.findall(pattern, html_element)
    
    if len(elem) > 0:
        return elem[0]
    else:
        return ""
    

def get_html_element(start_pos, text):
    symbols = ['>', '/', '<', '>', '<']
    elem = ''
    
    for i in range(start_pos, len(text)):
        char = text[i]
         
        if len(symbols) == 0:
            break
        elem += char
        if char == symbols[-1]:
            symbols.pop()
    return elem


# SOLUTIONS BY OTHER PLAYERS
def truncateOnlyText(text, position):
    res = []
    cnt = 0
    is_tag = False
    tag_opened = False

    for i, ch in enumerate(text):
        res.append(ch)
        if is_tag:
            if ch == '>':
                is_tag = False
                tag_opened = not tag_opened
        else:
            if ch == '<':
                is_tag = True
            else:
                cnt += 1
        if cnt == position:
            break
    if tag_opened:
        i += 1
        if text[i] == '<':
            while text[i] != '>':
                res.append(text[i])
                i += 1
            res.append(text[i])
        else:
            res = ''.join(res)
            res = res[:res.rfind('<')] + res[res.rfind('>') + 1:]
            return res
    return ''.join(res)