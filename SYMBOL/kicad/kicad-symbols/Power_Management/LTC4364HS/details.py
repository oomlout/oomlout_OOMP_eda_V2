
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "LTC4364HS"
    hexID = "SZKPOWERMANAGEMENTLTC4364HS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LTC4364CS', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC4364HS', 'kicadSymbolFootprint': 'Package_SO:SOIC-16_3.9x9.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/436412f.pdf', 'kicadSymbolki_keywords': 'surge overvoltage undervoltage reverse-polarity protection diode ORing MOSFET driver', 'kicadSymbolki_description': 'Surge stopper with ideal diode, UV and OV protection -40V to +80V in SOIC-16 package, -40°C to +125°C', 'kicadSymbolki_fp_filters': 'SOIC*3.9x9.9mm*P1.27mm*'}])
    newPart['name'].append('Power_Management : LTC4364HS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

