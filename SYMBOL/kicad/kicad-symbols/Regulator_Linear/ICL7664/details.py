
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "ICL7664"
    hexID = "SZKREGULATORLINEARICL7664"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ICL7664', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://pe2bz.philpem.me.uk/pdf%20on%20typenumber/I-L/ICL7664.pdf', 'kicadSymbolki_keywords': 'Linear Regulator 50mA -5V fixed negative', 'kicadSymbolki_description': '50mA Dual Mode -5V/Programmable Negative Voltage Regulator, DIP-8/SO-8/TO-99', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x4.9mm*P1.27mm* TO?99*'}])
    newPart['name'].append('Regulator_Linear : ICL7664')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

