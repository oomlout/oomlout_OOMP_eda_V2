
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "L6563A"
    hexID = "SZKREGULATORCONTROLLERL6563A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'L6563', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'L6563A', 'kicadSymbolFootprint': 'Package_SO:SOIC-14_3.9x8.7mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.st.com/resource/en/datasheet/l6563.pdf', 'kicadSymbolki_keywords': 'SMPS pfc controller', 'kicadSymbolki_description': 'Advanced Transition-Mode PFC Controller, SOIC-14', 'kicadSymbolki_fp_filters': 'SOIC*3.9x8.7mm*P1.27mm*'}])
    newPart['name'].append('Regulator_Controller : L6563A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

