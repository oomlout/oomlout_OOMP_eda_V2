
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "USB_C_Plug"
    hexID = "SZKCNUCPLUG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'P', 'kicadSymbolValue': 'USB_C_Plug', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.usb.org/sites/default/files/documents/usb_type-c.zip', 'kicadSymbolki_keywords': 'usb universal serial bus', 'kicadSymbolki_description': 'USB Type-C Plug connector', 'kicadSymbolki_fp_filters': 'USB*C*Plug*'}])
    newPart['name'].append('USB_C_Plug')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

