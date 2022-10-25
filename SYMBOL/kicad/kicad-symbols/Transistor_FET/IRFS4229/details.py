
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRFS4229"
    hexID = "SZKTRANSISTORFETIRFS4229"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STB15N80K5', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRFS4229', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-2', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irfs4229pbf.pdf?fileId=5546d462533600a401535639fdc421a1', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '91A Id, 250V Vds, 42mOhm Rds, N-Channel MOSFET, D2PAK', 'kicadSymbolki_fp_filters': 'TO?263*'}])
    newPart['name'].append('Transistor_FET : IRFS4229')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

