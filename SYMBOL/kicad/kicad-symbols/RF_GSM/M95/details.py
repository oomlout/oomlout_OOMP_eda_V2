
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_GSM"
    oIndex = "M95"
    hexID = "SZKGSMM95"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'M95', 'kicadSymbolFootprint': 'RF_GSM:Quectel_M95', 'kicadSymbolDatasheet': 'https://www.quectel.com/UploadImage/Downlad/M95_Hardware_Design_V1.3.pdf', 'kicadSymbolki_keywords': 'GSM GPRS AT SMS voice TCP/IP', 'kicadSymbolki_description': 'Quectel quad-band GSM/GPRS module in LCC package', 'kicadSymbolki_fp_filters': 'Quectel*M95*'}])
    newPart['name'].append('RF_GSM : M95')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

