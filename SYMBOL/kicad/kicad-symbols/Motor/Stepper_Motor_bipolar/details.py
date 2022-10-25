
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Motor"
    oIndex = "Stepper_Motor_bipolar"
    hexID = "SZKMOTORSTEPPERMOTORBIPOLAR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'M', 'kicadSymbolValue': 'Stepper_Motor_bipolar', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.infineon.com/dgdl/Application-Note-TLE8110EE_driving_UniPolarStepperMotor_V1.1.pdf?fileId=db3a30431be39b97011be5d0aa0a00b0', 'kicadSymbolki_keywords': 'bipolar stepper motor', 'kicadSymbolki_description': '4-wire bipolar stepper motor', 'kicadSymbolki_fp_filters': 'PinHeader*P2.54mm*Vertical* TerminalBlock* Motor*'}])
    newPart['name'].append('Motor : Stepper_Motor_bipolar')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

