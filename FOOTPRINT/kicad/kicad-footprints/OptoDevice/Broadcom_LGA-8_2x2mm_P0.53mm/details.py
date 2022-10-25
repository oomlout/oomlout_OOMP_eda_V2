
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "OptoDevice"
    oIndex = "Broadcom_LGA-8_2x2mm_P0.53mm"
    hexID = "FZKOPBROADCOMLGA82X2P53"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Broadcom_LGA-8_2x2mm_P0.53mm', 'description': 'Broadcom  LGA, 8 Pin (https://docs.broadcom.com/docs/AV02-4755EN), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'Broadcom LGA NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/Broadcom_LGA-8_2x2mm_P0.53mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('OptoDevice : Broadcom_LGA-8_2x2mm_P0.53mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

