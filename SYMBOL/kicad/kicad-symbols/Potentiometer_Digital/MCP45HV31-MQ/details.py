
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Potentiometer_Digital"
    oIndex = "MCP45HV31-MQ"
    hexID = "SZKPOTENTIOMETERDIGITALMCP45HV31MQ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP45HV51-MQ', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP45HV31-MQ', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-20-1EP_5x5mm_P0.65mm_EP3.35x3.35mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/20005304A.pdf', 'kicadSymbolki_keywords': 'I2C Potentiometer pot digital', 'kicadSymbolki_description': '7/8-bit single +36V (+/-18V) digital pot, I2C serial interface, volatile memory, QFN-20', 'kicadSymbolki_fp_filters': 'QFN*5x5mm*P0.65mm*'}])
    newPart['name'].append('MCP45HV31-MQ')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

