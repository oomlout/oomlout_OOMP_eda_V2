
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRFI4020H"
    hexID = "SZKTRANSISTORFETIRFI42H"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IRFI4019H', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRFI4020H', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220F-5_P3.4x2.06mm_StaggerEven_Lead1.86mm_Vertical', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irfi4020h-117p.pdf?fileId=5546d462533600a401535623e7271f73', 'kicadSymbolki_keywords': 'Dual N-Channel MOSFET Half-Bridge', 'kicadSymbolki_description': '9.1A Id, 200V Vds, 80mOhm Rds, Dual Half Bridge N-Channel MOSFET, TO-220-5', 'kicadSymbolki_fp_filters': 'TO?220F*P3.4x2.06mm*StaggerEven*Lead1.86mm*'}])
    newPart['name'].append('Transistor_FET : IRFI4020H')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

