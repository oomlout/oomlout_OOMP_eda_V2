
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_TO_SOT_SMD"
    oIndex = "TSOT-23-8"
    hexID = "FZKPACKAGETOSOTSMTSOT238"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TSOT-23-8', 'description': 'TSOT, 8 Pin (https://www.jedec.org/sites/default/files/docs/MO-193D.pdf variant BA), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'TSOT TO_SOT_SMD', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_SMD.3dshapes/TSOT-23-8.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_TO_SOT_SMD : TSOT-23-8')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

