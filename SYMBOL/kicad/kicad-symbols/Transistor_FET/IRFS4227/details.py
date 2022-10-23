
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRFS4227"
    hexID = "SZKTRANSISTORFETIRFS4227"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STB15N80K5', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRFS4227', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-2', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irfs4227pbf.pdf?fileId=5546d462533600a401535639ef64219b', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '130A Id, 200V Vds, 22mOhm Rds, N-Channel MOSFET, D2PAK', 'kicadSymbolki_fp_filters': 'TO?263*'}])
    newPart['name'].append('IRFS4227')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

