
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "ExpressCard"
    hexID = "SZKCNEXPRESSCARD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'ExpressCard', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://web.archive.org/web/20180809060653/http://www.usb.org/developers/expresscard/EC_specifications/ExpressCard_2_0_FINAL.pdf', 'kicadSymbolki_keywords': 'expresscard pci express', 'kicadSymbolki_description': 'ExpressCard connector', 'kicadSymbolki_fp_filters': 'ExpressCard*'}])
    newPart['name'].append('ExpressCard')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

