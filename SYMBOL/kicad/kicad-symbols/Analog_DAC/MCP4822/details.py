
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "MCP4822"
    hexID = "SZKANALOGDACMCP4822"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP4802', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP4822', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/20002249B.pdf', 'kicadSymbolki_keywords': '12-Bit DAC SPI Reference 2ch', 'kicadSymbolki_description': '2-Channel 12-Bit D/A Converters with SPI Interface and Internal Reference (2.048V)', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x4.9mm*P1.27mm* MSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Analog_DAC : MCP4822')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

