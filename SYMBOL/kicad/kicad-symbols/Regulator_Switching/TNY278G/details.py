
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TNY278G"
    hexID = "SZKREGULATORSWITCHINGTNY278G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TNY274G', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TNY278G', 'kicadSymbolFootprint': 'Package_DIP:PowerIntegrations_SMD-8C', 'kicadSymbolDatasheet': 'http://www.powerint.com/sites/default/files/product-docs/tny274-280.pdf', 'kicadSymbolki_keywords': 'Energy-Efficient, Off-Line Switcher With Enhanced Flexibility and Extended Power Range', 'kicadSymbolki_description': 'TinySwitch-III Family, 21.5W Output Power, SMD-8C', 'kicadSymbolki_fp_filters': 'PowerIntegrations?SMD?8C*'}])
    newPart['name'].append('TNY278G')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

