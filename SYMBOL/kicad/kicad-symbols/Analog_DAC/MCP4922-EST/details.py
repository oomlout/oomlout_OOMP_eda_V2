
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "MCP4922-EST"
    hexID = "SZKANALOGDACMCP4922EST"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP4922-EP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP4922-EST', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/devicedoc/21897a.pdf', 'kicadSymbolki_keywords': 'Dual DAC 1ch 12bit SPI', 'kicadSymbolki_description': 'Dual 12-bit Digital to Analog Converter, SPI Interface, TSSOP-14', 'kicadSymbolki_fp_filters': 'DIP* PDIP* SO* SOIC* TSSOP*'}])
    newPart['name'].append('Analog_DAC : MCP4922-EST')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

