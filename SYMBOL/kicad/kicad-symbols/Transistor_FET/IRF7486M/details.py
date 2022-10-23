
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF7486M"
    hexID = "SZKTRANSISTORFETIRF7486M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IRF60DM206', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF7486M', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_ME', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-IRL7486M-DS-v01_00-EN.pdf?fileId=5546d46258fc0bc10158fec7a83a0629', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '209A Id, 40V Vds, 1.25mOhm Rds, N-Channel MOSFET, DirectFET ME', 'kicadSymbolki_fp_filters': 'DirectFET*ME*'}])
    newPart['name'].append('IRF7486M')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

