
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Relay_THT"
    oIndex = "Relay_SPDT_StandexMeder_SIL_Form1C"
    hexID = "FZKRELRELAYSPDTSTANDEXMEDERSILFORM1C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Relay_SPDT_StandexMeder_SIL_Form1C', 'description': 'Standex-Meder SIL-relais, Form 1C, see https://standexelectronics.com/wp-content/uploads/datasheet_reed_relay_SIL.pdf', 'tags': 'Standex Meder SIL reed relais', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Relay_THT.3dshapes/Relay_SPDT_StandexMeder_SIL_Form1C.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Relay_THT : Relay_SPDT_StandexMeder_SIL_Form1C')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

