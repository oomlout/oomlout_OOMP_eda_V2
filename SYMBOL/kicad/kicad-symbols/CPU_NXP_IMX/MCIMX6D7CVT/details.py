
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "CPU_NXP_IMX"
    oIndex = "MCIMX6D7CVT"
    hexID = "SZKCPUNXPIMXMCIMX6D7CVT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCIMX6QP7CVT', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCIMX6D7CVT', 'kicadSymbolFootprint': 'Package_BGA:BGA-624_21.0x21.0mm_Layout25x25_P0.8mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/IMX6DQIEC.pdf', 'kicadSymbolki_keywords': 'Dual-Core ARM Cortex A9 SOC Industrial', 'kicadSymbolki_description': 'i.MX 6Dual Application Processor for Industrial Products, BGA-624', 'kicadSymbolki_fp_filters': 'BGA*21.0x21.0mm*P0.8mm*'}])
    newPart['name'].append('CPU_NXP_IMX : MCIMX6D7CVT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

