
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRFI4212H"
    hexID = "SZKTRANSISTORFETIRFI4212H"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IRFI4019H', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRFI4212H', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220F-5_P3.4x2.06mm_StaggerEven_Lead1.86mm_Vertical', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irfi4212h-117p.pdf?fileId=5546d462533600a401535623fc841f7a', 'kicadSymbolki_keywords': 'Dual N-Channel MOSFET Half-Bridge', 'kicadSymbolki_description': '11A Id, 100V Vds, 58mOhm Rds, Dual Half Bridge N-Channel MOSFET, TO-220-5', 'kicadSymbolki_fp_filters': 'TO?220F*P3.4x2.06mm*StaggerEven*Lead1.86mm*'}])
    newPart['name'].append('Transistor_FET : IRFI4212H')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

