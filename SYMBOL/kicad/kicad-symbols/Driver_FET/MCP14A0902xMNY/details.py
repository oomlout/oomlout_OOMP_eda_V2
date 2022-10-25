
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "MCP14A0902xMNY"
    hexID = "SZKDRIVERFETMCP14A92XMNY"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP14A0902xMNY', 'kicadSymbolFootprint': 'Package_DFN_QFN:TDFN-8-1EP_3x2mm_P0.5mm_EP1.3x1.4mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/MCP14A0901_2-Data-Sheet-20006183A.pdf', 'kicadSymbolki_keywords': 'Driver, Dual MOSFET', 'kicadSymbolki_description': 'Dual 9A-Peak MOSFET Driver, non-inverting outputs, DFN-8', 'kicadSymbolki_fp_filters': 'TDFN*1EP*3x2mm*P0.5mm*'}])
    newPart['name'].append('Driver_FET : MCP14A0902xMNY')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

