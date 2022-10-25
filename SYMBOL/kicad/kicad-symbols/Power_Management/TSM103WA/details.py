
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "TSM103WA"
    hexID = "SZKPOWERMANAGEMENTTSM13WA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TSM103W', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TSM103WA', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.st.com/resource/en/datasheet/tsm103w.pdf', 'kicadSymbolki_keywords': 'dual opamp reference', 'kicadSymbolki_description': 'Dual Operational Amplifier and 2.5V 0.4% Voltage Reference, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Power_Management : TSM103WA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

