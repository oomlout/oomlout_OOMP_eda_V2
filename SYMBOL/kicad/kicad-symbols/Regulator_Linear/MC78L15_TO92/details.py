
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "MC78L15_TO92"
    hexID = "SZKREGULATORLINEARMC78L15TO92"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MC78L05_TO92', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MC78L15_TO92', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-92_Inline', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/MC78L00A-D.PDF', 'kicadSymbolki_keywords': 'Voltage Regulator 100mA Positive', 'kicadSymbolki_description': 'Positive 100mA 30V Linear Regulator, Fixed Output 15V, TO-92', 'kicadSymbolki_fp_filters': 'TO?92*'}])
    newPart['name'].append('Regulator_Linear : MC78L15_TO92')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

