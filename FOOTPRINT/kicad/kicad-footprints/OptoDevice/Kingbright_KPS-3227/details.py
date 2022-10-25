
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "OptoDevice"
    oIndex = "Kingbright_KPS-3227"
    hexID = "FZKOPKINGBRIGHTKPS3227"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Kingbright_KPS-3227', 'description': '3.2mmx2.7mm, light sensor, https://www.kingbright.com/attachments/file/psearch/000/00/00/KPS-3227SP1C(Ver.16).pdf', 'tags': 'KPS-3227 Ambient Light Photo Sensor', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/Kingbright_KPS-3227.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('OptoDevice : Kingbright_KPS-3227')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

