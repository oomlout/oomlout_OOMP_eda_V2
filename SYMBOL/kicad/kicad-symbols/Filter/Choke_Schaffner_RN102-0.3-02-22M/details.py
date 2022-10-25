
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Filter"
    oIndex = "Choke_Schaffner_RN102-0.3-02-22M"
    hexID = "SZKFILCHOKESCHAFFNERRN123222M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'FL', 'kicadSymbolValue': 'Choke_Schaffner_RN102-0.3-02-22M', 'kicadSymbolFootprint': 'Inductor_THT:Choke_Schaffner_RN102-04-14.0x14.0mm', 'kicadSymbolDatasheet': 'https://www.schaffner.com/products/download/product/datasheet/rn-series-common-mode-chokes-new/', 'kicadSymbolki_keywords': 'common-mode common mode choke powerline power line filter', 'kicadSymbolki_description': 'Common mode choke, 300mA, 300VAC, 22mH, 1.3 ohm, RN-102', 'kicadSymbolki_fp_filters': 'Choke*Schaffner*RN102*'}])
    newPart['name'].append('Filter : Choke_Schaffner_RN102-0.3-02-22M')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

