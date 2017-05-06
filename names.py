
def mangle(name, args):
    parts = [p.replace('_', '__') for p in [name] + args]
    return '_'.join(parts)

def unmangle(s):
    parts = ['']
    i = 0
    while i < len(s):
        if s[i] == '_':
            if i < len(s)-1 and s[i+1] == '_':
                parts[-1] += '_'
                i += 1
            else:
                parts.append('')
        else:
            parts[-1] += s[i]
        i += 1
    return parts[0], parts[1:]
