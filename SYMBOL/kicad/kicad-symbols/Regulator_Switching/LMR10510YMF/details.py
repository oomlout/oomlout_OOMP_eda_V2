
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LMR10510YMF"
    hexID = "SZKREGULATORSWITCHINGLMR151YMF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LMR10510XMF', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LMR10510YMF', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lmr10510.pdf', 'kicadSymbolki_keywords': 'Miniature Step-Down Buck Voltage Regulator', 'kicadSymbolki_description': '1A, 5.5V Step-Down Voltage Regulator, 3MHz Frequency, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Regulator_Switching : LMR10510YMF')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

