
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "IFX25401TBV50"
    hexID = "SZKREGULATORLINEARIFX2541TBV5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IFX25401TBV50', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-5_TabPin3', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-IFX25401-DS-v01_02-en.pdf?fileId=db3a304320d39d590120f62a690569f7', 'kicadSymbolki_keywords': 'fixed ldo positive voltage regulator', 'kicadSymbolki_description': 'Fixed 5V LDO Linear Voltage Regulator (TO-263-5)', 'kicadSymbolki_fp_filters': 'TO?263*TabPin3*'}])
    newPart['name'].append('IFX25401TBV50')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

