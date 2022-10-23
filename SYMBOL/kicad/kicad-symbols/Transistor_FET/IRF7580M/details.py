
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF7580M"
    hexID = "SZKTRANSISTORFETIRF758M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IRF60DM206', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF7580M', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_ME', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irf7580mpbf.pdf?fileId=5546d462533600a401535603855c1c72', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '114A Id, 60V Vds, 3.6mOhm Rds, N-Channel MOSFET, DirectFET ME', 'kicadSymbolki_fp_filters': 'DirectFET*ME*'}])
    newPart['name'].append('IRF7580M')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

