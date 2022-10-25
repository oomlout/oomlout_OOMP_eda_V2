
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator_Analog"
    oIndex = "ACPL-C87A"
    hexID = "SZKISOLATORANALOGACPLC87A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ACPL-C870', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ACPL-C87A', 'kicadSymbolFootprint': 'Package_SO:SSO-8_6.8x5.9mm_P1.27mm_Clearance8mm', 'kicadSymbolDatasheet': 'www.avagotech.com/docs/AV02-3563EN', 'kicadSymbolki_keywords': 'Optycally Isolated Voltage Sensor', 'kicadSymbolki_description': 'Precision Optycally Isolated Voltage Sensor, ±1% Gain Tolerance, Bandwidth 100kHz, SSO-8', 'kicadSymbolki_fp_filters': 'SSO*6.8x5.9mm*P1.27mm*Clearance8mm*'}])
    newPart['name'].append('Isolator_Analog : ACPL-C87A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

