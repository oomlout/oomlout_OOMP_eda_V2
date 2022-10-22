
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "MCP14A1201xMNY"
    hexID = "SZKDRIVERFETMCP14A121XMNY"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP14A0901xMNY', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP14A1201xMNY', 'kicadSymbolFootprint': 'Package_DFN_QFN:TDFN-8-1EP_3x2mm_P0.5mm_EP1.3x1.4mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/MCP14A1201-Family-Data-Sheet-DS20006228A.pdf', 'kicadSymbolki_keywords': 'Driver, Dual MOSFET', 'kicadSymbolki_description': 'Dual 12A-Peak MOSFET Driver, inverting outputs, DFN-8', 'kicadSymbolki_fp_filters': 'TDFN*1EP*3x2mm*P0.5mm*'}])
    newPart['name'].append('MCP14A1201xMNY')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

