
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "USB3250-ABZJ"
    hexID = "SZKINTERFACEUU325ABZJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'USB3250-ABZJ', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-56-1EP_8x8mm_P0.5mm_EP4.3x4.3mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/00002142A.pdf', 'kicadSymbolki_keywords': 'HS FS Device USB PHY UTMI', 'kicadSymbolki_description': 'Hi-Speed USB Device Transceiver with UTMI Interface, QFN-56', 'kicadSymbolki_fp_filters': 'QFN*1EP*8x8mm*P0.5mm*'}])
    newPart['name'].append('USB3250-ABZJ')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

