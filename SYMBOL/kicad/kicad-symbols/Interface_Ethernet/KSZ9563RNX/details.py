
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Ethernet"
    oIndex = "KSZ9563RNX"
    hexID = "SZKINTERFACEETHERNETKSZ9563RNX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'KSZ9563RNX', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-64-1EP_8x8mm_P0.4mm_EP6.5x6.5mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/KSZ9563R-Data-Sheet-DS00002419C.pdf', 'kicadSymbolki_keywords': 'Gigabit Ethernet Switch RGMII MII RMII ieee1588v2', 'kicadSymbolki_description': '3-Port Gigabit Ethernet Switch with RGMII/MII/RMII Interface and IEEE 1588v2, QFN-64', 'kicadSymbolki_fp_filters': 'QFN*1EP*8x8mm*P0.4mm*'}])
    newPart['name'].append('KSZ9563RNX')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

