
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Temperature"
    oIndex = "TMP1075D"
    hexID = "SZKSENTEMPERATURETMP175D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TMP1075D', 'kicadSymbolFootprint': 'Package_SO:SO-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/gpn/tmp1075', 'kicadSymbolki_keywords': 'temperature sensor I2C single channel', 'kicadSymbolki_description': 'I2C-bus digital temperature sensor and thermal watchdog, SO-8', 'kicadSymbolki_fp_filters': 'SO*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Sensor_Temperature : TMP1075D')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

