
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_Power_Module"
    oIndex = "STGIPS20K60"
    hexID = "SZKTRANSISTORPOWERMOSTGIPS2K6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STGIPS20K60', 'kicadSymbolFootprint': 'Transistor_Power_Module:ST_SDIP-25L', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/stgips20k60.pdf', 'kicadSymbolki_keywords': 'SLLIMM IPM inverter short-circuit rugged IGBT', 'kicadSymbolki_description': '18 A, 600 V, 20KHz, 52Wx6,  3-phase, Control Logic, Negative Input , Freewheeling Diode, Undervoltage Lockout, Interlocking, Shut down (SD), Comparator, SDIP-25L', 'kicadSymbolki_fp_filters': 'ST*SDIP*'}])
    newPart['name'].append('STGIPS20K60')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

