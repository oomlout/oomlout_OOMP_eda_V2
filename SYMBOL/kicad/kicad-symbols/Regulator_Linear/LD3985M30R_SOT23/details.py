
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LD3985M30R_SOT23"
    hexID = "SZKREGULATORLINEARLD3985M3RSOT23"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LD3985M122R_SOT23', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LD3985M30R_SOT23', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'http://www.st.com/internet/com/TECHNICAL_RESOURCES/TECHNICAL_LITERATURE/DATASHEET/CD00003395.pdf', 'kicadSymbolki_keywords': '150mA LDO Regulator Fixed Positive', 'kicadSymbolki_description': '150mA Low Dropout Voltage Regulator, Fixed Output 3.0V, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Regulator_Linear : LD3985M30R_SOT23')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

