
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay_SolidState"
    oIndex = "AQH2223A"
    hexID = "SZKRELAYSOLIDSTATEAQH2223A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AQH0223A', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AQH2223A', 'kicadSymbolFootprint': 'Package_SO:SSO-7-8_6.4x9.78mm_P2.54mm', 'kicadSymbolDatasheet': 'https://b2b-api.panasonic.eu/file_stream/pids/fileversion/2787', 'kicadSymbolki_keywords': 'Opto-Triac Opto Triac Random Phase', 'kicadSymbolki_description': 'Random Phase Opto-Triac, Vdrm 600V, Ift 10mA, IT 900mA, SOIC-7', 'kicadSymbolki_fp_filters': 'SSO*6.4x9.78mm*P2.54mm*'}])
    newPart['name'].append('Relay_SolidState : AQH2223A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

