
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "CPU_NXP_IMX"
    oIndex = "MCIMX6QP4AVT"
    hexID = "SZKCPUNXPIMXMCIMX6QP4AVT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCIMX6QP5EYM', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCIMX6QP4AVT', 'kicadSymbolFootprint': 'Package_BGA:BGA-624_21.0x21.0mm_Layout25x25_P0.8mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/IMX6DQPAEC.pdf', 'kicadSymbolki_keywords': 'Quad-Core ARM Cortex A9 SOC Automotive', 'kicadSymbolki_description': 'i.MX 6QuadPlus Automotive and Infotainment Application Processor, BGA-624', 'kicadSymbolki_fp_filters': 'BGA*21.0x21.0mm*P0.8mm*'}])
    newPart['name'].append('CPU_NXP_IMX : MCIMX6QP4AVT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

