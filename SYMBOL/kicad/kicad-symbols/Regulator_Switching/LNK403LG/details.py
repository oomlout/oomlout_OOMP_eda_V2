
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LNK403LG"
    hexID = "SZKREGULATORSWITCHINGLNK43LG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LNK403LG', 'kicadSymbolFootprint': 'Package_SIP:PowerIntegrations_eSIP-7F', 'kicadSymbolDatasheet': 'http://www.powerint.com/sites/default/files/product-docs/linkswitch-ph_family_datasheet.pdf', 'kicadSymbolki_keywords': 'LED Driver IC with TRIAC Dimming, Single-Stage PFC and Primary-Side Constant Current Control', 'kicadSymbolki_description': 'LinkSwitch-PH Family, 12W Output Power, eSIP-7F', 'kicadSymbolki_fp_filters': 'PowerIntegrations?eSIP?7F*'}])
    newPart['name'].append('Regulator_Switching : LNK403LG')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

