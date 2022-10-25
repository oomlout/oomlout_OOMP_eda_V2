
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "LM4132xMF-2.5"
    hexID = "SZKREFERENCEVOLTAGELM4132XMF25"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM4132xMF-1.8', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM4132xMF-2.5', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm4132.pdf', 'kicadSymbolki_keywords': 'Precision Low Dropout Voltage Reference 2.5V', 'kicadSymbolki_description': 'Precision Low Dropout Voltage Reference, 2.5V, ±0.05% to ±0.5%, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Reference_Voltage : LM4132xMF-2.5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

