
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "MCP4912"
    hexID = "SZKANALOGDACMCP4912"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP4902', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP4912', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/22250A.pdf', 'kicadSymbolki_keywords': '10-Bit DAC SPI 2ch', 'kicadSymbolki_description': '2-Channel 10-Bit D/A Converters with SPI Interface', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x8.7mm*P1.27mm* TSSOP*4.4x5mm*P0.65mm*'}])
    newPart['name'].append('Analog_DAC : MCP4912')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

