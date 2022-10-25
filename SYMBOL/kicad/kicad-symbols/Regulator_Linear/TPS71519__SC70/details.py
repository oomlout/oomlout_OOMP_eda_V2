
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "TPS71519__SC70"
    hexID = "SZKREGULATORLINEARTPS71519SC7"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TPS71518__SC70', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS71519__SC70', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-353_SC-70-5', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps715.pdf', 'kicadSymbolki_keywords': 'LDO regulator voltage', 'kicadSymbolki_description': 'Low-drop Voltage Regulator, Io up to 50mA, Fixed Vo 1.9V, Ignd 3.2uA , SC70.', 'kicadSymbolki_fp_filters': '*SC?70*'}])
    newPart['name'].append('Regulator_Linear : TPS71519__SC70')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

