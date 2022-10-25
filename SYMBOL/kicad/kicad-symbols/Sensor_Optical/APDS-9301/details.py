
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "APDS-9301"
    hexID = "SZKSENOPTICALAPDS931"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'APDS-9301', 'kicadSymbolFootprint': 'OptoDevice:Broadcom_APDS-9301', 'kicadSymbolDatasheet': 'https://docs.broadcom.com/docs/AV02-2315EN', 'kicadSymbolki_keywords': 'ambient light sensor i2c', 'kicadSymbolki_description': 'ambient light sensor, i2c interface, 2.7-3.6V', 'kicadSymbolki_fp_filters': 'Broadcom*APDS*9301*'}])
    newPart['name'].append('Sensor_Optical : APDS-9301')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

