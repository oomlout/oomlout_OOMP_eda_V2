
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "MCP4921-EP"
    hexID = "SZKANALOGDACMCP4921EP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP4921-EMS', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP4921-EP', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/devicedoc/21897a.pdf', 'kicadSymbolki_keywords': 'Single DAC 1ch 12bit SPI', 'kicadSymbolki_description': 'Single 12-bit Digital to Analog Converter, SPI Interface, PDIP-8', 'kicadSymbolki_fp_filters': 'MSOP* SOIC* DIP* PDIP*'}])
    newPart['name'].append('MCP4921-EP')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

