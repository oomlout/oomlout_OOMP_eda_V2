
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "MCP14A0305xMNY"
    hexID = "SZKDRIVERFETMCP14A35XMNY"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP14A0305xMNY', 'kicadSymbolFootprint': 'Package_DFN_QFN:WDFN-8-1EP_3x2mm_P0.5mm_EP1.3x1.4mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/MCP14A0303_4_5-Data-Sheet-20006046A.pdf', 'kicadSymbolki_keywords': 'Driver, Dual MOSFET', 'kicadSymbolki_description': 'Dual 3A-Peak MOSFET Driver, inverting/non-inverting outputs, DFN-8', 'kicadSymbolki_fp_filters': 'WDFN*1EP*3x2mm*P0.5mm*EP1.3x1.4mm*'}])
    newPart['name'].append('Driver_FET : MCP14A0305xMNY')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

