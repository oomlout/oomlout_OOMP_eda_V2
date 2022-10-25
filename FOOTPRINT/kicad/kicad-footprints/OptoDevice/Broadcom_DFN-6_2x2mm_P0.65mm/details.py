
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "OptoDevice"
    oIndex = "Broadcom_DFN-6_2x2mm_P0.65mm"
    hexID = "FZKOPBROADCOMDFN62X2P65"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Broadcom_DFN-6_2x2mm_P0.65mm', 'description': 'Broadcom  DFN, 6 Pin (https://docs.broadcom.com/docs/AV02-4755EN), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'Broadcom DFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/Broadcom_DFN-6_2x2mm_P0.65mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('OptoDevice : Broadcom_DFN-6_2x2mm_P0.65mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

