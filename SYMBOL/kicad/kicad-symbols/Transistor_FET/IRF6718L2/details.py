
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF6718L2"
    hexID = "SZKTRANSISTORFETIRF6718L2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF6718L2', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_L6', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irf6718l2pbf.pdf?fileId=5546d462533600a4015355ed25bd1a88', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '61A Id, 25V Vds, 0.7mOhm Rds, N-Channel MOSFET, DirectFET L6', 'kicadSymbolki_fp_filters': 'DirectFET*L6*'}])
    newPart['name'].append('IRF6718L2')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

