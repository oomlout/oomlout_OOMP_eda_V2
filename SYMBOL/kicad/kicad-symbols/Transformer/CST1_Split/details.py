
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transformer"
    oIndex = "CST1_Split"
    hexID = "SZKTRCST1SPLIT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'T', 'kicadSymbolValue': 'CST1_Split', 'kicadSymbolFootprint': 'Transformer_SMD:Transformer_Coilcraft_CST1', 'kicadSymbolDatasheet': 'https://www.coilcraft.com/pdfs/cst.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'current sense transformer', 'kicadSymbolki_description': 'Coilcraft Current Sense Transformer, SMD, 20A, 1:20 to 1:125', 'kicadSymbolki_fp_filters': 'Transformer*Coilcraft*CST1*'}])
    newPart['name'].append('CST1_Split')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

