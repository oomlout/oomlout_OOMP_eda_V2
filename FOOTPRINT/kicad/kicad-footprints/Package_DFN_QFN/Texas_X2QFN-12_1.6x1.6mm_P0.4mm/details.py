
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "Texas_X2QFN-12_1.6x1.6mm_P0.4mm"
    hexID = "FZKDFNTEXASX2QFN1216X16P4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_X2QFN-12_1.6x1.6mm_P0.4mm', 'description': 'Texas  X2QFN, 12 Pin (http://www.ti.com/lit/ml/mpqf391c/mpqf391c.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'Texas X2QFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Texas_X2QFN-12_1.6x1.6mm_P0.4mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : Texas_X2QFN-12_1.6x1.6mm_P0.4mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

