
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "LP3947"
    hexID = "SZKBATMANAGEMENTLP3947"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LP3947', 'kicadSymbolFootprint': 'Package_SON:WSON-14-1EP_4.0x4.0mm_P0.5mm_EP2.6x2.6mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lp3947.pdf', 'kicadSymbolki_keywords': 'li-ion battery charger usb', 'kicadSymbolki_description': 'Single Cell Li-Ion LDO Battery Charger IC, Up to 1A, Support USB charging scheme', 'kicadSymbolki_fp_filters': 'WSON*4.0x4.0mm*P0.5mm*'}])
    newPart['name'].append('LP3947')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

