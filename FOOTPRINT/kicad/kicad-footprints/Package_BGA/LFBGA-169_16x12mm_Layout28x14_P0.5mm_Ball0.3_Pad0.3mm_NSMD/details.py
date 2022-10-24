
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "LFBGA-169_16x12mm_Layout28x14_P0.5mm_Ball0.3_Pad0.3mm_NSMD"
    hexID = "FZKBGALFBGA16916X12LAYOUT28X14P5BALL3PAD3NSM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LFBGA-169_16x12mm_Layout28x14_P0.5mm_Ball0.3_Pad0.3mm_NSMD', 'description': 'https://4donline.ihs.com/images/VipMasterIC/IC/SGST/SGSTS20279/SGSTS20279-1.pdf?hkey=EF798316E3902B6ED9A73243A3159BB0', 'tags': 'eMMC Flash LFBGA169', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/LFBGA-169_16x12mm_Layout28x14.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : LFBGA-169_16x12mm_Layout28x14_P0.5mm_Ball0.3_Pad0.3mm_NSMD')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

