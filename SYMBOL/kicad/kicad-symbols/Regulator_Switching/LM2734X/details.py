
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM2734X"
    hexID = "SZKREGULATORSWITCHINGLM2734X"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM2734Y', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM2734X', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TSOT-23-6', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm2734.pdf', 'kicadSymbolki_keywords': 'Miniature Step-Down Buck Voltage Regulator', 'kicadSymbolki_description': '1A Step-Down DC-DC Regulator, Adjustable Output Voltage, 1.6MHz, TSOT-23-5', 'kicadSymbolki_fp_filters': 'TSOT?23*'}])
    newPart['name'].append('Regulator_Switching : LM2734X')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

