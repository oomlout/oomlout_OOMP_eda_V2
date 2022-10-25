
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Filter"
    oIndex = "Choke_Schaffner_RN102-1.5-02-1M6"
    hexID = "SZKFILCHOKESCHAFFNERRN121521M6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'Choke_Schaffner_RN102-0.3-02-22M', 'kicadSymbolReference': 'FL', 'kicadSymbolValue': 'Choke_Schaffner_RN102-1.5-02-1M6', 'kicadSymbolFootprint': 'Inductor_THT:Choke_Schaffner_RN102-04-14.0x14.0mm', 'kicadSymbolDatasheet': 'https://www.schaffner.com/products/download/product/datasheet/rn-series-common-mode-chokes-new/', 'kicadSymbolki_keywords': 'common-mode common mode choke powerline power line filter', 'kicadSymbolki_description': 'Common mode choke, 1.5A, 300VAC, 1.6mH, 94mohm, RN-102', 'kicadSymbolki_fp_filters': 'Choke*Schaffner*RN102*'}])
    newPart['name'].append('Filter : Choke_Schaffner_RN102-1.5-02-1M6')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

