
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LK112M18TR"
    hexID = "SZKREGULATORLINEARLK112M18TR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LK112M15TR', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LK112M18TR', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'https://www.st.com/resource/ja/datasheet/lk112.pdf', 'kicadSymbolki_keywords': 'LDO regulator voltage', 'kicadSymbolki_description': 'Low noise and low drop voltage regulator with shutdown function, 150mA, Vout = 1.8V, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Regulator_Linear : LK112M18TR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

