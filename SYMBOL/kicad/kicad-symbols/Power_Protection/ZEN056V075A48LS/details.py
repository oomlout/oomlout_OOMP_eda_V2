
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "ZEN056V075A48LS"
    hexID = "SZKPOWERPROTECTIONZEN56V75A48LS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ZEN056V130A24LS', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'ZEN056V075A48LS', 'kicadSymbolFootprint': 'Diode_SMD:Littelfuse_PolyZen-LS', 'kicadSymbolDatasheet': 'http://m.littelfuse.com/~/media/electronics/datasheets/polyzen_devices/littelfuse_polyzen_standard_polyzen_catalog_datasheet.pdf.pdf', 'kicadSymbolki_keywords': 'Polymer zener', 'kicadSymbolki_description': 'Polymer Protected Zener Diode, 5.6V, 0.75A, 48V, LS', 'kicadSymbolki_fp_filters': 'Littelfuse*PolyZen*LS*'}])
    newPart['name'].append('ZEN056V075A48LS')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

