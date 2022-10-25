
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Crystal"
    oIndex = "Crystal_SMD_MicroCrystal_CC7V-T1A-2Pin_3.2x1.5mm"
    hexID = "FZKXXSMMXCC7VT1A2PIN32X15"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Crystal_SMD_MicroCrystal_CC7V-T1A-2Pin_3.2x1.5mm', 'description': 'SMD Crystal MicroCrystal CC7V-T1A/CM7V-T1A series https://www.microcrystal.com/fileadmin/Media/Products/32kHz/Datasheet/CC7V-T1A.pdf, 3.2x1.5mm^2 package', 'tags': 'SMD SMT crystal', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Crystal_SMD_MicroCrystal_CC7V-T1A-2Pin_3.2x1.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Crystal : Crystal_SMD_MicroCrystal_CC7V-T1A-2Pin_3.2x1.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

