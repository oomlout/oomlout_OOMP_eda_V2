
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Ethernet"
    oIndex = "LAN9514"
    hexID = "SZKINTERFACEETHERNETLAN9514"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LAN9514', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-64-1EP_9x9mm_P0.5mm_EP7.3x7.3mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/00002306A.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'USB HUB Ethernet 10/100', 'kicadSymbolki_description': 'Four USB 2.0 hub with an integrated 10/100 Ethernet controller (0°C to +70°C), QFN-48', 'kicadSymbolki_fp_filters': 'QFN*1EP?9x9mm?P0.5mm?EP7.3x7.3mm*'}])
    newPart['name'].append('Interface_Ethernet : LAN9514')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

