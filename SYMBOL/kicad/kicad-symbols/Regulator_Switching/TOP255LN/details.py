
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TOP255LN"
    hexID = "SZKREGULATORSWITCHINGTOP255LN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TOP255LN', 'kicadSymbolFootprint': 'Package_SIP:PowerIntegrations_eSIP-7F', 'kicadSymbolDatasheet': 'https://ac-dc.power.com/sites/default/files/product-docs/topswitch-hx_family_datasheet.pdf', 'kicadSymbolki_keywords': 'Eco Smart Off-Line Switcher, Extendend Power Range', 'kicadSymbolki_description': 'TOPSwitch-HX Family, 57W Output Power', 'kicadSymbolki_fp_filters': 'PowerIntegrations?eSIP?7F*'}])
    newPart['name'].append('TOP255LN')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

