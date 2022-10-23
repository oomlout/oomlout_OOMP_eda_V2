
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF7759L2"
    hexID = "SZKTRANSISTORFETIRF7759L2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IRF7739L1', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF7759L2', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_L8', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irf7759l2pbf.pdf?fileId=5546d462533600a40153560478171cb0', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '160A Id, 75V Vds, 2.3mOhm Rds, N-Channel MOSFET, DirectFET L8', 'kicadSymbolki_fp_filters': 'DirectFET*L8*'}])
    newPart['name'].append('IRF7759L2')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

