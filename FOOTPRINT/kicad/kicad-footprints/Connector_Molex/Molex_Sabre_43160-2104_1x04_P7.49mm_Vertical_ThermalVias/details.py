
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_Sabre_43160-2104_1x04_P7.49mm_Vertical_ThermalVias"
    hexID = "FZKCNMXMXSABRE43162141X4P749VERTICALTHERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_Sabre_43160-2104_1x04_P7.49mm_Vertical_ThermalVias', 'description': 'Molex Sabre Power Connector, 43160-2104, With thermal vias in pads, 4 Pins per row (http://www.molex.com/pdm_docs/sd/431602102_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex Sabre side entry', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_Sabre_43160-2104_1x04_P7.49mm_Vertical_ThermalVias.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Molex : Molex_Sabre_43160-2104_1x04_P7.49mm_Vertical_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

