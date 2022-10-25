
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "LTC4242xUHF"
    hexID = "SZKPOWERMANAGEMENTLTC4242XUHF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC4242xUHF', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-38-1EP_5x7mm_P0.5mm_EP3.15x5.15mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/4242f.pdf', 'kicadSymbolki_keywords': 'Dual-Slot PCIe', 'kicadSymbolki_description': 'Hot-Swap Power Controller, QFN-38', 'kicadSymbolki_fp_filters': 'QFN*1EP*5x7mm*P0.5mm*'}])
    newPart['name'].append('Power_Management : LTC4242xUHF')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

