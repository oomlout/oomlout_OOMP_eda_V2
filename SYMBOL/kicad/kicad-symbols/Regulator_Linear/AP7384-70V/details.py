
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "AP7384-70V"
    hexID = "SZKREGULATORLINEARAP73847V"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'APE8865NL-12-HF-3', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AP7384-70V', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-92_Inline_Wide', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/AP7384.pdf', 'kicadSymbolki_keywords': '50mA LDO Regulator Fixed Positive', 'kicadSymbolki_description': '50mA Low Dropout Voltage Regulator, Fixed Output 7V, Wide Input Voltage Range 40V, TO-92', 'kicadSymbolki_fp_filters': 'TO?92*'}])
    newPart['name'].append('Regulator_Linear : AP7384-70V')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

