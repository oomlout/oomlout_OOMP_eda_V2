
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Motor"
    oIndex = "Motor_Servo_Hitec"
    hexID = "SZKMOTORMOTORSERVOHITEC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'Motor_Servo', 'kicadSymbolReference': 'M', 'kicadSymbolValue': 'Motor_Servo_Hitec', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://forums.parallax.com/uploads/attachments/46831/74481.png', 'kicadSymbolki_keywords': 'Servo Motor', 'kicadSymbolki_description': 'Servo Motor (HiTec connector)', 'kicadSymbolki_fp_filters': 'PinHeader*P2.54mm*'}])
    newPart['name'].append('Motor_Servo_Hitec')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

