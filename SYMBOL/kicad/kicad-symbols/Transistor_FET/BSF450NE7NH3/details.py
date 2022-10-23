
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "BSF450NE7NH3"
    hexID = "SZKTRANSISTORFETBSF45NE7NH3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BSF450NE7NH3', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_ST', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-BSF450NE7NH3-DS-v02_02-EN.pdf?fileId=db3a30433a047ba0013a687e2ae403da', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '15A Id, 75V Vds, 45mOhm Rds, N-Channel MOSFET, DirectFET ST', 'kicadSymbolki_fp_filters': 'DirectFET*ST*'}])
    newPart['name'].append('BSF450NE7NH3')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

