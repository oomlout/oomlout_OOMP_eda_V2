
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "MCP3425A2T-ECH"
    hexID = "SZKANALOGADCMCP3425A2TECH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP3425A0T-ECH', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP3425A2T-ECH', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/22072b.pdf', 'kicadSymbolki_keywords': 'Sigma-Delta ADC Converter 16bit I2C 1ch', 'kicadSymbolki_description': 'Single Delta-Sigma 16bit Analog to Digital Converter, I2C Interface, SOT-23-6', 'kicadSymbolki_fp_filters': 'SOT?23* SOT?23*'}])
    newPart['name'].append('MCP3425A2T-ECH')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

