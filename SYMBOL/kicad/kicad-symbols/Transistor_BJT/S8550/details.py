
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "S8550"
    hexID = "SZKTRANSISTORBJTS855"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'S8550', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-92_Inline', 'kicadSymbolDatasheet': 'http://www.unisonic.com.tw/datasheet/S8550.pdf', 'kicadSymbolki_keywords': 'S8550 PNP Low Voltage High Current Transistor', 'kicadSymbolki_description': '0.7A Ic, 20V Vce, Low Voltage High Current PNP Transistor, TO-92', 'kicadSymbolki_fp_filters': 'TO?92*'}])
    newPart['name'].append('Transistor_BJT : S8550')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

