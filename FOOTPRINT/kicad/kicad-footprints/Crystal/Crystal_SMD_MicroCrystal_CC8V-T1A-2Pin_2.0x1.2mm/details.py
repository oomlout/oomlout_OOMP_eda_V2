
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Crystal"
    oIndex = "Crystal_SMD_MicroCrystal_CC8V-T1A-2Pin_2.0x1.2mm"
    hexID = "FZKXXSMMXCC8VT1A2PIN2X12"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Crystal_SMD_MicroCrystal_CC8V-T1A-2Pin_2.0x1.2mm', 'description': 'SMD Crystal MicroCrystal CC8V-T1A/CM8V-T1A series https://www.microcrystal.com/fileadmin/Media/Products/32kHz/Datasheet/CC8V-T1A.pdf, 2.0x1.2mm^2 package', 'tags': 'SMD SMT crystal', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Crystal_SMD_MicroCrystal_CC8V-T1A-2Pin_2.0x1.2mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Crystal : Crystal_SMD_MicroCrystal_CC8V-T1A-2Pin_2.0x1.2mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

