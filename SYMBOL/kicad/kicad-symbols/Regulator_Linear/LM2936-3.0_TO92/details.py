
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LM2936-3.0_TO92"
    hexID = "SZKREGULATORLINEARLM29363TO92"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MC78L05_TO92', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM2936-3.0_TO92', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-92_Inline', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm2936.pdf', 'kicadSymbolki_keywords': 'linear regulator ldo fixed positive', 'kicadSymbolki_description': '50mA Ultra-Low Quiescent Current LDO Voltage Regulator, 3.0V fixed output, TO-92', 'kicadSymbolki_fp_filters': 'TO?92*'}])
    newPart['name'].append('Regulator_Linear : LM2936-3.0_TO92')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

