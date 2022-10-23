
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "AOZ1282CI-1"
    hexID = "SZKREGULATORSWITCHINGAOZ1282CI1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AOZ1280CI', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AOZ1282CI-1', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-6', 'kicadSymbolDatasheet': 'http://www.aosmd.com/res/data_sheets/AOZ1282CI-1.pdf', 'kicadSymbolki_keywords': 'switching buck converter', 'kicadSymbolki_description': '600 mA Simple Buck Regulator, 4.5-36V input, 1MHz', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('AOZ1282CI-1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

