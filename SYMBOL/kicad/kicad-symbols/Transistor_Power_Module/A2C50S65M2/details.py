
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_Power_Module"
    oIndex = "A2C50S65M2"
    hexID = "SZKTRANSISTORPOWERMOA2C5S65M2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'A2C25S12M3', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'A2C50S65M2', 'kicadSymbolFootprint': 'Transistor_Power_Module:ST_ACEPACK-2-CIB', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/a2c50s65m2.pdf', 'kicadSymbolki_keywords': 'IGBT Power Module Trench Field Stop Technology M series', 'kicadSymbolki_description': '50A, 650V, 20kHz, 208W x 6 , 3-phase, Freewheeling Diode, Brake Chopper, Diode Rectifier, 5k NTC, ACEPACK-2-CIB', 'kicadSymbolki_fp_filters': 'ST*ACEPACK*2*CIB*'}])
    newPart['name'].append('A2C50S65M2')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

