
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF"
    oIndex = "S116S02"
    hexID = "SZKRFS116S2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'S102S02', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'S116S02', 'kicadSymbolFootprint': 'Package_SIP:SIP4_Sharp-SSR_P7.62mm_Straight', 'kicadSymbolDatasheet': 'http://www.sharp-world.com/products/device/lineup/data/pdf/datasheet/s116s02_e.pdf', 'kicadSymbolki_keywords': 'Opto-Triac Opto Triac Zero Cross Solid State Relays', 'kicadSymbolki_description': 'Zero Cross Opto-Triac, Vdrm 400V, Ift 8mA, IT 16A', 'kicadSymbolki_fp_filters': 'SIP4*Sharp*SSR*P7.62mm*'}])
    newPart['name'].append('RF : S116S02')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

