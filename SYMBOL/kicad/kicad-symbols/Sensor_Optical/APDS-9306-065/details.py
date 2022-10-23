
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "APDS-9306-065"
    hexID = "SZKSENOPTICALAPDS93665"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'APDS-9306-065', 'kicadSymbolFootprint': 'OptoDevice:Broadcom_DFN-6_2x2mm_P0.65mm', 'kicadSymbolDatasheet': 'https://docs.broadcom.com/docs/AV02-4755EN', 'kicadSymbolki_keywords': 'opto ambient light sensor', 'kicadSymbolki_description': 'Ambient Light Sensor, I2C interface, 1.7-3.6V, DFN-6', 'kicadSymbolki_fp_filters': 'Broadcom*DFN*2x2mm*P0.65mm*'}])
    newPart['name'].append('APDS-9306-065')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

