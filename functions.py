
def procesar_mensaje2(message):

    words = message.split()
    mode = words[0]
    text = ''
    name = ''

    if 'texto' in words:
        index_texto = words.index('texto')

    if index_texto < len(words) - 1:
        text = ' '.join(words[index_texto+1:])
        
    if index_texto > 1:
        name = ' '.join(words[1:index_texto])
        
    return mode, text, name


def procesar_chat(message):

    words = message.split()

    mode = words[0]

    text = ' '.join(words[1:])

    return mode, text


def procesar_google(message):

    words = message.split()

    mode = words[0]

    text = ' '.join(words[1:])

    return mode, text








