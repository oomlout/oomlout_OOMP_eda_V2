
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "ESDA6V1-5SC6"
    hexID = "SZKPOWERPROTECTIONESDA6V15SC6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'ESDA6V1-5SC6', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-6', 'kicadSymbolDatasheet': 'www.st.com/resource/en/datasheet/esda6v1-5sc6.pdf', 'kicadSymbolki_keywords': 'ESD protection suppression transient', 'kicadSymbolki_description': 'Quintuple bidirectional transil, Suppressor for ESD protection, 6V1 Breakdown, SOT-23-6', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Power_Protection : ESDA6V1-5SC6')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

