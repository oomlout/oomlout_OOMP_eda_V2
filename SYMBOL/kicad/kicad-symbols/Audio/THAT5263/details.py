
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "THAT5263"
    hexID = "SZKAUDIOTHAT5263"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'THAT5263', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-24-1EP_5x5mm_P0.65mm_EP3.4x3.4mm', 'kicadSymbolDatasheet': 'http://www.thatcorp.com/datashts/THAT_5263_Datasheet.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'dual mic preamp gain controller', 'kicadSymbolki_description': '2-Channel Digital Preamplifier Controller IC, QFN-24', 'kicadSymbolki_fp_filters': 'QFN*1EP*5x5mm*P0.65mm*'}])
    newPart['name'].append('Audio : THAT5263')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

