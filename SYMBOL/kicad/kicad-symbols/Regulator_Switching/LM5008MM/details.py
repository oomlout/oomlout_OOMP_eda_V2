
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM5008MM"
    hexID = "SZKREGULATORSWITCHINGLM58"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM5007MM', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM5008MM', 'kicadSymbolFootprint': 'Package_SO:MSOP-8_3x3mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm5008.pdf', 'kicadSymbolki_keywords': 'Step-Down Switching Regulator', 'kicadSymbolki_description': '500mA, High Voltage (100V) Step-Down Switching Regulator, Adjustable Output Voltage, MSOP-8', 'kicadSymbolki_fp_filters': 'MSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Regulator_Switching : LM5008MM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

