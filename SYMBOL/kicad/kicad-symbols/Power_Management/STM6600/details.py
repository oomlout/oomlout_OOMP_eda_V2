
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "STM6600"
    hexID = "SZKPOWERMANAGEMENTSTM66"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM6600', 'kicadSymbolFootprint': 'Package_DFN_QFN:TDFN-12_2x3mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/resource/en/datasheet/stm6600.pdf', 'kicadSymbolki_keywords': 'push-button-controller low-power', 'kicadSymbolki_description': 'Smart push-button on/off controller, power-on lockout, Low Power, 1.6-5.5V, TDFN12', 'kicadSymbolki_fp_filters': 'TDFN*2x3mm*P0.5mm*'}])
    newPart['name'].append('STM6600')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

