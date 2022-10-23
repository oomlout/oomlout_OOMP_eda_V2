
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TOP209G"
    hexID = "SZKREGULATORSWITCHINGTOP29G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TOP209G', 'kicadSymbolFootprint': 'Package_DIP:PowerIntegrations_SMD-8', 'kicadSymbolDatasheet': 'http://www.powerint.com/sites/default/files/product-docs/top209210.pdf', 'kicadSymbolki_keywords': 'Three-terminal Off-line PWM Switch', 'kicadSymbolki_description': 'TOPSwitch Family, 2W Max Output Power, SMD-8', 'kicadSymbolki_fp_filters': 'PowerIntegrations?SMD?8*'}])
    newPart['name'].append('TOP209G')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

