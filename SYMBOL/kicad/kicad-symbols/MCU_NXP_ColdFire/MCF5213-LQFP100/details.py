
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_ColdFire"
    oIndex = "MCF5213-LQFP100"
    hexID = "SZKMCUNXPCOLDFIREMCF5213LQFP1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCF5213-LQFP100', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '', 'kicadSymbolki_keywords': 'COLDFIRE', 'kicadSymbolki_description': 'Coldfire with SRAM and Flash Eprom - LQFP100 package'}])
    newPart['name'].append('MCU_NXP_ColdFire : MCF5213-LQFP100')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

