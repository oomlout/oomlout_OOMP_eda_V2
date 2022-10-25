
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Relay_THT"
    oIndex = "Relay_StandexMeder_UMS"
    hexID = "FZKRELRELAYSTANDEXMEDERUMS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Relay_StandexMeder_UMS', 'description': 'Standex-Meder SIL-relais, UMS, see http://cdn-reichelt.de/documents/datenblatt/C300/UMS05_1A80_75L_DB.pdf', 'tags': 'Standex Meder SIL reed relais', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Relay_THT.3dshapes/Relay_StandexMeder_UMS.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Relay_THT : Relay_StandexMeder_UMS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

