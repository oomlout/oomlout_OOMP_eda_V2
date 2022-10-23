
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "ZEN132V230A16LS"
    hexID = "SZKPOWERPROTECTIONZEN132V23A16LS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ZEN056V130A24LS', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'ZEN132V230A16LS', 'kicadSymbolFootprint': 'Diode_SMD:Littelfuse_PolyZen-LS', 'kicadSymbolDatasheet': 'http://m.littelfuse.com/~/media/electronics/datasheets/polyzen_devices/littelfuse_polyzen_standard_polyzen_catalog_datasheet.pdf.pdf', 'kicadSymbolki_keywords': 'Polymer zener', 'kicadSymbolki_description': 'Polymer Protected Zener Diode, 13.2V, 2.30A, 16V, LS', 'kicadSymbolki_fp_filters': 'Littelfuse*PolyZen*LS*'}])
    newPart['name'].append('ZEN132V230A16LS')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

