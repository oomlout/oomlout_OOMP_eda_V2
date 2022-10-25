
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "MCP4921"
    hexID = "SZKANALOGDACMCP4921"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP4901', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP4921', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/22248a.pdf', 'kicadSymbolki_keywords': '12-Bit DAC SPI 1ch', 'kicadSymbolki_description': '12-Bit D/A Converters with SPI Interface', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* MSOP*3x3mm*P0.65mm* SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Analog_DAC : MCP4921')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

