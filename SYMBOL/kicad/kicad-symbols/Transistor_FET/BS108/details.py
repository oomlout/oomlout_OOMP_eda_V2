
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "BS108"
    hexID = "SZKTRANSISTORFETBS18"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BS107', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BS108', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-92_Inline', 'kicadSymbolDatasheet': 'http://www.redrok.com/MOSFET_BS108_200V_250mA_8O_Vth1.5_TO-92.PDF', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '0.25A Id, 200V Vds, N-Channel MOSFET, TO-92', 'kicadSymbolki_fp_filters': 'TO?92*'}])
    newPart['name'].append('Transistor_FET : BS108')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

