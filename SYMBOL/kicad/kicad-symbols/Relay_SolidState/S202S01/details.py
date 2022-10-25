
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay_SolidState"
    oIndex = "S202S01"
    hexID = "SZKRELAYSOLIDSTATES22S1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'S102S01', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'S202S01', 'kicadSymbolFootprint': 'Package_SIP:SIP4_Sharp-SSR_P7.62mm_Straight', 'kicadSymbolDatasheet': 'http://www.sharp-world.com/products/device/lineup/data/pdf/datasheet/s102s01_e.pdf', 'kicadSymbolki_keywords': 'Opto-Triac Opto Triac Random Phase Solid State Relays', 'kicadSymbolki_description': 'Random Phase Opto-Triac, Vdrm 600V, Ift 8mA, IT 8A', 'kicadSymbolki_fp_filters': 'SIP4*Sharp*SSR*P7.62mm*'}])
    newPart['name'].append('Relay_SolidState : S202S01')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

