
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "BF458"
    hexID = "SZKTRANSISTORBJTBF458"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BF457', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BF458', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-126-3_Vertical', 'kicadSymbolDatasheet': 'https://www.pcpaudio.com/pcpfiles/transistores/BF457-8-9.pdf', 'kicadSymbolki_keywords': 'NPN HV High Voltage Transistor', 'kicadSymbolki_description': '0.1A Ic, 250V Vce, High Voltage NPN Transistor, TO-126', 'kicadSymbolki_fp_filters': 'TO?126*'}])
    newPart['name'].append('Transistor_BJT : BF458')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

