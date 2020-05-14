import re
import textwrap




def items_len(line):
    return sum([len(x) for x in line])


space_re = re.compile(r'(^\s+)(.*)$')


def align_string(ln, width):
    # check the whitespace at beginning
    sp = space_re.match(ln)
    if sp is None:
        start, end, w = '', ln, width
    else:
        start, end, w = sp.group(1), sp.group(2), width - len(sp.group(1))

    linewordlist = end.split()

    # add required space to each words, exclude last word
    for i in range(len(linewordlist) - 1):
        linewordlist[i] += ' '


    # number of spaces to add
    left_count = w - items_len(linewordlist)
    while left_count > 0 and len(linewordlist) > 1:
        for i in range(len(linewordlist) - 1):
            linewordlist[i] += ' '
            left_count -= 1
            if left_count < 1:
                break

    res = start + ''.join(linewordlist)
    return res


def splitalign_paragraph(paragraph, width):

    lines = list()
    if type(paragraph) == type(lines):
        lines.extend(paragraph)
    elif type(paragraph) == type(''):
        lines.append(paragraph)
    elif type(paragraph) == type(tuple()):
        lines.extend(list(paragraph))
    else:
        print("Please enter correct Data {}", Paragraph)

    flatten_para = ' '.join(lines)

    splitwrap = textwrap.wrap(flatten_para, width)

    wrapped = list()
    while len(splitwrap) > 0:
        line = splitwrap.pop(0)
        aligned = align_string(line, width)
        wrapped.append(aligned)

    return wrapped

Paragraph = "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works."
Page_Width: int = 20

print("Paragraph = ", Paragraph)
print("Page_Width = ", Page_Width)
print("Below is the Output\n_____________", Page_Width * '_')
#print("_____________", Page_Width * '_')

final_wrap = splitalign_paragraph(Paragraph, Page_Width)
i: int = 1
for y in final_wrap:
    print(f'Array [{i}] = "{y}"')
    i += 1
