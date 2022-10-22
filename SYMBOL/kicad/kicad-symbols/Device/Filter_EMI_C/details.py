
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "Filter_EMI_C"
    hexID = "SZKDEVICEFILEMIC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'C_Feedthrough', 'kicadSymbolReference': 'C', 'kicadSymbolValue': 'Filter_EMI_C', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.murata.com/~/media/webrenewal/support/library/catalog/products/emc/emifil/c31e.ashx?la=en-gb', 'kicadSymbolki_keywords': 'EMI filter feedthrough capacitor', 'kicadSymbolki_description': 'EMI filter, single capacitor'}])
    newPart['name'].append('Filter_EMI_C')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

