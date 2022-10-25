
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "SAD512"
    hexID = "SZKAUDIOSAD512"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SAD1024', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SAD512', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://thmq.mysteria.cz/em1022/SAD1024.pdf', 'kicadSymbolki_keywords': 'EG&G RETICON BBD N-channel silicon-gate', 'kicadSymbolki_description': 'SAD-512 ANALOG DELAY LINE, bucket brigade device, 512 stages, signal frequency range 0 to 200KHz, clock frequency range 1.5KHz to 1.5MHz', 'kicadSymbolki_fp_filters': 'DIP-16*'}])
    newPart['name'].append('Audio : SAD512')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

