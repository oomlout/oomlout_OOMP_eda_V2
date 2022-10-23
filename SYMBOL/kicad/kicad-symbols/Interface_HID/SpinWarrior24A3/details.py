
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_HID"
    oIndex = "SpinWarrior24A3"
    hexID = "SZKINTERFACEHIDSPINWARRIOR24A3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SpinWarrior24A3', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.codemercs.com/downloads/spinwarrior/SW_Datasheet.pdf', 'kicadSymbolki_keywords': '16bit, absolute position, USB, rotary encoder', 'kicadSymbolki_description': 'SpinWarrior, 3 16bit absolute position rotary encoders, 6 digital inputs, DIP-24/SOIC-24', 'kicadSymbolki_fp_filters': 'DIP*7.62mm* SOIC*7.5x15.4mm*P1.27mm*'}])
    newPart['name'].append('SpinWarrior24A3')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

