
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRL6297SD"
    hexID = "SZKTRANSISTORFETIRL6297SD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IRF6802SD', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRL6297SD', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_SA', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irl6297sdpbf.pdf?fileId=5546d462533600a40153565ff22f2575', 'kicadSymbolki_keywords': 'Dual N-Channel HEXFET MOSFET Logic-Level', 'kicadSymbolki_description': '15A Id, 20V Vds, 4.9mOhm Rds, Dual N-Channel HEXFET Power MOSFET, DirectFET SA', 'kicadSymbolki_fp_filters': 'DirectFET*SA*'}])
    newPart['name'].append('IRL6297SD')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

