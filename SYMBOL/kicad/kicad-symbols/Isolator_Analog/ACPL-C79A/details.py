
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator_Analog"
    oIndex = "ACPL-C79A"
    hexID = "SZKISOLATORANALOGACPLC79A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ACPL-C790', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ACPL-C79A', 'kicadSymbolFootprint': 'Package_SO:SSO-8_6.8x5.9mm_P1.27mm_Clearance8mm', 'kicadSymbolDatasheet': 'http://docs.avagotech.com/docs/AV02-2460EN', 'kicadSymbolki_keywords': 'Isolation Amplifer', 'kicadSymbolki_description': 'Precision Isolation Amplifer, ±1% Gain Tolerance, Bandwidth 200kHz, SSO-8', 'kicadSymbolki_fp_filters': 'SSO*6.8x5.9mm*P1.27mm*Clearance8mm*'}])
    newPart['name'].append('ACPL-C79A')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

