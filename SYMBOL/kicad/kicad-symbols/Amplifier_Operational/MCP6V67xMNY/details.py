
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "MCP6V67xMNY"
    hexID = "SZKAMPLIFIEROPERATIONALMCP6V67XMNY"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP6V67xMNY', 'kicadSymbolFootprint': 'Package_DFN_QFN:TDFN-8-1EP_3x2mm_P0.5mm_EP1.3x1.4mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/MCP6V66-Family-Data-Sheet-DS20006266A.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'dual opamp zero drift', 'kicadSymbolki_description': 'Dual Operational Amplifiers, Zero-Drift, 80 kHz Bandwidth, 1.8V to 5.5V, Rail-to-Rail, TDFN-8', 'kicadSymbolki_fp_filters': 'TDFN*1EP*3x2mm*P0.5mm*'}])
    newPart['name'].append('Amplifier_Operational : MCP6V67xMNY')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

