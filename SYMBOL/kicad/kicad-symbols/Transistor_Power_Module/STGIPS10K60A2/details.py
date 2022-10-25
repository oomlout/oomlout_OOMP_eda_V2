
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_Power_Module"
    oIndex = "STGIPS10K60A2"
    hexID = "SZKTRANSISTORPOWERMOSTGIPS1K6A2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STGIPS10K60A', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STGIPS10K60A2', 'kicadSymbolFootprint': 'Transistor_Power_Module:ST_SDIP-25L', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/stgips10k60a2.pdf', 'kicadSymbolki_keywords': 'SLLIMM IPM inverter short-circuit rugged IGBT', 'kicadSymbolki_description': '10 A, 600 V, 20KHz, 33Wx6, 3-phase, Control Logic, Positive Input , Freewheeling Diodes, Undervoltage Lockout, Interlocking, 4k7 NTC, SDIP-25L', 'kicadSymbolki_fp_filters': 'ST*SDIP*'}])
    newPart['name'].append('Transistor_Power_Module : STGIPS10K60A2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

