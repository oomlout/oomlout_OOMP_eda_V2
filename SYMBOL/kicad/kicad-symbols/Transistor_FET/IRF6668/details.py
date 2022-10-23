
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF6668"
    hexID = "SZKTRANSISTORFETIRF6668"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BSB028N06NN3', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF6668', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_MN', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irf6668pbf.pdf?fileId=5546d462533600a4015355ec96b91a64', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '55A Id, 80V Vds, 15mOhm Rds, N-Channel MOSFET, DirectFET MN', 'kicadSymbolki_fp_filters': 'DirectFET*MN*'}])
    newPart['name'].append('IRF6668')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

