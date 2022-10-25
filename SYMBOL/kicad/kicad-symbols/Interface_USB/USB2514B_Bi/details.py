
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "USB2514B_Bi"
    hexID = "SZKINTERFACEUU2514BBI"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'USB2514B_Bi', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-36-1EP_6x6mm_P0.5mm_EP3.7x3.7mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/00001692C.pdf', 'kicadSymbolki_keywords': 'USB2.0 Hi-Speed-USB-Hub Hub-Controller', 'kicadSymbolki_description': 'USB 2.0 Hi-Speed Hub Controller', 'kicadSymbolki_fp_filters': 'QFN*6x6mm*P0.5mm*'}])
    newPart['name'].append('Interface_USB : USB2514B_Bi')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

