
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_QFP"
    oIndex = "VQFP-128_14x14mm_P0.4mm"
    hexID = "FZKQFPVQFP12814X14P4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'VQFP-128_14x14mm_P0.4mm', 'description': 'VQFP, 128 Pin (http://www.microsemi.com/index.php?option=com_docman&task=doc_download&gid=131095), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'VQFP QFP', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_QFP.3dshapes/VQFP-128_14x14mm_P0.4mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_QFP : VQFP-128_14x14mm_P0.4mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

