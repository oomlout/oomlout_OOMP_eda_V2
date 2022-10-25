
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Motor"
    oIndex = "SLA7042M"
    hexID = "SZKDRIVERMOTORSLA742M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SLA7044M', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SLA7042M', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'www.sumzi.com/upload/files/2007/07/2007073114282034189.PDF', 'kicadSymbolki_keywords': 'Stepper driver', 'kicadSymbolki_description': 'Unipolar PWM high-current motor driver', 'kicadSymbolki_fp_filters': 'SLA704XM'}])
    newPart['name'].append('Driver_Motor : SLA7042M')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

