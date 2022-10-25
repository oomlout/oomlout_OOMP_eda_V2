
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "MCP6002-xMC"
    hexID = "SZKAMPLIFIEROPERATIONALMCP62XMC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP6002-xMC', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8-1EP_3x2mm_P0.5mm_EP1.75x1.45mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/21733j.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'dual opamp', 'kicadSymbolki_description': '1MHz, Low-Power Op Amp, DFN-8', 'kicadSymbolki_fp_filters': 'DFN*1EP*3x2mm*P0.5mm*'}])
    newPart['name'].append('Amplifier_Operational : MCP6002-xMC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

