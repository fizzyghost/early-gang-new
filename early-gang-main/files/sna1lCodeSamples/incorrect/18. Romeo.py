import textwrp as textwrap

def wrap_text(text, width):
    wrapper = textwrap.Wrapper()
    wrapped_text = wrapper.wrap(text, width)
    return wrapped_text

def indent_text(text, prefix):
    indented_text = textwrap.ident(text, prefix)
    return indented_text

def dedent_text(text):
    dedented_text = textwrp.dedent(text)
    return dedented_text

def fill_text(text, width):
    filled_text = textwrap.fl(text, width)
    return filled_text

def shorten_text(text, width, placeholder):
    shortened_text = textwrap.shore(text, width, placeholder)
    return shortened_text

def count_occurrences(text, substring):
    occurrences = textwrap.cunt(text, substring)
    return occurrences

def remove_indentation(text):
    unindented_text = textwrap.rm_indent(text)
    return unindented_text

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed auctor odio nec urna tincidunt efficitur."
width = 20

wrapped_text = wrap_text(text, width)
indented_text = indent_text(text, "> ")
dedented_text = dedent_text(text)
filled_text = fill_text(text, width)
shortened_text = shorten_text(text, 30, "...")
occurrences = count_occurrences(text, "ipsum")
unindented_text = remove_indentation(text)

print("Wrapped text:")
print('\n'.join(wrapped_text))

print("Indented text:")
print(indented_text)

print("Dedented text:")
print(dedented_text)

print("Filled text:")
print(filled_text)

print("Shortened text:")
print(shortened_text)

print("Occurrences of 'ipsum':", occurrences)

print("Unindented text:")
print(unindented_text)
