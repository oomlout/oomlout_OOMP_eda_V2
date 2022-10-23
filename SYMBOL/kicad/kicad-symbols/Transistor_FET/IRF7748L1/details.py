
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF7748L1"
    hexID = "SZKTRANSISTORFETIRF7748L1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IRF6718L2', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF7748L1', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_L6', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irf7748l1pbf.pdf?fileId=5546d462533600a40153560434c11c9e', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '104A Id, 60V Vds, 2.2mOhm Rds, N-Channel MOSFET, DirectFET L6', 'kicadSymbolki_fp_filters': 'DirectFET*L6*'}])
    newPart['name'].append('IRF7748L1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

