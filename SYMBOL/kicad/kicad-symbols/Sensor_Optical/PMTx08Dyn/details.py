
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "PMTx08Dyn"
    hexID = "SZKSENOPTICALPMTX8DYN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'PMT', 'kicadSymbolValue': 'PMTx08Dyn', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'PMT 8-stage', 'kicadSymbolki_description': '8-stage photomultiplier tube', 'kicadSymbolki_fp_filters': 'PMT*'}])
    newPart['name'].append('Sensor_Optical : PMTx08Dyn')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

