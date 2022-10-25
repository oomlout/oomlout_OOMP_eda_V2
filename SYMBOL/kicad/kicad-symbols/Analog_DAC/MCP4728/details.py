
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "MCP4728"
    hexID = "SZKANALOGDACMCP4728"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP4728', 'kicadSymbolFootprint': 'Package_SO:MSOP-10_3x3mm_P0.5mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/22187E.pdf', 'kicadSymbolki_keywords': 'dac i2c', 'kicadSymbolki_description': '12-bit digital to analog converter, quad output, 2.048V internal reference, integrated EEPROM, I2C interface', 'kicadSymbolki_fp_filters': '*SOP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Analog_DAC : MCP4728')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

