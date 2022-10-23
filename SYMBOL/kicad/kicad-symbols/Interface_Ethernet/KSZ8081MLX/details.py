
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Ethernet"
    oIndex = "KSZ8081MLX"
    hexID = "SZKINTERFACEETHERNETKSZ881MLX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'KSZ8081MLX', 'kicadSymbolFootprint': 'Package_QFP:LQFP-48_7x7mm_P0.5mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/KSZ8081MLX.pdf', 'kicadSymbolki_keywords': 'ETH PHY RMII MII', 'kicadSymbolki_description': '10BASE-T/100BASE-TX PHY with RMII Support, 25 MHz input clock, LQFP-48', 'kicadSymbolki_fp_filters': 'LQFP?48*7x7mm*P0.5mm*'}])
    newPart['name'].append('KSZ8081MLX')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

