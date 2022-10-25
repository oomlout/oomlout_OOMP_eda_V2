
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "A4403GEU"
    hexID = "SZKREGULATORSWITCHINGA443GEU"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'A4403GEU', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-16-1EP_4x4mm_P0.65mm_EP2.7x2.7mm', 'kicadSymbolDatasheet': 'https://www.allegromicro.com/~/media/Files/Datasheets/A4403-Datasheet.ashx', 'kicadSymbolki_keywords': 'buck regulator adjustable', 'kicadSymbolki_description': 'Valley current mode buck converter, 46V, 3A, up to 2MHz, QFN-16', 'kicadSymbolki_fp_filters': 'QFN*1EP*4x4mm*P0.65mm*EP2.7x2.7mm*'}])
    newPart['name'].append('Regulator_Switching : A4403GEU')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

