
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "IFX25401TEV50"
    hexID = "SZKREGULATORLINEARIFX2541TEV5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IFX25401TEV50', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-252-4', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-IFX25401-DS-v01_02-en.pdf?fileId=db3a304320d39d590120f62a690569f7', 'kicadSymbolki_keywords': 'fixed ldo positive voltage regulator', 'kicadSymbolki_description': 'Fixed 5V LDO Linear Voltage Regulator (TO-252-4)', 'kicadSymbolki_fp_filters': 'TO*252*'}])
    newPart['name'].append('IFX25401TEV50')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

