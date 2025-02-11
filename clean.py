import re

def remove_blue_text(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = []
    last_pos = 0
    # Iterate over each match of the \textcolor{blue}{ pattern
    for m in re.finditer(r'\\textcolor{blue}{', content):
        start = m.start()
        # Append the content from the last position to the start of the current match
        new_content.append(content[last_pos:start])
        pos = m.end()  # Position after the opening '{' of the content
        counter = 1  # Start counting braces, starting with the one we just found
        # Find the matching closing '}'
        while pos < len(content):
            if content[pos] == '{':
                counter += 1
            elif content[pos] == '}':
                counter -= 1
                if counter == 0:
                    break
            pos += 1
        # Extract the content inside the braces (excluding the closing '}')
        inner_content = content[m.end():pos]
        new_content.append(inner_content)
        # Update last_pos to the position after the closing '}'
        last_pos = pos + 1
    # Append the remaining content after the last match
    new_content.append(content[last_pos:])
    # Join all parts to form the final content
    result = ''.join(new_content)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(result)

if __name__ == '__main__':
    input_path = '/yourpath/sample-acmsmall-submission.tex'
    output_path = input_path.replace('.tex', '_new.tex')
    remove_blue_text(input_path, output_path)