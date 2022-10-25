
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "CS8416-xNZ"
    hexID = "SZKAUDIOCS8416XNZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CS8416-xNZ', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-28-1EP_5x5mm_P0.5mm_EP3.35x3.35mm', 'kicadSymbolDatasheet': 'https://d3uzseaevmutz1.cloudfront.net/pubs/proDatasheet/CS8416_F3.pdf', 'kicadSymbolki_keywords': 'audio digital interface receiver', 'kicadSymbolki_description': '192 kHz Digital Audio Interface Receiver, QFN-28', 'kicadSymbolki_fp_filters': 'QFN*5x5mm*P0.5mm*'}])
    newPart['name'].append('Audio : CS8416-xNZ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

