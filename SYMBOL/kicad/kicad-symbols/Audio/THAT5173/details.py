
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "THAT5173"
    hexID = "SZKAUDIOTHAT5173"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'THAT5173', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-24-1EP_5x5mm_P0.65mm_EP3.4x3.4mm', 'kicadSymbolDatasheet': 'http://www.thatcorp.com/datashts/THAT_5173_Datasheet.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'mic preamp gain controller', 'kicadSymbolki_description': 'Audio Preamplifier Digital Controller IC, QFN-24', 'kicadSymbolki_fp_filters': 'QFN*1EP*5x5mm*P0.65mm*'}])
    newPart['name'].append('Audio : THAT5173')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

