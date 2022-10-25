
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "L78L06_TO92"
    hexID = "SZKREGULATORLINEARL78L6TO92"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MC78L05_TO92', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'L78L06_TO92', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-92_Inline', 'kicadSymbolDatasheet': 'http://www.st.com/content/ccc/resource/technical/document/datasheet/15/55/e5/aa/23/5b/43/fd/CD00000446.pdf/files/CD00000446.pdf/jcr:content/translations/en.CD00000446.pdf', 'kicadSymbolki_keywords': 'Voltage Regulator 100mA Positive', 'kicadSymbolki_description': 'Positive 100mA 30V Linear Regulator, Fixed Output 6V, TO-92', 'kicadSymbolki_fp_filters': 'TO?92*'}])
    newPart['name'].append('Regulator_Linear : L78L06_TO92')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

