
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "CP2104"
    hexID = "SZKINTERFACEUCP214"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CP2104', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-24-1EP_4x4mm_P0.5mm_EP2.6x2.6mm', 'kicadSymbolDatasheet': 'https://www.silabs.com/documents/public/data-sheets/cp2104.pdf', 'kicadSymbolki_keywords': 'uart usb bridge interface transceiver', 'kicadSymbolki_description': 'Single-Chip USB-to-UART Bridge, USB 2.0 Full-Speed, 2Mbps UART, QFN-24', 'kicadSymbolki_fp_filters': 'QFN*4x4mm*P0.5mm*'}])
    newPart['name'].append('Interface_USB : CP2104')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

