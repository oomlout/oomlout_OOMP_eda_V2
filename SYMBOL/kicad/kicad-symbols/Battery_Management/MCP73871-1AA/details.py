
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "MCP73871-1AA"
    hexID = "SZKBATMANAGEMENTMCP738711AA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP73871', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP73871-1AA', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-20-1EP_4x4mm_P0.5mm_EP2.5x2.5mm', 'kicadSymbolDatasheet': 'http://www.mouser.com/ds/2/268/22090a-52174.pdf', 'kicadSymbolki_keywords': 'battery charger lithium', 'kicadSymbolki_description': 'Single cell, Li-Ion/Li-Po charge management controller, 4.10V', 'kicadSymbolki_fp_filters': 'QFN*4x4mm*P0.5mm*'}])
    newPart['name'].append('Battery_Management : MCP73871-1AA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

