
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM2733XMF"
    hexID = "SZKREGULATORSWITCHINGLM2733XMF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LMR10510XMF', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM2733XMF', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm2733.pdf', 'kicadSymbolki_keywords': 'Miniature Step-Up Boost Voltage Regulator', 'kicadSymbolki_description': 'LM27313, 1A, 40Vout Boost Voltage Regulator, 1.6MHz Frequency, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Regulator_Switching : LM2733XMF')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

