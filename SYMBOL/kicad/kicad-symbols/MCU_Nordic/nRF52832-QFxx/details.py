
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Nordic"
    oIndex = "nRF52832-QFxx"
    hexID = "SZKMCUNORDICNRF52832QFXX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'nRF52832-QFxx', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-48-1EP_6x6mm_P0.4mm_EP4.6x4.6mm', 'kicadSymbolDatasheet': 'http://infocenter.nordicsemi.com/pdf/nRF52832_PS_v1.4.pdf', 'kicadSymbolki_keywords': 'MCU, ARM, BLE, 2.4GHz', 'kicadSymbolki_description': 'Multiprotocol BLE/2.4GHz Cortex-M4 SoC, QFN-48', 'kicadSymbolki_fp_filters': 'QFN*1EP*6x6mm*P0.4mm*'}])
    newPart['name'].append('MCU_Nordic : nRF52832-QFxx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

