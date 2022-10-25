
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "L6564"
    hexID = "SZKREGULATORCONTROLLERL6564"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'L6564', 'kicadSymbolFootprint': 'Package_SO:SSOP-10_3.9x4.9mm_P1.00mm', 'kicadSymbolDatasheet': 'http://www.st.com/resource/en/datasheet/l6564.pdf', 'kicadSymbolki_keywords': 'SMPS pfc controller', 'kicadSymbolki_description': '10-Pin Transition-Mode PFC Controller, SSOP-10', 'kicadSymbolki_fp_filters': 'SSOP*3.9x4.9mm*P1.00mm*'}])
    newPart['name'].append('Regulator_Controller : L6564')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

