
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "BSB028N06NN3"
    hexID = "SZKTRANSISTORFETBSB28N6NN3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BSB028N06NN3', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_MN', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-BSB028N06NN3-DS-v02_00-en.pdf?fileId=db3a30432e25b009012e29fda4e23838', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '90A Id, 60V Vds, 2.8mOhm Rds, N-Channel MOSFET, DirectFET MN', 'kicadSymbolki_fp_filters': 'DirectFET*MN*'}])
    newPart['name'].append('BSB028N06NN3')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

