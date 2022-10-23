
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_Kinetis"
    oIndex = "MKW41Z512VHT"
    hexID = "SZKMCUNXPKINETISMKW41Z512VHT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MKW41Z512VHT', 'kicadSymbolFootprint': 'Package_DFN_QFN:NXP_LQFN-48-1EP_7x7mm_P0.5mm_EP3.5x3.5mm_16xMask0.45x0.45_ThermalVias', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/MKW41Z512.pdf', 'kicadSymbolki_keywords': 'Kinetis KW41Z ARM Cortex M0+', 'kicadSymbolki_description': 'Kinetis KW41Z-2.4 GHz, Arm Cortex-M0+, 512kB Flash, 128kB SRAM, Multi Mode: Bluetooth LE and 802.15.4 Wireless Radio and generic FSK, LQFN-48', 'kicadSymbolki_fp_filters': 'NXP*LQFN*1EP*7x7mm*P0.5mm*'}])
    newPart['name'].append('MKW41Z512VHT')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

