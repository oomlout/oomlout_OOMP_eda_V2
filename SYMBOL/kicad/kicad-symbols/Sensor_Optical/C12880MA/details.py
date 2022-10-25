
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "C12880MA"
    hexID = "SZKSENOPTICALC1288MA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'C12880MA', 'kicadSymbolFootprint': 'OptoDevice:Hamamatsu_C12880', 'kicadSymbolDatasheet': 'http://www.hamamatsu.com/resources/pdf/ssd/c12880ma_kacc1226e.pdf', 'kicadSymbolki_keywords': 'spectrometer', 'kicadSymbolki_description': 'Micro spectrometer 340 to 850nm resolution 15nm', 'kicadSymbolki_fp_filters': 'Hamamatsu*C12880*'}])
    newPart['name'].append('Sensor_Optical : C12880MA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

