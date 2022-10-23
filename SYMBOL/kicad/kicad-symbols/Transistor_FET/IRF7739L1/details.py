
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF7739L1"
    hexID = "SZKTRANSISTORFETIRF7739L1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF7739L1', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_L8', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irf7739l1pbf.pdf?fileId=5546d462533600a40153560423d91c9a', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '270A Id, 40V Vds, 1.0mOhm Rds, N-Channel MOSFET, DirectFET L8', 'kicadSymbolki_fp_filters': 'DirectFET*L8*'}])
    newPart['name'].append('IRF7739L1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

