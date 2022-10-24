
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "SOIC-8_7.5x5.85mm_P1.27mm"
    hexID = "FZKSOSOIC875X585P127"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SOIC-8_7.5x5.85mm_P1.27mm', 'description': 'SOIC, 8 Pin (http://www.ti.com/lit/ml/mpds382b/mpds382b.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'SOIC SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SOIC-8_7.5x5.85mm_P1.27mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : SOIC-8_7.5x5.85mm_P1.27mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

