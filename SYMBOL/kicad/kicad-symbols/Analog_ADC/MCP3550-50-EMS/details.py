
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "MCP3550-50-EMS"
    hexID = "SZKANALOGADCMCP3555EMS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP3550-50-EMS', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/devicedoc/21950c.pdf', 'kicadSymbolki_keywords': 'Sigma-Delta ADC Converter 22bit SPI 1ch', 'kicadSymbolki_description': 'Single Delta-Sigma 22bit Analog to Digital Converter, SPI Interface, 50Hz Rejection, MSOP-8', 'kicadSymbolki_fp_filters': 'MSOP*'}])
    newPart['name'].append('MCP3550-50-EMS')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

