
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRLZ34N"
    hexID = "SZKTRANSISTORFETIRLZ34N"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BUZ11', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRLZ34N', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-3_Vertical', 'kicadSymbolDatasheet': 'http://www.infineon.com/dgdl/irlz34npbf.pdf?fileId=5546d462533600a40153567206892720', 'kicadSymbolki_keywords': 'N-Channel HEXFET MOSFET Logic-Level', 'kicadSymbolki_description': '30A Id, 55V Vds, 35mOhm Rds, N-Channel HEXFET Power MOSFET, TO-220AB', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('IRLZ34N')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

