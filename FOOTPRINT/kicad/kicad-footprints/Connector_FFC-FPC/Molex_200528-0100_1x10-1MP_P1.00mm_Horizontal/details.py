
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_FFC-FPC"
    oIndex = "Molex_200528-0100_1x10-1MP_P1.00mm_Horizontal"
    hexID = "FZKCNFFCFPCMX252811X11MPP1HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_200528-0100_1x10-1MP_P1.00mm_Horizontal', 'description': 'Molex Molex 1.00mm Pitch Easy-On BackFlip, Right-Angle, Bottom Contact FFC/FPC, 200528-0100, 10 Circuits (https://www.molex.com/pdm_docs/sd/2005280100_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex  top entry', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_FFC-FPC.3dshapes/Molex_200528-0100_1x10-1MP_P1.00mm_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_FFC-FPC : Molex_200528-0100_1x10-1MP_P1.00mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

