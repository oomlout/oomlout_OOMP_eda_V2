
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "MAX5139"
    hexID = "SZKANALOGDACMAX5139"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX5139', 'kicadSymbolFootprint': 'Package_DFN_QFN:TQFN-16-1EP_3x3mm_P0.5mm_EP1.23x1.23mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX5138-MAX5139.pdf', 'kicadSymbolki_keywords': '12-bit DAC 1CH', 'kicadSymbolki_description': 'Low-Power, Single, 12-Bit, Buffered Voltage-Output DAC', 'kicadSymbolki_fp_filters': 'TQFN*1EP*3x3mm*P0.5mm*'}])
    newPart['name'].append('MAX5139')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

