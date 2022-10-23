
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "FSL136MRT"
    hexID = "SZKREGULATORSWITCHINGFSL136MRT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FSL136MRT', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:Fairchild_TO-220F-6L', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/FSL136MRT-D.pdf', 'kicadSymbolki_keywords': 'SMPS Controller 50W AC-DC', 'kicadSymbolki_description': '67kHz SMPS Controller w/ Soft Start, max. 50W AC-DC, TO-220F-6L', 'kicadSymbolki_fp_filters': 'Fairchild*TO*220F*6L*'}])
    newPart['name'].append('FSL136MRT')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

