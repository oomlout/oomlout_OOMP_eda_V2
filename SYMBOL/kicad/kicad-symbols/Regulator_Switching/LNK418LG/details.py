
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LNK418LG"
    hexID = "SZKREGULATORSWITCHINGLNK418LG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LNK403LG', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LNK418LG', 'kicadSymbolFootprint': 'Package_SIP:PowerIntegrations_eSIP-7F', 'kicadSymbolDatasheet': 'http://www.powerint.com/sites/default/files/product-docs/linkswitch-ph_family_datasheet.pdf', 'kicadSymbolki_keywords': 'LED Driver IC, Single-Stage PFC and Primary-Side Constant Current Control', 'kicadSymbolki_description': 'LinkSwitch-PH Family, 35W Output Power, eSIP-7F', 'kicadSymbolki_fp_filters': 'PowerIntegrations?eSIP?7F*'}])
    newPart['name'].append('Regulator_Switching : LNK418LG')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

