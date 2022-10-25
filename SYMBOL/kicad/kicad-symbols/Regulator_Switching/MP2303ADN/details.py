
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "MP2303ADN"
    hexID = "SZKREGULATORSWITCHINGMP233ADN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MP2303ADN', 'kicadSymbolFootprint': 'Package_SO:SOIC-8-1EP_3.9x4.9mm_P1.27mm_EP2.62x3.51mm', 'kicadSymbolDatasheet': 'https://www.monolithicpower.com/pub/media/document/MP2303A_r1.1.pdf', 'kicadSymbolki_keywords': 'buck converter step down', 'kicadSymbolki_description': 'Synchronous Rectified 3A, 28V, 360kHz Step-Down Converter, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*1EP*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Regulator_Switching : MP2303ADN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

