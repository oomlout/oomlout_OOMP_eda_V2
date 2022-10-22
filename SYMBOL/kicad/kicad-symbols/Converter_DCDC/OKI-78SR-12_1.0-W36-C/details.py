
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "OKI-78SR-12_1.0-W36-C"
    hexID = "SZKCONOKI78SR121W36C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'OKI-78SR-3.3_1.5-W36-C', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'OKI-78SR-12_1.0-W36-C', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_Murata_OKI-78SR_Vertical', 'kicadSymbolDatasheet': 'https://power.murata.com/data/power/oki-78sr.pdf', 'kicadSymbolki_keywords': 'dc-dc murata Step-Down DC/DC-Regulator', 'kicadSymbolki_description': '1.0A Step-Down DC/DC-Regulator, 15-36V input, 12V fixed Output Voltage, LM78xx replacement, -40°C to +85°C, OKI-78SR_Vertical', 'kicadSymbolki_fp_filters': 'Converter*DCDC*Murata*OKI*78SR*Vertical*'}])
    newPart['name'].append('OKI-78SR-12_1.0-W36-C')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

