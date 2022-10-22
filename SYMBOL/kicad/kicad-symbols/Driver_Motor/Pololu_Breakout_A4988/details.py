
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Motor"
    oIndex = "Pololu_Breakout_A4988"
    hexID = "SZKDRIVERMOTORPOLOLUBREAKOUTA4988"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'A', 'kicadSymbolValue': 'Pololu_Breakout_A4988', 'kicadSymbolFootprint': 'Module:Pololu_Breakout-16_15.2x20.3mm', 'kicadSymbolDatasheet': 'https://www.pololu.com/product/2980/pictures', 'kicadSymbolki_keywords': 'Pololu Breakout Board Stepper Driver A4988', 'kicadSymbolki_description': 'Pololu Breakout Board, Stepper Driver A4988', 'kicadSymbolki_fp_filters': 'Pololu*Breakout*15.2x20.3mm*'}])
    newPart['name'].append('Pololu_Breakout_A4988')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

