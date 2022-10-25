
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_TO_SOT_SMD"
    oIndex = "SOT-23-8"
    hexID = "FZKPACKAGETOSOTSMSOT238"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SOT-23-8', 'description': 'SOT, 8 Pin (https://www.jedec.org/sites/default/files/docs/Mo-178c.PDF variant BA), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'SOT TO_SOT_SMD', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_SMD.3dshapes/SOT-23-8.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_TO_SOT_SMD : SOT-23-8')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

