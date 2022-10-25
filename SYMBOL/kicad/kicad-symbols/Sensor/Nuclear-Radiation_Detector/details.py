
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor"
    oIndex = "Nuclear-Radiation_Detector"
    hexID = "SZKSENNUCLEARRADIATIONDETECTOR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'V', 'kicadSymbolValue': 'Nuclear-Radiation_Detector', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'nuclear ionising radiation sensor geiger mueller muller tube neutron counter ionization chamber', 'kicadSymbolki_description': 'Generic radiation detector'}])
    newPart['name'].append('Sensor : Nuclear-Radiation_Detector')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

