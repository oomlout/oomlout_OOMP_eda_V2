
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Antenna"
    oIndex = "Pulse_W3011"
    hexID = "FZKRFPULSEW311"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Pulse_W3011', 'description': 'Pulse RF Antenna, 4mm Clearance', 'tags': 'antenna rf', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Antenna.3dshapes/Pulse_W3011.wrl', 'pins': {'type': 'smd', 'shape': 'trapezoid'}})
    newPart['name'].append('RF_Antenna : Pulse_W3011')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

