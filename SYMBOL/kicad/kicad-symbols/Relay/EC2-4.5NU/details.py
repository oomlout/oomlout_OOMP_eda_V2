
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "EC2-4.5NU"
    hexID = "SZKRELAYEC245NU"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'EC2-3NU', 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'EC2-4.5NU', 'kicadSymbolFootprint': 'Relay_THT:Relay_DPDT_Kemet_EC2', 'kicadSymbolDatasheet': 'https://content.kemet.com/datasheets/KEM_R7002_EC2_EE2.pdf', 'kicadSymbolki_keywords': 'signal relay double pole double throw DPDT DC coil non latching', 'kicadSymbolki_description': 'General purpose signal relay, Kemet EC2 Series, DPDT (2 Form C), non-latching, through hole, 60W/125VA, 220VDC/250VAC, 2A, 4.5V DC coil', 'kicadSymbolki_fp_filters': 'Relay*THT*Kemet*EC2*'}])
    newPart['name'].append('Relay : EC2-4.5NU')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

