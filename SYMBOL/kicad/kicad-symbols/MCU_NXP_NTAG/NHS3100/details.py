
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_NTAG"
    oIndex = "NHS3100"
    hexID = "SZKMCUNXPNTAGNHS31"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NHS3100', 'kicadSymbolFootprint': 'Package_DFN_QFN:HVQFN-24-1EP_4x4mm_P0.5mm_EP2.6x2.6mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/NHS3100.pdf', 'kicadSymbolki_keywords': 'NFC Cortex-M0', 'kicadSymbolki_description': 'Temperature logger, VQFN-24', 'kicadSymbolki_fp_filters': 'HVQFN*1EP*4x4mm*P0.5mm*'}])
    newPart['name'].append('NHS3100')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

