
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "OKI-78SR-3.3_1.5-W36H-C"
    hexID = "SZKCONOKI78SR3315W36HC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'OKI-78SR-3.3_1.5-W36H-C', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_Murata_OKI-78SR_Horizontal', 'kicadSymbolDatasheet': 'https://power.murata.com/data/power/oki-78sr.pdf', 'kicadSymbolki_keywords': 'dc-dc murata Step-Down DC/DC-Regulator', 'kicadSymbolki_description': '1.5A Step-Down DC/DC-Regulator, 7-36V input, 3.3V fixed Output Voltage, LM78xx replacement, -40°C to +85°C, OKI-78SR_Horizontal', 'kicadSymbolki_fp_filters': 'Converter*DCDC*Murata*OKI*78SR*Horizontal*'}])
    newPart['name'].append('OKI-78SR-3.3_1.5-W36H-C')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

