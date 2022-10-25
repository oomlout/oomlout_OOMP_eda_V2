
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Antenna"
    oIndex = "Texas_SWRA117D_2.4GHz_Right"
    hexID = "FZKRFTEXASSWRA117D24GHZRIGHT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_SWRA117D_2.4GHz_Right', 'description': 'http://www.ti.com/lit/an/swra117d/swra117d.pdf', 'tags': 'PCB antenna', 'attributeType': None, 'pins': {'type': 'connect', 'shape': 'rect'}})
    newPart['name'].append('RF_Antenna : Texas_SWRA117D_2.4GHz_Right')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

