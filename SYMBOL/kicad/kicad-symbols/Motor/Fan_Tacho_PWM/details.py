
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Motor"
    oIndex = "Fan_Tacho_PWM"
    hexID = "SZKMOTORFANTACHOPWM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'M', 'kicadSymbolValue': 'Fan_Tacho_PWM', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.formfactors.org/developer%5Cspecs%5Crev1_2_public.pdf', 'kicadSymbolki_keywords': 'Fan Motor tacho PWM', 'kicadSymbolki_description': 'Fan, tacho output, PWM input, 4-pin connector', 'kicadSymbolki_fp_filters': 'FanPinHeader*P2.54mm*Vertical* PinHeader*P2.54mm*Vertical* TerminalBlock*'}])
    newPart['name'].append('Motor : Fan_Tacho_PWM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

