
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "MCP4911-EMC"
    hexID = "SZKANALOGDACMCP4911EMC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP4901-EMC', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP4911-EMC', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8-1EP_3x2mm_P0.5mm_EP1.75x1.45mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/22248a.pdf', 'kicadSymbolki_keywords': '10-Bit DAC SPI  1ch', 'kicadSymbolki_description': '10-Bit D/A Converters with SPI Interface', 'kicadSymbolki_fp_filters': 'DFN*1EP*3x2mm*P0.5mm*'}])
    newPart['name'].append('Analog_DAC : MCP4911-EMC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

