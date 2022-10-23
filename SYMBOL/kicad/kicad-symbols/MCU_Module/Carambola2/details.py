
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Module"
    oIndex = "Carambola2"
    hexID = "SZKMCUMOCARAMBOLA2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'Carambola2', 'kicadSymbolFootprint': 'Module:Carambola2', 'kicadSymbolDatasheet': 'https://www.8devices.com/media/products/carambola2/downloads/carambola2-datasheet.pdf', 'kicadSymbolki_keywords': 'carambola, 8devices, openwrt, board, wlan', 'kicadSymbolki_description': 'Qualcomm AR9331, 16MB Flash, 64MB RAM, USB, Serial, Ethernet, GPIO, OpenWRT, industrial SoM computer', 'kicadSymbolki_fp_filters': 'Carambola2*'}])
    newPart['name'].append('Carambola2')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

