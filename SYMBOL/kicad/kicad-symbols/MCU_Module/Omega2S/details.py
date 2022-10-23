
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Module"
    oIndex = "Omega2S"
    hexID = "SZKMCUMOOMEGA2S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'Omega2S', 'kicadSymbolFootprint': 'Module:Onion_Omega2S', 'kicadSymbolDatasheet': 'https://github.com/OnionIoT/Omega2/raw/master/Documents/Omega2S%20Datasheet.pdf', 'kicadSymbolki_keywords': 'onion omega module', 'kicadSymbolki_description': 'Iot Computer Module by Onion, 64MB RAM, 16MB FLASH', 'kicadSymbolki_fp_filters': 'Onion*Omega2S*'}])
    newPart['name'].append('Omega2S')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

