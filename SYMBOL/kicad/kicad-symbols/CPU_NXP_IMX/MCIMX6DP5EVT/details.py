
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "CPU_NXP_IMX"
    oIndex = "MCIMX6DP5EVT"
    hexID = "SZKCPUNXPIMXMCIMX6DP5EVT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCIMX6QP5EYM', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCIMX6DP5EVT', 'kicadSymbolFootprint': 'Package_BGA:BGA-624_21.0x21.0mm_Layout25x25_P0.8mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/IMX6DQPCEC.pdf', 'kicadSymbolki_keywords': 'Dual-Core ARM Cortex A9 SOC', 'kicadSymbolki_description': 'i.MX 6DualPlus Application Processor for Consumer Products, BGA-624', 'kicadSymbolki_fp_filters': 'BGA*21.0x21.0mm*P0.8mm*'}])
    newPart['name'].append('MCIMX6DP5EVT')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

