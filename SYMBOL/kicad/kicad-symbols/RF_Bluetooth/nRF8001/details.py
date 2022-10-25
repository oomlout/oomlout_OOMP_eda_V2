
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Bluetooth"
    oIndex = "nRF8001"
    hexID = "SZKRFBLUETOOTHNRF81"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'nRF8001', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-32-1EP_5x5mm_P0.5mm_EP3.45x3.45mm', 'kicadSymbolDatasheet': 'https://www.nordicsemi.com/eng/nordic/content_download/2981/38488/file/nRF8001_PS_v1.3.pdf', 'kicadSymbolki_keywords': 'BLE, bluetooth', 'kicadSymbolki_description': 'BLE LE Connectivity IC, QFN-32', 'kicadSymbolki_fp_filters': 'QFN*1EP*5x5mm*P0.5mm*'}])
    newPart['name'].append('RF_Bluetooth : nRF8001')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

