
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_GSM"
    oIndex = "BC95"
    hexID = "SZKGSMBC95"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BC95', 'kicadSymbolFootprint': 'RF_GSM:Quectel_BC95', 'kicadSymbolDatasheet': 'https://www.quectel.com/UploadImage/Downlad/Quectel_BC95_Hardware_Design_V1.3.pdf', 'kicadSymbolki_keywords': 'NB-IoT GSM GPRS Quad-Band SMS', 'kicadSymbolki_description': 'NB-IoT, GSM Quad-Band Communication Module, GPRS, Audio Engine, AT Command Set', 'kicadSymbolki_fp_filters': 'Quectel?BC95*'}])
    newPart['name'].append('RF_GSM : BC95')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

