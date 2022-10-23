
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "D3V3XA4B10LP"
    hexID = "SZKPOWERPROTECTIOND3V3XA4B1LP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'D3V3XA4B10LP', 'kicadSymbolFootprint': 'Package_DFN_QFN:Diodes_UDFN-10_1.0x2.5mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/D3V3XA4B10LP.pdf', 'kicadSymbolki_keywords': 'ESD protection TVS', 'kicadSymbolki_description': '4-Channel Low Capacitance TVS Diode Array, DFN-10', 'kicadSymbolki_fp_filters': 'Diodes*UDFN*1.0x2.5mm*P0.5mm*'}])
    newPart['name'].append('D3V3XA4B10LP')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

