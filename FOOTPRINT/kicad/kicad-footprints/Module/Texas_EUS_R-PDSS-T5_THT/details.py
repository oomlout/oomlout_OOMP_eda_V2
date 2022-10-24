
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Module"
    oIndex = "Texas_EUS_R-PDSS-T5_THT"
    hexID = "FZKMOTEXASEUSRPDSST5THT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_EUS_R-PDSS-T5_THT', 'description': 'Texas Instruments EUS 5 Pin Double Sided Module', 'tags': 'module pcb', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Module.3dshapes/Texas_EUSR-PDSS-T5_THT.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Module : Texas_EUS_R-PDSS-T5_THT')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

