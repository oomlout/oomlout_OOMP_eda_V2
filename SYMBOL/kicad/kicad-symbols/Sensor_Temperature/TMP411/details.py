
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Temperature"
    oIndex = "TMP411"
    hexID = "SZKSENTEMPERATURETMP411"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TMP411', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com.cn/cn/lit/ds/symlink/tmp411.pdf', 'kicadSymbolki_keywords': 'Temperature sensor remote local i2c', 'kicadSymbolki_description': '- Remote and Local TEMPERATURE SENSOR', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* VSSOP*3.0x3.0mm*P0.65mm*'}])
    newPart['name'].append('Sensor_Temperature : TMP411')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

