
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Ethernet"
    oIndex = "LAN7500-ABJZ"
    hexID = "SZKINTERFACEETHERNETLAN75ABJZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LAN7500-ABJZ', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-56-1EP_8x8mm_P0.5mm_EP5.9x5.9mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/00001734B.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'USB Ethernet 10/100/1000', 'kicadSymbolki_description': 'Hi-Speed USB 2.0 to 10/100/1000 Ethernet Controller, QFN-56', 'kicadSymbolki_fp_filters': 'QFN*1EP*8x8mm*P0.5mm*'}])
    newPart['name'].append('Interface_Ethernet : LAN7500-ABJZ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

