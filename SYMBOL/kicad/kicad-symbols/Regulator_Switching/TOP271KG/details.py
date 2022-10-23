
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TOP271KG"
    hexID = "SZKREGULATORSWITCHINGTOP271KG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TOP264KG', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TOP271KG', 'kicadSymbolFootprint': 'Package_SO:PowerIntegrations_eSOP-12B', 'kicadSymbolDatasheet': 'https://ac-dc.power.com/sites/default/files/product-docs/topswitch-jx_family_datasheet.pdf', 'kicadSymbolki_keywords': 'Integrated Off-Line Switcher with EcoSmart™ Technology', 'kicadSymbolki_description': 'TOPSwitch-JX Family, 66W Output Power, eSOP-12B', 'kicadSymbolki_fp_filters': 'PowerIntegrations?eSOP?12B*'}])
    newPart['name'].append('TOP271KG')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

