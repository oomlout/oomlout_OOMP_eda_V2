
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "MAX5815"
    hexID = "SZKANALOGDACMAX5815"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX5813', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX5815', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://datasheets.maximintegrated.com/en/ds/MAX5813-MAX5815.pdf', 'kicadSymbolki_keywords': 'DA 12 Bit 4 ch', 'kicadSymbolki_description': 'Digital to analog, 12 Bit, 4 ch, 2.7 - 5.5 VDD, I2C, TSSOP-14', 'kicadSymbolki_fp_filters': '*TSSOP*14*4.4*'}])
    newPart['name'].append('MAX5815')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

