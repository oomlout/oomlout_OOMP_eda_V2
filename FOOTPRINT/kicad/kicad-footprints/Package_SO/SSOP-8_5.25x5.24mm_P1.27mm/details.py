
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "SSOP-8_5.25x5.24mm_P1.27mm"
    hexID = "FZKSOSS8525X524P127"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SSOP-8_5.25x5.24mm_P1.27mm', 'description': 'SSOP, 8 Pin (http://www.fujitsu.com/ca/en/Images/MB85RS2MT-DS501-00023-1v0-E.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'SSOP SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SSOP-8_5.25x5.24mm_P1.27mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : SSOP-8_5.25x5.24mm_P1.27mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

