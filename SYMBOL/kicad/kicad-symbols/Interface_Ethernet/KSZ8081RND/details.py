
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Ethernet"
    oIndex = "KSZ8081RND"
    hexID = "SZKINTERFACEETHERNETKSZ881RND"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'KSZ8081RNA', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'KSZ8081RND', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-24-1EP_4x4mm_P0.5mm_EP2.6x2.6mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/00002199A.pdf', 'kicadSymbolki_keywords': 'ETH PHY RMII', 'kicadSymbolki_description': '10BASE-T/100BASE-TX PHY with RMII Support, 50 MHz input clock, QFN-24', 'kicadSymbolki_fp_filters': 'QFN*1EP*4x4mm*P0.5mm*'}])
    newPart['name'].append('Interface_Ethernet : KSZ8081RND')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

