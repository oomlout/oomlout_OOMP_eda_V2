
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Touch"
    oIndex = "PCF8883"
    hexID = "SZKSENTOUCHPCF8883"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PCF8883', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.nxp.com/docs/en/data-sheet/PCF8883.pdf', 'kicadSymbolki_keywords': 'NXP capacitive touch sensor auto-calibration', 'kicadSymbolki_description': 'Capacitive touch/proximity switch with auto-calibration, SOIC-8/WLCSP-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* NXP*WLCSP*PCF8883*'}])
    newPart['name'].append('Sensor_Touch : PCF8883')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

