
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF8301M"
    hexID = "SZKTRANSISTORFETIRF831M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IRF6613', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF8301M', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_MT', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irf8301mpbf.pdf?fileId=5546d462533600a40153560d0e7a1d58', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '34A Id, 30V Vds, 1.5mOhm Rds, N-Channel MOSFET, DirectFET MT', 'kicadSymbolki_fp_filters': 'DirectFET*MT*'}])
    newPart['name'].append('IRF8301M')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

