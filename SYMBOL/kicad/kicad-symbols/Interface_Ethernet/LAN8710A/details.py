
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Ethernet"
    oIndex = "LAN8710A"
    hexID = "SZKINTERFACEETHERNETLAN871A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LAN8710A', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-32-1EP_5x5mm_P0.5mm_EP3.3x3.3mm_ThermalVias', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/8710a.pdf', 'kicadSymbolki_keywords': 'ETH PHY MII RMII', 'kicadSymbolki_description': 'LAN8710 Ethernet PHY with MII/RMII interface, QFN-32', 'kicadSymbolki_fp_filters': 'QFN*1EP*5x5mm*P0.5mm*'}])
    newPart['name'].append('Interface_Ethernet : LAN8710A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

