
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF6892S"
    hexID = "SZKTRANSISTORFETIRF6892S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF6892S', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_S3C', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irf6892spbf.pdf?fileId=5546d462533600a4015355f0bb961ab8', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '28A Id, 25V Vds, 1.7mOhm Rds, N-Channel MOSFET, DirectFET S3C', 'kicadSymbolki_fp_filters': 'DirectFET*S3C*'}])
    newPart['name'].append('IRF6892S')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

