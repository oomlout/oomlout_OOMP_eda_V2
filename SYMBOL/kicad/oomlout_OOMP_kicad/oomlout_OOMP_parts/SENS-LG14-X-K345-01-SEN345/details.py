
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "SENS-LG14-X-K345-01-SEN345"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSSENSLG14XK3451SEN345"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SENS-LG14-X-K345-01-SEN345', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:SENS-LG14-X-K345-01-SEN345', 'kicadSymbolDatasheet': 'oom.lt/SEN345', 'kicadSymbolki_keywords': '3-axis accelerometer i2c spi mems', 'kicadSymbolki_description': 'hexID: SEN345;3-Axis MEMS Accelerometer, 2/4/8/16g range, I2C/SPI, LGA-14', 'kicadSymbolki_fp_filters': '*LGA*3x5mm*P0.8mm*'}])
    newPart['name'].append('oomlout_OOMP_parts : SENS-LG14-X-K345-01-SEN345')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

