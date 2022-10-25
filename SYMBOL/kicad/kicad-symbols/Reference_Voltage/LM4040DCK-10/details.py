
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "LM4040DCK-10"
    hexID = "SZKREFERENCEVOLTAGELM44DCK1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM4040DCK-2.0', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM4040DCK-10', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-353_SC-70-5', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm4040-n.pdf', 'kicadSymbolki_keywords': 'diode device voltage reference shunt', 'kicadSymbolki_description': '10.0V Precision Micropower Shunt Voltage Reference, SC-70', 'kicadSymbolki_fp_filters': 'SOT?353*'}])
    newPart['name'].append('Reference_Voltage : LM4040DCK-10')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

