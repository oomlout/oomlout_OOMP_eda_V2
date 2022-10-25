
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Intel"
    oIndex = "IA188XLPLC68IR2"
    hexID = "SZKMCUINTELIA188XLPLC68IR2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '80C188', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IA188XLPLC68IR2', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.innovasic.com/upload/products/Innovasic_IA186XL_IA188XL_Data_Sheet_20110706_2.pdf', 'kicadSymbolki_keywords': 'MPRO', 'kicadSymbolki_description': 'MCU Replacement for Intel 80C188XL', 'kicadSymbolki_fp_filters': 'PLCC* PGA*Layout11x11*P2.54mm* LCC*'}])
    newPart['name'].append('MCU_Intel : IA188XLPLC68IR2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

