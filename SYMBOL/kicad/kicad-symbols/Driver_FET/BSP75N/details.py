
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "BSP75N"
    hexID = "SZKDRIVERFETBSP75N"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BSP75N', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-223', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-BSP75N-DS-v01_04-en.pdf?fileId=db3a30431ed1d7b2011f471f5a0256d1', 'kicadSymbolki_keywords': 'MOSFET ESD Overcurrent', 'kicadSymbolki_description': 'Self-Protected Low Side Driver with Temperature and Current Limit, SOT−223', 'kicadSymbolki_fp_filters': 'SOT?223*'}])
    newPart['name'].append('BSP75N')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

