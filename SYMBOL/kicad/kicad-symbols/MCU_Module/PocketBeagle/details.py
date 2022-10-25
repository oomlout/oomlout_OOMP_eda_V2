
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Module"
    oIndex = "PocketBeagle"
    hexID = "SZKMCUMOPOCKETBEAGLE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PocketBeagle', 'kicadSymbolFootprint': 'Module:BeagleBoard_PocketBeagle', 'kicadSymbolDatasheet': 'https://github.com/beagleboard/pocketbeagle/wiki/System-Reference-Manual', 'kicadSymbolki_keywords': 'beagleboard pocketbeagle', 'kicadSymbolki_description': 'Singleboard computer with ARM Cortex-A8 1GHz, 512MB RAM', 'kicadSymbolki_fp_filters': 'BeagleBoard*PocketBeagle*'}])
    newPart['name'].append('MCU_Module : PocketBeagle')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

