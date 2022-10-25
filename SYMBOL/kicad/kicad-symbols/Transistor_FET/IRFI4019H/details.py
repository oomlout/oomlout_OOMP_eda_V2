
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRFI4019H"
    hexID = "SZKTRANSISTORFETIRFI419H"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRFI4019H', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220F-5_P3.4x2.06mm_StaggerEven_Lead1.86mm_Vertical', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irfi4019h-117p.pdf?fileId=5546d462533600a401535623d74d1f6f', 'kicadSymbolki_keywords': 'Dual N-Channel MOSFET Half-Bridge', 'kicadSymbolki_description': '8.7A Id, 150V Vds, 80mOhm Rds, Dual Half Bridge N-Channel MOSFET, TO-220-5', 'kicadSymbolki_fp_filters': 'TO?220F*P3.4x2.06mm*StaggerEven*Lead1.86mm*'}])
    newPart['name'].append('Transistor_FET : IRFI4019H')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

