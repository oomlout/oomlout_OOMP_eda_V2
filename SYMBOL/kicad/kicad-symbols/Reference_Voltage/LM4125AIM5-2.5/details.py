
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "LM4125AIM5-2.5"
    hexID = "SZKREFERENCEVOLTAGELM4125AIM525"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM4125AIM5-2.5', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm4125.pdf', 'kicadSymbolki_keywords': 'Precision Micropower Low Dropout Voltage Reference 2.5V', 'kicadSymbolki_description': '2.5V ±0.2% Precision Micropower Low Dropout Voltage Reference, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Reference_Voltage : LM4125AIM5-2.5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

