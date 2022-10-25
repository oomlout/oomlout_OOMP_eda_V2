
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "D_Schottky_KAK"
    hexID = "SZKDEVICEDSCHOTTKYKAK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'D_Schottky_KAK', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'diode Schottky SCHDPAK', 'kicadSymbolki_description': 'Schottky diode, cathode on pins 1 and 3', 'kicadSymbolki_fp_filters': 'TO-???* *_Diode_* *SingleDiode* D_*'}])
    newPart['name'].append('Device : D_Schottky_KAK')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

