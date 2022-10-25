
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "D_Laser_1A3C"
    hexID = "SZKDEVICEDLASER1A3C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'LD', 'kicadSymbolValue': 'D_Laser_1A3C', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'opto laserdiode', 'kicadSymbolki_description': 'Laser diode, cathode on pin 3, anode on pin 1', 'kicadSymbolki_fp_filters': '*LaserDiode*'}])
    newPart['name'].append('Device : D_Laser_1A3C')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

