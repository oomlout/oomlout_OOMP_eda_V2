
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "AP7384-70SA"
    hexID = "SZKREGULATORLINEARAP73847SA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'APE8865NR-12-HF-3', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AP7384-70SA', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/AP7384.pdf', 'kicadSymbolki_keywords': '50mA LDO Regulator Fixed Positive', 'kicadSymbolki_description': '50mA Low Dropout Voltage Regulator, Fixed Output 7V, Wide Input Voltage Range 40V, SOT-23', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('AP7384-70SA')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

