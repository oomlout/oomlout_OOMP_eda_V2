
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "THAT5171"
    hexID = "SZKAUDIOTHAT5171"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'THAT5171', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-32-1EP_7x7mm_P0.65mm_EP5.4x5.4mm', 'kicadSymbolDatasheet': 'http://www.thatcorp.com/datashts/THAT_5171_Datasheet.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'mic preamp gain controller', 'kicadSymbolki_description': 'High-Performance Digital Preamplifier Controller IC, QFN-32', 'kicadSymbolki_fp_filters': 'QFN*1EP*7x7mm*P0.65mm*'}])
    newPart['name'].append('Audio : THAT5171')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

