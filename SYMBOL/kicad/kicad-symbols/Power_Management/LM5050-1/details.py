
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "LM5050-1"
    hexID = "SZKPOWERMANAGEMENTLM551"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM5050-1', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TSOT-23-6', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm5050-1-q1.pdf', 'kicadSymbolki_keywords': 'positive high-side or-ing ideal-diode', 'kicadSymbolki_description': 'High side OR-ing FET controller, 5V to 75V operation, TSOT-23-6', 'kicadSymbolki_fp_filters': 'TSOT?23*'}])
    newPart['name'].append('Power_Management : LM5050-1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

