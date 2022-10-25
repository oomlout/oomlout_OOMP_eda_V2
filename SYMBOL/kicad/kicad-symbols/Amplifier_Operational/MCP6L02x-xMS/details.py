
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "MCP6L02x-xMS"
    hexID = "SZKAMPLIFIEROPERATIONALMCP6L2XXMS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'NCS2325DM', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP6L02x-xMS', 'kicadSymbolFootprint': 'Package_SO:MSOP-8_3x3mm_P0.65mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/devicedoc/22140b.pdf', 'kicadSymbolki_keywords': 'opamp vfa r2r rtr', 'kicadSymbolki_description': 'Dual, 1 MHz, 85µA, Rail-to-Rail input and output, MSOP-8', 'kicadSymbolki_fp_filters': 'MSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Amplifier_Operational : MCP6L02x-xMS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

