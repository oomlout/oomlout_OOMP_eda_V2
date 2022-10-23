
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LNK625DG"
    hexID = "SZKREGULATORSWITCHINGLNK625DG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LNK623DG', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LNK625DG', 'kicadSymbolFootprint': 'Package_SO:PowerIntegrations_SO-8C', 'kicadSymbolDatasheet': 'http://www.powerint.com/sites/default/files/product-docs/linkcv_family_datasheet.pdf', 'kicadSymbolki_keywords': 'Energy-Efficient, Off-line Switcher with Accurate Primary-side Constant-Voltage Control', 'kicadSymbolki_description': 'LinkSwitch-CV Family, 8W Output Power, SO-8C', 'kicadSymbolki_fp_filters': 'PowerIntegrations?SO?8C*'}])
    newPart['name'].append('LNK625DG')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

