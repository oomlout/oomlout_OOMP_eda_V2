
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "PTN78000H_EUS-5"
    hexID = "SZKCONPTN78HEUS5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PTN78000W_EUS-5', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PTN78000H_EUS-5', 'kicadSymbolFootprint': 'Module:Texas_EUS_R-PDSS-T5_THT', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/ptn78000w.pdf', 'kicadSymbolki_keywords': 'texas dc-dc converter step down buck', 'kicadSymbolki_description': '1.5A non-isolated switching regulator power module, 7-36V input voltage, 11.85-22V output voltage, EUS-5', 'kicadSymbolki_fp_filters': 'Texas*EUS*R?PDSS?T5*'}])
    newPart['name'].append('PTN78000H_EUS-5')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

