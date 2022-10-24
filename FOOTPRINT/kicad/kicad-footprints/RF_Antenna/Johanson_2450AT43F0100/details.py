
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Antenna"
    oIndex = "Johanson_2450AT43F0100"
    hexID = "FZKRFJOHANSON245AT43F1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Johanson_2450AT43F0100', 'description': 'Johanson 2450AT43F0100 SMD antenna 2400-2500Mhz, 1dBi, https://www.johansontechnology.com/datasheets/2450AT43F0100/2450AT43F0100.pdf', 'tags': 'antenna', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Antenna.3dshapes/Johanson_2450AT43F0100.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('RF_Antenna : Johanson_2450AT43F0100')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

