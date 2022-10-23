
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_Array"
    oIndex = "TBD62783A"
    hexID = "SZKTRANSISTORARRAYTBD62783A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TBD62783A', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://toshiba.semicon-storage.com/info/docget.jsp?did=30523&prodName=TBD62783APG', 'kicadSymbolki_keywords': 'relays solenoids lamps steppers servos LEDs', 'kicadSymbolki_description': '8-Channel Source Type Transistor Array, TTL and CMOS compatible, 500mA, 50V, DIP-18/SOP-18/SSOP-18/SOIC-18W', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOP*7.0x12.5mm*P1.27mm* SSOP*4.4x6.5mm*P0.65mm* SOIC*7.5x11.6mm*P1.27mm*'}])
    newPart['name'].append('TBD62783A')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

