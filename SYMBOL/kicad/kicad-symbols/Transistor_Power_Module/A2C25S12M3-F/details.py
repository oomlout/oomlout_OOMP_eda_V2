
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_Power_Module"
    oIndex = "A2C25S12M3-F"
    hexID = "SZKTRANSISTORPOWERMOA2C25S12M3F"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'A2C25S12M3', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'A2C25S12M3-F', 'kicadSymbolFootprint': 'Transistor_Power_Module:ST_ACEPACK-2-CIB_PressFIT', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/a2c25s12m3-f.pdf', 'kicadSymbolki_keywords': 'IGBT Power Module Trench Field Stop Technology M series', 'kicadSymbolki_description': '25A, 1200V, 20kHz, 197W x 6 , 3-phase, Freewheeling Diode, Brake Chopper, Diode Rectifier, 5k NTC, PressFIT, ACEPACK-2-CIB', 'kicadSymbolki_fp_filters': 'ST*ACEPACK*2*CIB*PressFIT*'}])
    newPart['name'].append('Transistor_Power_Module : A2C25S12M3-F')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

