
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "MCP3553-ESN"
    hexID = "SZKANALOGADCMCP3553ESN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP3550-60-ESN', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP3553-ESN', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/devicedoc/21950c.pdf', 'kicadSymbolki_keywords': 'Sigma-Delta ADC Converter 22bit SPI 1ch', 'kicadSymbolki_description': 'Single Delta-Sigma 22bit Analog to Digital Converter, SPI Interface, MSOP-8', 'kicadSymbolki_fp_filters': 'SO*'}])
    newPart['name'].append('MCP3553-ESN')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

