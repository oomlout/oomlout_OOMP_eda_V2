
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "Texas_S-PX2QFN-14"
    hexID = "FZKDFNTEXASSPX2QFN14"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_S-PX2QFN-14', 'description': 'Texas  QFN, 14 Pin (http://www.ti.com/lit/ds/symlink/tlv9004.pdf#page=64), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'Texas QFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Texas_S-PX2QFN-14.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : Texas_S-PX2QFN-14')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

