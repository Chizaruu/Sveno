import regex

def parseReactHook(content, html, functions, variables):
    hooks = regex.findall(r'(\n|^) *(use[A-Z][a-zA-Z0-9]*)', content)
    for hook in hooks:
        var = regex.search(r'(?<!return )' + hook[1] + r'( *\(.*\))? *;', content)
        if var:
            hookParser = regex.compile(f'({var[2]})(( *\(.*\))? *;)')
            matches = hookParser.findall(html)
            for match in matches:
                replacement = f'let {match[0]}'
                if match[1].strip() != '':
                    replacement += f' = {match[1]}'
                replacement += ';\n'
                html = html.replace(match[0] + match[1], replacement)
    return html, functions, variables