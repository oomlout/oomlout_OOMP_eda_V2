
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM2731YMF"
    hexID = "SZKREGULATORSWITCHINGLM2731YMF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LMR10510XMF', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM2731YMF', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm2731.pdf', 'kicadSymbolki_keywords': 'Miniature Step-Up Boost Voltage Regulator', 'kicadSymbolki_description': 'LM27313, 1.8A, 22Vout Boost Voltage Regulator, 600KHz Frequency,', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Regulator_Switching : LM2731YMF')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

