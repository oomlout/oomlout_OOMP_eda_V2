
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "SAD1024"
    hexID = "SZKAUDIOSAD124"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SAD1024', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://thmq.mysteria.cz/em1022/SAD1024.pdf', 'kicadSymbolki_keywords': 'EG&G RETICON BBD N-channel silicon-gate', 'kicadSymbolki_description': 'SAD-1024 DUAL ANALOG DELAY LINE, bucket brigade device, 2 independent 512 stages, signal frequency range 0 to 200KHz, clock frequency range 1.5KHz to 1.5MHz', 'kicadSymbolki_fp_filters': 'DIP-16*'}])
    newPart['name'].append('SAD1024')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

