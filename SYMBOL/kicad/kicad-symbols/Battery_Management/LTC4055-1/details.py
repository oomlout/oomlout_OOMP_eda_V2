
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "LTC4055-1"
    hexID = "SZKBATMANAGEMENTLTC4551"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LTC4055', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC4055-1', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-16-1EP_4x4mm_P0.65mm_EP2.15x2.15mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/4055fb.pdf', 'kicadSymbolki_keywords': 'charger PMIC Liion USB', 'kicadSymbolki_description': 'USB Power Controller and Li-Ion Charger (4.1V Float Voltage)', 'kicadSymbolki_fp_filters': 'QFN*1EP*4x4mm*P0.65mm*'}])
    newPart['name'].append('Battery_Management : LTC4055-1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

