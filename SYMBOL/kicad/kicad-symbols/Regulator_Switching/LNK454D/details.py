
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LNK454D"
    hexID = "SZKREGULATORSWITCHINGLNK454D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LNK454D', 'kicadSymbolFootprint': 'Package_SO:PowerIntegrations_SO-8C', 'kicadSymbolDatasheet': 'http://www.powerint.com/sites/default/files/product-docs/linkswitch-pl_family_datasheet.pdf', 'kicadSymbolki_keywords': 'LED Driver IC with TRIAC Dimming, Single-Stage PFC and Constant Current Control for Non-Isolated Applications', 'kicadSymbolki_description': 'LinkSwitch-PL Family, 3W Output Power, SO-8C', 'kicadSymbolki_fp_filters': 'PowerIntegrations?SO?8C*'}])
    newPart['name'].append('Regulator_Switching : LNK454D')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

