
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Pressure"
    oIndex = "MPXH6115A"
    hexID = "SZKSENPRESSUREMPXH6115A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MPXA6115A', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MPXH6115A', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.nxp.com/files/sensors/doc/data_sheet/MPXA6115A.pdf', 'kicadSymbolki_keywords': 'absolute pressure sensor', 'kicadSymbolki_description': 'Absolute pressure sensor, 15 to 115kPa, analog output, integrated signal conditioning, temperature compensated, SSO package'}])
    newPart['name'].append('Sensor_Pressure : MPXH6115A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

