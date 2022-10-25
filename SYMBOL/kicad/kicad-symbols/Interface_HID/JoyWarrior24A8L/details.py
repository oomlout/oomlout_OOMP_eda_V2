
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_HID"
    oIndex = "JoyWarrior24A8L"
    hexID = "SZKINTERFACEHIDJOYWARRIOR24A8L"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'JoyWarrior24A10L', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'JoyWarrior24A8L', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://codemercs.com/downloads/joywarrior/JW_Datasheet.pdf', 'kicadSymbolki_keywords': 'joystick controller, 8 bit, 4 axis', 'kicadSymbolki_description': 'JoyWarrior 8bit, 4 axis, joystick controller, DIP-24/SOIC-24', 'kicadSymbolki_fp_filters': 'SOIC*7.5x15.4mm*P1.27mm* DIP*7.62mm*'}])
    newPart['name'].append('Interface_HID : JoyWarrior24A8L')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

