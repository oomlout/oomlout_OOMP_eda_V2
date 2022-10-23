
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TNY288K"
    hexID = "SZKREGULATORSWITCHINGTNY288K"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TNY284K', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TNY288K', 'kicadSymbolFootprint': 'Package_SO:PowerIntegrations_eSOP-12B', 'kicadSymbolDatasheet': 'https://ac-dc.power.com/sites/default/files/product-docs/tinyswitch-4_family_datasheet.pdf', 'kicadSymbolki_keywords': 'Energy-Efficient, Off-Line Switcher With Line Compensated Overload Power', 'kicadSymbolki_description': 'TinySwitch-4 Family, 21.5W Output Power, eSOP-12B', 'kicadSymbolki_fp_filters': 'PowerIntegrations?eSOP?12B*'}])
    newPart['name'].append('TNY288K')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

