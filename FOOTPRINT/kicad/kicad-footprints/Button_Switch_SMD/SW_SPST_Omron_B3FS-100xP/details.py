
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_SMD"
    oIndex = "SW_SPST_Omron_B3FS-100xP"
    hexID = "FZKBSWITCHSMSWSPSTOMRONB3FS1XP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_SPST_Omron_B3FS-100xP', 'description': 'Surface Mount Tactile Switch for High-Density Mounting, 3.1mm height, https://omronfs.omron.com/en_US/ecb/products/pdf/en-b3fs.pdf', 'tags': 'Tactile Switch', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_SMD.3dshapes/SW_SPST_Omron_B3FS-100xP.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Button_Switch_SMD : SW_SPST_Omron_B3FS-100xP')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

