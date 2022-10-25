
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "USB_C_Plug_USB2.0"
    hexID = "SZKCNUCPLUGU2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'P', 'kicadSymbolValue': 'USB_C_Plug_USB2.0', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.usb.org/sites/default/files/documents/usb_type-c.zip', 'kicadSymbolki_keywords': 'usb universal serial bus type-C USB2.0', 'kicadSymbolki_description': 'USB 2.0-only Type-C Plug connector', 'kicadSymbolki_fp_filters': 'USB*C*Plug*'}])
    newPart['name'].append('Connector : USB_C_Plug_USB2.0')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

