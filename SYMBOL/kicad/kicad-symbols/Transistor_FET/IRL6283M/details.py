
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRL6283M"
    hexID = "SZKTRANSISTORFETIRL6283M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRL6283M', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_MD', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irl6283mpbf.pdf?fileId=5546d462533600a40153565fe9452573', 'kicadSymbolki_keywords': 'N-Channel HEXFET MOSFET IRFET', 'kicadSymbolki_description': '38A Id, 20V Vds, 0.75mOhm Rds, N-Channel HEXFET Power MOSFET, DirectFET MD', 'kicadSymbolki_fp_filters': 'DirectFET*MD*'}])
    newPart['name'].append('Transistor_FET : IRL6283M')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

