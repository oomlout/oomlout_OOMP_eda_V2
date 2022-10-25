
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Nordic"
    oIndex = "nRF52810-QCxx"
    hexID = "SZKMCUNORDICNRF5281QCXX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'nRF52810-QCxx', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-32-1EP_5x5mm_P0.5mm_EP3.6x3.6mm', 'kicadSymbolDatasheet': 'http://infocenter.nordicsemi.com/pdf/nRF52810_PS_v1.1.pdf', 'kicadSymbolki_keywords': 'MCU, ARM, BLE, 2.4GHz', 'kicadSymbolki_description': 'Multiprotocol BLE/2.4GHz Cortex-M4 SoC, QFN-32', 'kicadSymbolki_fp_filters': 'QFN*1EP*5x5mm*P0.5mm*'}])
    newPart['name'].append('MCU_Nordic : nRF52810-QCxx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

