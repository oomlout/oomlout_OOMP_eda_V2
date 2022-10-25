
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF4905"
    hexID = "SZKTRANSISTORFETIRF495"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IRF9540N', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF4905', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-3_Vertical', 'kicadSymbolDatasheet': 'http://www.infineon.com/dgdl/irf4905.pdf?fileId=5546d462533600a4015355e32165197c', 'kicadSymbolki_keywords': 'Single P-Channel HEXFET Power MOSFET', 'kicadSymbolki_description': '-74A Id, -55V Vds, Single P-Channel HEXFET Power MOSFET, 20mOhm Ron, TO-220AB', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('Transistor_FET : IRF4905')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

