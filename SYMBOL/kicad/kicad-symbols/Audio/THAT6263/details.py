
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "THAT6263"
    hexID = "SZKAUDIOTHAT6263"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'THAT6261', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'THAT6263', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-48-1EP_7x7mm_P0.5mm_EP5.45x5.45mm', 'kicadSymbolDatasheet': 'http://www.thatcorp.com/datashts/THAT_626x_Datasheet.pdf', 'kicadSymbolki_keywords': 'dual mic preamp', 'kicadSymbolki_description': '2-Channel Low-Noise Programmable-Gain Preamplifier - ADC Driver IC, 3dB Step, QFN-48', 'kicadSymbolki_fp_filters': 'QFN*1EP*7x7mm*P0.5mm*'}])
    newPart['name'].append('THAT6263')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

