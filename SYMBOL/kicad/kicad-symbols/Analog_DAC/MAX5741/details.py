
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "MAX5741"
    hexID = "SZKANALOGDACMAX5741"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX5741', 'kicadSymbolFootprint': 'Package_SO:MSOP-10_3x3mm_P0.5mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX5741.pdf', 'kicadSymbolki_keywords': 'DA 8 Bit 4 ch', 'kicadSymbolki_description': 'Digital to analog, 10 Bit, 4 ch, 2.7 - 5.5 VDD, SPI, uMAX-10', 'kicadSymbolki_fp_filters': 'MSOP*3x3mm?P0.5mm*'}])
    newPart['name'].append('MAX5741')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

