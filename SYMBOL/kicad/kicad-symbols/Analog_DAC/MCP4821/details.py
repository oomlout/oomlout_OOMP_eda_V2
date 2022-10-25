
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "MCP4821"
    hexID = "SZKANALOGDACMCP4821"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP4801', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP4821', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/22244B.pdf', 'kicadSymbolki_keywords': '12-Bit DAC SPI Reference 1ch', 'kicadSymbolki_description': '12-Bit D/A Converters with SPI Interface, internal Reference (2.048V)', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* MSOP*3x3mm*P0.65mm* SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Analog_DAC : MCP4821')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

