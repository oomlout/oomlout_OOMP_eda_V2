
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "CS8406"
    hexID = "SZKAUDIOCS846"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CS8406', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://d3uzseaevmutz1.cloudfront.net/pubs/proDatasheet/CS8406_F6.pdf', 'kicadSymbolki_keywords': 'audio digital interface transmitter 192kHz', 'kicadSymbolki_description': '192 kHz Digital Audio Interface Transmitter, SOIC-28/TSSOP-28', 'kicadSymbolki_fp_filters': 'SOIC*7.5x17.9mm*P1.27mm* TSSOP*4.4x9.7mm*P0.65mm*'}])
    newPart['name'].append('CS8406')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

