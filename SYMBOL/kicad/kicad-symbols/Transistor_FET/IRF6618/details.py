
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF6618"
    hexID = "SZKTRANSISTORFETIRF6618"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IRF6613', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF6618', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_MT', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irf6618pbf.pdf?fileId=5546d462533600a4015355e862c21a1b', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '170A Id, 30V Vds, 2.2mOhm Rds, N-Channel MOSFET, DirectFET MT', 'kicadSymbolki_fp_filters': 'DirectFET*MT*'}])
    newPart['name'].append('IRF6618')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

