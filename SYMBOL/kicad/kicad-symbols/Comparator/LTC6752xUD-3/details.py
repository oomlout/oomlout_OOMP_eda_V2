
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Comparator"
    oIndex = "LTC6752xUD-3"
    hexID = "SZKCOMPARATORLTC6752XUD3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC6752xUD-3', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-12-1EP_3x3mm_P0.5mm_EP1.65x1.65mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/6752fc.pdf', 'kicadSymbolki_keywords': 'single comparator high speed cmos', 'kicadSymbolki_description': 'Single 280Mhz 2.9ns Comparator, Rail-to-Rail Inputs, CMOS Output, QFN-12', 'kicadSymbolki_fp_filters': 'QFN*1EP*3x3mm*P0.5mm*'}])
    newPart['name'].append('LTC6752xUD-3')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

