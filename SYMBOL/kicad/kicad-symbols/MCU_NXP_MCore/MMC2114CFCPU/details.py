
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_MCore"
    oIndex = "MMC2114CFCPU"
    hexID = "SZKMCUNXPMCOREC2114CFCPU"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MMC2114CFCPU', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'motorola/mmc2114.pdf', 'kicadSymbolki_description': 'Motorola M*CORE  upro 100 pins'}])
    newPart['name'].append('MCU_NXP_MCore : MMC2114CFCPU')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

