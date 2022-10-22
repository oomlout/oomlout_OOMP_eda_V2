
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "MCP3421A0T-ECH"
    hexID = "SZKANALOGADCMCP3421ATECH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP3425A0T-ECH', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP3421A0T-ECH', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/22003e.pdf', 'kicadSymbolki_keywords': 'Sigma-Delta ADC Converter 18bit I2C 1ch', 'kicadSymbolki_description': 'Single Delta-Sigma 18bit Analog to Digital Converter, I2C Interface, SOT-23-6', 'kicadSymbolki_fp_filters': 'SOT?23* SOT?23*'}])
    newPart['name'].append('MCP3421A0T-ECH')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

