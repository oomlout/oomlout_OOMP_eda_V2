
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Magnetic"
    oIndex = "AH1806-P"
    hexID = "SZKSENMAGNETICAH186P"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AH1806-P', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/AH1806.pdf', 'kicadSymbolki_keywords': 'hall switch', 'kicadSymbolki_description': 'High Sensitivity Micropower Omnipolar Hall-Effect Switch, SIP-3', 'kicadSymbolki_fp_filters': 'Diodes*SIP*4.1x1.5mm*P1.27mm* Diodes*SIP*4.1x1.5mm*P2.65mm*'}])
    newPart['name'].append('Sensor_Magnetic : AH1806-P')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

