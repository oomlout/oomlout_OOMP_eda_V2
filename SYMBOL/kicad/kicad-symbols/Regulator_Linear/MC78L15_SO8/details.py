
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "MC78L15_SO8"
    hexID = "SZKREGULATORLINEARMC78L15SO8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MC78L05_SO8', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MC78L15_SO8', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/MC78L00A-D.PDF', 'kicadSymbolki_keywords': 'Voltage Regulator 100mA Positive', 'kicadSymbolki_description': 'Positive 100mA 30V Linear Regulator, Fixed Output 15V, SO-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Regulator_Linear : MC78L15_SO8')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

