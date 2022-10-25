
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "MCP4921-EMS"
    hexID = "SZKANALOGDACMCP4921EMS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP4921-EMS', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/devicedoc/21897a.pdf', 'kicadSymbolki_keywords': 'Single DAC 1ch 12bit SPI', 'kicadSymbolki_description': 'Single 12-bit Digital to Analog Converter, SPI Interface, MSOP-8', 'kicadSymbolki_fp_filters': 'MSOP* SOIC* DIP* PDIP*'}])
    newPart['name'].append('Analog_DAC : MCP4921-EMS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

