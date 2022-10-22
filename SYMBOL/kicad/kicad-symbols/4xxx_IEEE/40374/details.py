
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "4xxx_IEEE"
    oIndex = "40374"
    hexID = "SZK4XXXIEEE4374"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '40374', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.digchip.com/datasheets/download_datasheet.php?id=369790&part-number=HEF40374BDB', 'kicadSymbolki_keywords': 'CMOS BUFFER 3State', 'kicadSymbolki_description': '8-bit D-flip-flop with 3-State outputs'}])
    newPart['name'].append('40374')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

