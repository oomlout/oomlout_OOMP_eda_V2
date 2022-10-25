
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "OptoDevice"
    oIndex = "Kingbright_KPS-5130"
    hexID = "FZKOPKINGBRIGHTKPS513"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Kingbright_KPS-5130', 'description': 'http://www.kingbright.com/attachments/file/psearch/000/00/00/KPS-5130PD7C(Ver.14).pdf', 'tags': 'KPS-5130 photodiode RGB sensor', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/Kingbright_KPS-5130.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('OptoDevice : Kingbright_KPS-5130')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

