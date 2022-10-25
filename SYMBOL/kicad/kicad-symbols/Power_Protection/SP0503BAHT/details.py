
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "SP0503BAHT"
    hexID = "SZKPOWERPROTECTIONSP53BAHT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'SP0503BAHT', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-143', 'kicadSymbolDatasheet': 'http://www.littelfuse.com/~/media/files/littelfuse/technical%20resources/documents/data%20sheets/sp05xxba.pdf', 'kicadSymbolki_keywords': 'usb esd protection suppression transient', 'kicadSymbolki_description': 'TVS Diode Array, 5.5V Standoff, 3 Channels, SOT-143 package', 'kicadSymbolki_fp_filters': 'SOT?143*'}])
    newPart['name'].append('Power_Protection : SP0503BAHT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

