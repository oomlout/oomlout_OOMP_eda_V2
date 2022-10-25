
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LNK419EG"
    hexID = "SZKREGULATORSWITCHINGLNK419EG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LNK403EG', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LNK419EG', 'kicadSymbolFootprint': 'Package_SIP:PowerIntegrations_eSIP-7C', 'kicadSymbolDatasheet': 'http://www.powerint.com/sites/default/files/product-docs/linkswitch-ph_family_datasheet.pdf', 'kicadSymbolki_keywords': 'LED Driver IC, Single-Stage PFC and Primary-Side Constant Current Control', 'kicadSymbolki_description': 'LinkSwitch-PH Family, 50W Output Power, eSIP-7C', 'kicadSymbolki_fp_filters': 'PowerIntegrations?eSIP?7C*'}])
    newPart['name'].append('Regulator_Switching : LNK419EG')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

