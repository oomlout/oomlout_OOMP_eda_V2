
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Module"
    oIndex = "A20_OLINUXINO_LIME2"
    hexID = "FZKMOA2OLINUXINOLIME2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'A20_OLINUXINO_LIME2', 'description': 'A20 Olinuxino LIME2, 1.2GHz, 512-1024MB RAM, Micro-SD, NAND or eMMC, 1000Mbit Ethernet', 'tags': 'A20 Olimex Olinuxino LIME2 development board', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Module.3dshapes/A20_OLINUXINO_LIME2.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Module : A20_OLINUXINO_LIME2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

