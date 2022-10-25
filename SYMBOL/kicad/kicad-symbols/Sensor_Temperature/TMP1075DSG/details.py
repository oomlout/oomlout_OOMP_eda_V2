
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Temperature"
    oIndex = "TMP1075DSG"
    hexID = "SZKSENTEMPERATURETMP175DSG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TMP1075DSG', 'kicadSymbolFootprint': 'Package_SON:WSON-8-1EP_2x2mm_P0.5mm_EP0.9x1.6mm_ThermalVias', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/gpn/tmp1075', 'kicadSymbolki_keywords': 'temperature sensor I2C single channel', 'kicadSymbolki_description': 'I2C-bus digital temperature sensor and thermal watchdog, WSON-8', 'kicadSymbolki_fp_filters': 'WSON*1EP*2x2mm*P0.5mm*'}])
    newPart['name'].append('Sensor_Temperature : TMP1075DSG')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

