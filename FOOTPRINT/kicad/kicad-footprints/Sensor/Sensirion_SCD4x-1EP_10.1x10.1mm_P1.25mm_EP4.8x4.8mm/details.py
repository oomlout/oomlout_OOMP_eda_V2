
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor"
    oIndex = "Sensirion_SCD4x-1EP_10.1x10.1mm_P1.25mm_EP4.8x4.8mm"
    hexID = "FZKSENSENSIRIONSCD4X1EP11X11P125EP48X48"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Sensirion_SCD4x-1EP_10.1x10.1mm_P1.25mm_EP4.8x4.8mm', 'description': 'Sensirion SCD4x QFN, 20 Pin (https://sensirion.com/media/documents/C4B87CE6/627C2DCD/CD_DS_SCD40_SCD41_Datasheet_D1.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'Sensirion QFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Sensor.3dshapes/Sensirion_SCD4x-1EP_10.1x10.1mm_P1.25mm_EP4.8x4.8mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Sensor : Sensirion_SCD4x-1EP_10.1x10.1mm_P1.25mm_EP4.8x4.8mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

