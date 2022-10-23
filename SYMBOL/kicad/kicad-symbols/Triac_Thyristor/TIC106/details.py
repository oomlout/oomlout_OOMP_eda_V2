
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Triac_Thyristor"
    oIndex = "TIC106"
    hexID = "SZKTRIACTHYRISTORTIC16"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'TIC106', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-3_Vertical', 'kicadSymbolDatasheet': 'http://pdf.datasheetcatalog.com/datasheet/PowerInnovations/mXyzrtvs.pdf', 'kicadSymbolki_keywords': 'thyristor', 'kicadSymbolki_description': '5A Ion, 400-800V Voff, Silicon Controlled Rectifier (Thyristor), TO-220', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('TIC106')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

