
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Nordic"
    oIndex = "nRF52840"
    hexID = "SZKMCUNORDICNRF5284"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'nRF52840', 'kicadSymbolFootprint': 'Package_DFN_QFN:Nordic_AQFN-73-1EP_7x7mm_P0.5mm', 'kicadSymbolDatasheet': 'http://infocenter.nordicsemi.com/topic/com.nordic.infocenter.nrf52/dita/nrf52/chips/nrf52840.html', 'kicadSymbolki_keywords': 'MCU, ARM, BLE, ANT, 2.4GHz, 802.15.4', 'kicadSymbolki_description': 'Multiprotocol BLE/ANT/2.4 GHz/802.15.4 Cortex-M4F SoC, AQFN-73', 'kicadSymbolki_fp_filters': 'Nordic*AQFN*1EP*7x7mm*P0.5mm*'}])
    newPart['name'].append('nRF52840')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

