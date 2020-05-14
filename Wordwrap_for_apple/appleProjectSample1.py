import textwrap

Paragraph = "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works."
Page_Width: int = 20

pw = textwrap.wrap(Paragraph, Page_Width, )

i: int = 1
for x in pw:
    print(f'Array [{i}] = "{x.ljust(Page_Width, " ")}"')
    i += 1
