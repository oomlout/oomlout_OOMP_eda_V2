
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_QFP"
    oIndex = "PQFP-208_28x28mm_P0.5mm"
    hexID = "FZKQFPPQFP2828X28P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PQFP-208_28x28mm_P0.5mm', 'description': 'PQFP, 208 Pin (http://www.microsemi.com/index.php?option=com_docman&task=doc_download&gid=131095), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'PQFP QFP', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_QFP.3dshapes/PQFP-208_28x28mm_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_QFP : PQFP-208_28x28mm_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

