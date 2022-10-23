
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_HID"
    oIndex = "SpinWarrior24R4"
    hexID = "SZKINTERFACEHIDSPINWARRIOR24R4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SpinWarrior24R4', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.codemercs.com/downloads/spinwarrior/SW_Datasheet.pdf', 'kicadSymbolki_keywords': '8bit, relative position, USB, rotary encoder', 'kicadSymbolki_description': 'SpinWarrior, 4 8bit relative position rotary encoders, 7 switches, DIP-24/SOIC-24', 'kicadSymbolki_fp_filters': 'DIP*7.62mm* SOIC*7.5x15.4mm*P1.27mm*'}])
    newPart['name'].append('SpinWarrior24R4')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

