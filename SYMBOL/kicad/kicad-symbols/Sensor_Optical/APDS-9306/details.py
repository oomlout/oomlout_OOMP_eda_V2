
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "APDS-9306"
    hexID = "SZKSENOPTICALAPDS936"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'APDS-9306', 'kicadSymbolFootprint': 'OptoDevice:Broadcom_LGA-8_2x2mm_P0.53mm', 'kicadSymbolDatasheet': 'https://docs.broadcom.com/docs/AV02-4755EN', 'kicadSymbolki_keywords': 'opto ambient light sensor', 'kicadSymbolki_description': 'Ambient Light Sensor, I2C interface, 1.7-3.6V, LGA-8', 'kicadSymbolki_fp_filters': 'Broadcom*LGA*2x2mm*P0.53mm*'}])
    newPart['name'].append('Sensor_Optical : APDS-9306')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

