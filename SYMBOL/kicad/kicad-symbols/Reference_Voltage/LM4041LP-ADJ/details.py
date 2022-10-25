
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "LM4041LP-ADJ"
    hexID = "SZKREFERENCEVOLTAGELM441LPADJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM4041LP-ADJ', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-92_Inline', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm4041-n.pdf', 'kicadSymbolki_keywords': 'diode device voltage reference shunt', 'kicadSymbolki_description': 'Adjustable Precision Micropower Shunt Voltage Reference, TO-92', 'kicadSymbolki_fp_filters': 'TO?92*'}])
    newPart['name'].append('Reference_Voltage : LM4041LP-ADJ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

