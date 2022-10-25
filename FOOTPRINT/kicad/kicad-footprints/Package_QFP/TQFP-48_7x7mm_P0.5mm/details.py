
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_QFP"
    oIndex = "TQFP-48_7x7mm_P0.5mm"
    hexID = "FZKQFPTQFP487X7P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TQFP-48_7x7mm_P0.5mm', 'description': 'TQFP, 48 Pin (https://www.jedec.org/system/files/docs/MS-026D.pdf var ABC), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'TQFP QFP', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_QFP.3dshapes/TQFP-48_7x7mm_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_QFP : TQFP-48_7x7mm_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

