
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LD3985G27R_TSOT23"
    hexID = "SZKREGULATORLINEARLD3985G27RTSOT23"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LD3985G122R_TSOT23', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LD3985G27R_TSOT23', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TSOT-23-5', 'kicadSymbolDatasheet': 'http://www.st.com/internet/com/TECHNICAL_RESOURCES/TECHNICAL_LITERATURE/DATASHEET/CD00003395.pdf', 'kicadSymbolki_keywords': '150mA LDO Regulator Fixed Positive', 'kicadSymbolki_description': '150mA Low Dropout Voltage Regulator, Fixed Output 2.7V, TSOT-23-5', 'kicadSymbolki_fp_filters': 'TSOT?23*'}])
    newPart['name'].append('Regulator_Linear : LD3985G27R_TSOT23')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

