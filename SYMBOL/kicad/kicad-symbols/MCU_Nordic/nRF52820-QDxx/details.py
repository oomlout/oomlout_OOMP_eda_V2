
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Nordic"
    oIndex = "nRF52820-QDxx"
    hexID = "SZKMCUNORDICNRF5282QDXX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'nRF52820-QDxx', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-40-1EP_5x5mm_P0.4mm_EP3.6x3.6mm', 'kicadSymbolDatasheet': 'https://infocenter.nordicsemi.com/pdf/nRF52820_PS_v1.0.pdf', 'kicadSymbolki_keywords': 'MCU, ARM, BLE, ANT, 2.4GHz, 802.15.4', 'kicadSymbolki_description': 'Multiprotocol BLE/ANT/2.4 GHz/802.15.4 Cortex-M4 SoC, QFN-40', 'kicadSymbolki_fp_filters': 'QFN*1EP*5x5mm*P0.4mm*'}])
    newPart['name'].append('nRF52820-QDxx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

