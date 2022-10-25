
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_Array"
    oIndex = "SN75468"
    hexID = "SZKTRANSISTORARRAYSN75468"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SN75468', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/slrs023e/slrs023e.pdf', 'kicadSymbolki_keywords': 'darlington transistor array', 'kicadSymbolki_description': 'Higher Voltage, High Current Darlington Transistor Arrays, 5V CMOS/TTL-compatible input, SOIC16/SOIC16W/DIP16', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x9.9mm*P1.27mm* SOIC*W*5.3x10.2mm*P1.27mm*'}])
    newPart['name'].append('Transistor_Array : SN75468')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

