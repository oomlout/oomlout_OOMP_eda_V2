
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "NUF4401MN"
    hexID = "SZKPOWERPROTECTIONNUF441MN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NUF4401MN', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8-1EP_2x2mm_P0.5mm_EP0.7x1.3mm', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/NUF4401MN-D.PDF', 'kicadSymbolki_keywords': 'EMI, ESD protection', 'kicadSymbolki_description': '4 channel EMI filters with integrated ESD protection, DFN-8', 'kicadSymbolki_fp_filters': 'DFN*1EP*2x2mm*P0.5mm*'}])
    newPart['name'].append('Power_Protection : NUF4401MN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

