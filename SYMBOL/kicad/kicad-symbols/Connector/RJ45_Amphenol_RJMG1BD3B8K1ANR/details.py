
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "RJ45_Amphenol_RJMG1BD3B8K1ANR"
    hexID = "SZKCNRJ45AMPHENOLRJMG1BD3B8K1ANR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'RJ45_Amphenol_RJMG1BD3B8K1ANR', 'kicadSymbolFootprint': 'Connector_RJ:RJ45_Amphenol_RJMG1BD3B8K1ANR', 'kicadSymbolDatasheet': 'https://www.amphenolcanada.com/ProductSearch/Drawings/AC/RJMG1BD3B8K1ANR.PDF', 'kicadSymbolki_keywords': 'RJ45 Magjack', 'kicadSymbolki_description': '1 Port RJ45 Magjack Connector Through Hole 10/100 Base-T, AutoMDIX', 'kicadSymbolki_fp_filters': 'RJ45*Amphenol*RJMG1BD3B8K1ANR*'}])
    newPart['name'].append('RJ45_Amphenol_RJMG1BD3B8K1ANR')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

