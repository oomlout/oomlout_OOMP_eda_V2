
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "AOZ1280CI"
    hexID = "SZKREGULATORSWITCHINGAOZ128CI"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AOZ1280CI', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-6', 'kicadSymbolDatasheet': 'http://aosmd.com/res/data_sheets/AOZ1280CI.pdf', 'kicadSymbolki_keywords': 'switching buck converter', 'kicadSymbolki_description': '1.2 A Simple Buck Regulator, 3-26V input, 1.5Mhz', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('AOZ1280CI')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

