
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Filter"
    oIndex = "BNX025"
    hexID = "SZKFILBNX25"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'FL', 'kicadSymbolValue': 'BNX025', 'kicadSymbolFootprint': 'Filter:Filter_Murata_BNX025', 'kicadSymbolDatasheet': 'https://www.murata.com/en-us/products/productdetail.aspx?cate=luNoiseSupprFilteBlockType&partno=BNX025H01%23', 'kicadSymbolki_keywords': 'EMI Filter SMD Murata', 'kicadSymbolki_description': 'EMI Filter SMD, Murata BNX025', 'kicadSymbolki_fp_filters': 'Filter*Murata*BNX025*'}])
    newPart['name'].append('Filter : BNX025')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

