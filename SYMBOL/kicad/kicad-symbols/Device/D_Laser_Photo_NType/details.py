
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "D_Laser_Photo_NType"
    hexID = "SZKDEVICEDLASERPHOTONTYPE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'LD', 'kicadSymbolValue': 'D_Laser_Photo_NType', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.egismos.disonhu.com/laser/diode-package.htm', 'kicadSymbolki_keywords': 'opto laserdiode photodiode', 'kicadSymbolki_description': 'Laser diode with photodiode, center on pin 2, LD cathode on pin 1', 'kicadSymbolki_fp_filters': '*LaserDiode*'}])
    newPart['name'].append('Device : D_Laser_Photo_NType')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

