
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator_Analog"
    oIndex = "ACPL-C87B"
    hexID = "SZKISOLATORANALOGACPLC87B"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ACPL-C870', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ACPL-C87B', 'kicadSymbolFootprint': 'Package_SO:SSO-8_6.8x5.9mm_P1.27mm_Clearance8mm', 'kicadSymbolDatasheet': 'www.avagotech.com/docs/AV02-3563EN', 'kicadSymbolki_keywords': 'Optycally Isolated Voltage Sensor', 'kicadSymbolki_description': 'Precision Optycally Isolated Voltage Sensor, ±0.5% Gain Tolerance, Bandwidth 100kHz, SSO-8', 'kicadSymbolki_fp_filters': 'SSO*6.8x5.9mm*P1.27mm*Clearance8mm*'}])
    newPart['name'].append('ACPL-C87B')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

