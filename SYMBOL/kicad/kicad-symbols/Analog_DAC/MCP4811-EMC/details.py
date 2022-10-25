
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "MCP4811-EMC"
    hexID = "SZKANALOGDACMCP4811EMC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP4801-EMC', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP4811-EMC', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8-1EP_3x2mm_P0.5mm_EP1.75x1.45mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/22244B.pdf', 'kicadSymbolki_keywords': '10-Bit DAC SPI Reference 1ch', 'kicadSymbolki_description': '10-Bit D/A Converters with SPI Interface, internal Reference (2.048V)', 'kicadSymbolki_fp_filters': 'DFN*1EP*3x2mm*P0.5mm*'}])
    newPart['name'].append('Analog_DAC : MCP4811-EMC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

