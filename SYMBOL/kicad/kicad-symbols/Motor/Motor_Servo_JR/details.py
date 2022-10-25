
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Motor"
    oIndex = "Motor_Servo_JR"
    hexID = "SZKMOTORMOTORSERVOJR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'Motor_Servo', 'kicadSymbolReference': 'M', 'kicadSymbolValue': 'Motor_Servo_JR', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://forums.parallax.com/uploads/attachments/46831/74481.png', 'kicadSymbolki_keywords': 'Servo Motor', 'kicadSymbolki_description': 'Servo Motor (JR connector)', 'kicadSymbolki_fp_filters': 'PinHeader*P2.54mm*'}])
    newPart['name'].append('Motor : Motor_Servo_JR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

