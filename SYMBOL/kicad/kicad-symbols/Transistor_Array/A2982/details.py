
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_Array"
    oIndex = "A2982"
    hexID = "SZKTRANSISTORARRAYA2982"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'A2982', 'kicadSymbolFootprint': 'Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.allegromicro.com/~/media/Files/Datasheets/A2981-2-Datasheet.ashx', 'kicadSymbolki_keywords': 'relays solenoids lamps steppers servos LEDs', 'kicadSymbolki_description': '8-Channel Source Driver, TTL DTL, PMOS or CMOS compatible, 500mA 50V output, SOIC-20W', 'kicadSymbolki_fp_filters': 'SOIC*20W*7.5x12.8mm*P1.27mm*'}])
    newPart['name'].append('A2982')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

