
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transformer"
    oIndex = "CST2010_Split"
    hexID = "SZKTRCST21SPLIT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'T', 'kicadSymbolValue': 'CST2010_Split', 'kicadSymbolFootprint': 'Transformer_SMD:Transformer_Coilcraft_CST2010', 'kicadSymbolDatasheet': 'https://www.coilcraft.com/pdfs/cst2010.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'current sense transformer', 'kicadSymbolki_description': 'Coilcraft Current Sense Transformer, SMD, 40A, 1:20 to 1:200', 'kicadSymbolki_fp_filters': 'Transformer*Coilcraft*CST2010*'}])
    newPart['name'].append('Transformer : CST2010_Split')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

