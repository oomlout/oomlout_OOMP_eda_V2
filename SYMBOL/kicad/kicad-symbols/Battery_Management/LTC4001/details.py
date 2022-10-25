
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "LTC4001"
    hexID = "SZKBATMANAGEMENTLTC41"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC4001', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-16-1EP_4x4mm_P0.65mm_EP2.15x2.15mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/4001f.pdf', 'kicadSymbolki_keywords': 'Li-Ion charger', 'kicadSymbolki_description': 'Single cell (4.2V) programmable synchronous buck Li-Ion charger, 2A, 5.5V input', 'kicadSymbolki_fp_filters': 'QFN*1EP*4x4mm*P0.65mm*'}])
    newPart['name'].append('Battery_Management : LTC4001')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

