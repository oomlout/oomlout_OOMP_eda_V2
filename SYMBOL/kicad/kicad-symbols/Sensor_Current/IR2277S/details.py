
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "IR2277S"
    hexID = "SZKSENCURRENTIR2277S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IR2177S', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IR2277S', 'kicadSymbolFootprint': 'Package_SO:SOIC-16W_7.5x10.3mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/ir2177s.pdf?fileId=5546d462533600a4015355c92e7416cb', 'kicadSymbolki_keywords': 'half bridge current sense', 'kicadSymbolki_description': 'Phase Current Sensor IC for AC Motor Control, PWM and ADC output, 1200V, SOIC-16W', 'kicadSymbolki_fp_filters': 'SOIC*W*7.5x10.3mm*P1.27mm*'}])
    newPart['name'].append('Sensor_Current : IR2277S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

