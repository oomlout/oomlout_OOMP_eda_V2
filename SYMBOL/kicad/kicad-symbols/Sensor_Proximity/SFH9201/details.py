
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Proximity"
    oIndex = "SFH9201"
    hexID = "SZKSENPROXIMITYSFH921"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SFH9206', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SFH9201', 'kicadSymbolFootprint': 'OptoDevice:Osram_SFH9x0x', 'kicadSymbolDatasheet': 'https://media.digikey.com/pdf/Data%20Sheets/Osram%20PDFs/SFH_9201.pdf', 'kicadSymbolki_keywords': 'Reflective Opto Interrupter Coupler', 'kicadSymbolki_description': 'Reflective Opto Interrupter/Coupler, SMD-6', 'kicadSymbolki_fp_filters': 'Osram*SFH9x0x*'}])
    newPart['name'].append('Sensor_Proximity : SFH9201')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

