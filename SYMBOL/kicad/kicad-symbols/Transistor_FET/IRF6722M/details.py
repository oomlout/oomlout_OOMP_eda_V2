
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF6722M"
    hexID = "SZKTRANSISTORFETIRF6722M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BSB104N08NP3', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF6722M', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_MP', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irf6722mpbf.pdf?fileId=5546d462533600a4015355ed3c661a8e', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '13A Id, 30V Vds, 7.7mOhm Rds, N-Channel MOSFET, DirectFET MP', 'kicadSymbolki_fp_filters': 'DirectFET*MP*'}])
    newPart['name'].append('IRF6722M')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

