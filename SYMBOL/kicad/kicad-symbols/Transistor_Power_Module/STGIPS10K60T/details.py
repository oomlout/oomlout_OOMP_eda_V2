
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_Power_Module"
    oIndex = "STGIPS10K60T"
    hexID = "SZKTRANSISTORPOWERMOSTGIPS1K6T"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STGIPS14K60T', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STGIPS10K60T', 'kicadSymbolFootprint': 'Transistor_Power_Module:ST_SDIP-25L', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/stgips10k60t.pdf', 'kicadSymbolki_keywords': 'SLLIMM IPM inverter short-circuit rugged IGBT', 'kicadSymbolki_description': '10 A, 600 V, 20KHz, 33Wx6, 3-phase, Control Logic, Negative Input , Freewheeling Diode, Undervoltage Lockout, Interlocking, Shut down (SD), 4k7 NTC, SDIP-25L', 'kicadSymbolki_fp_filters': 'ST*SDIP*'}])
    newPart['name'].append('STGIPS10K60T')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

