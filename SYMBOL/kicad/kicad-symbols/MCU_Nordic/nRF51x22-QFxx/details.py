
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Nordic"
    oIndex = "nRF51x22-QFxx"
    hexID = "SZKMCUNORDICNRF51X22QFXX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'nRF51x22-QFxx', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-48-1EP_6x6mm_P0.4mm_EP4.6x4.6mm', 'kicadSymbolDatasheet': 'http://infocenter.nordicsemi.com/pdf/nRF51822_PS_v3.3.pdf', 'kicadSymbolki_keywords': 'MCU, ARM, BLE, 2.4GHz', 'kicadSymbolki_description': 'Multiprotocol BLE/2.4GHz Cortex-M0+ SoC', 'kicadSymbolki_fp_filters': 'QFN*1EP*6x6mm*P0.4mm*'}])
    newPart['name'].append('MCU_Nordic : nRF51x22-QFxx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

