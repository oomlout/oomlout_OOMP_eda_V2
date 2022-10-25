
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "TLV9062xDSG"
    hexID = "SZKAMPLIFIEROPERATIONALTLV962XDSG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'OPA2333xxDRB', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLV9062xDSG', 'kicadSymbolFootprint': 'Package_SON:WSON-8-1EP_2x2mm_P0.5mm_EP0.9x1.6mm_ThermalVias', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/tlv9062.pdf', 'kicadSymbolki_keywords': 'dual opamp low-power', 'kicadSymbolki_description': 'Dual operational amplifier, 210uV Offset, 0.25uV/C, low-noise, WSON-8', 'kicadSymbolki_fp_filters': 'WSON*1EP?2x2mm*P0.5mm*'}])
    newPart['name'].append('Amplifier_Operational : TLV9062xDSG')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

