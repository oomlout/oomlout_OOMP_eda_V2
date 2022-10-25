
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "HTSSOP-44_6.1x14mm_P0.635mm_TopEP4.14x7.01mm"
    hexID = "FZKSOHTSS4461X14P635TOPEP414X71"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'HTSSOP-44_6.1x14mm_P0.635mm_TopEP4.14x7.01mm', 'description': 'HTSSOP, 44 Pin (http://www.ti.com/lit/ds/symlink/tpa3251.pdf#page=38), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'HTSSOP SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/HTSSOP-44_6.1x14mm_P0.635mm_TopEP4.14x7.01mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : HTSSOP-44_6.1x14mm_P0.635mm_TopEP4.14x7.01mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

