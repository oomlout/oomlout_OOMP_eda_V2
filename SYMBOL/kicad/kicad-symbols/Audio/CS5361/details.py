
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "CS5361"
    hexID = "SZKAUDIOCS5361"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CS5361', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://d3uzseaevmutz1.cloudfront.net/pubs/proDatasheet/CS5361_F2.pdf', 'kicadSymbolki_keywords': 'audio adc 2ch 24bit 192kHz', 'kicadSymbolki_description': '114 dB, 192 kHz, Multi-Bit Audio A/D Converter, SOIC-24/TSSOP-24', 'kicadSymbolki_fp_filters': 'SOIC*7.5x15.4mm*P1.27mm* TSSOP*4.4x7.8mm*P0.65mm*'}])
    newPart['name'].append('CS5361')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

