
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Temperature"
    oIndex = "MCP9804_DFN"
    hexID = "SZKSENTEMPERATUREMCP984DFN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP9804_DFN', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8-1EP_3x2mm_P0.5mm_EP1.7x1.4mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/22203b.pdf', 'kicadSymbolki_keywords': 'temperature sensor I2C', 'kicadSymbolki_description': '+/-0.25C (+/-1C) Typical (Maximum), Digital Temperature Sensor, DFN-8', 'kicadSymbolki_fp_filters': 'DFN*1EP*3x2mm*P0.5mm*'}])
    newPart['name'].append('Sensor_Temperature : MCP9804_DFN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

