
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_FFC-FPC"
    oIndex = "Molex_200528-0260_1x26-1MP_P1.00mm_Horizontal"
    hexID = "FZKCNFFCFPCMX2528261X261MPP1HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_200528-0260_1x26-1MP_P1.00mm_Horizontal', 'description': 'Molex Molex 1.00mm Pitch Easy-On BackFlip, Right-Angle, Bottom Contact FFC/FPC, 200528-0260, 26 Circuits (https://www.molex.com/pdm_docs/sd/2005280260_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex  top entry', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_FFC-FPC.3dshapes/Molex_200528-0260_1x26-1MP_P1.00mm_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_FFC-FPC : Molex_200528-0260_1x26-1MP_P1.00mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

