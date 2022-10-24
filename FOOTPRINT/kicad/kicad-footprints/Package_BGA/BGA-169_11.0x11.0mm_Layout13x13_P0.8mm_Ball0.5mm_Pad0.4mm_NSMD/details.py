
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "BGA-169_11.0x11.0mm_Layout13x13_P0.8mm_Ball0.5mm_Pad0.4mm_NSMD"
    hexID = "FZKBGABGA16911X11LAYOUT13X13P8BALL5PAD4NSM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BGA-169_11.0x11.0mm_Layout13x13_P0.8mm_Ball0.5mm_Pad0.4mm_NSMD', 'description': 'Altera U169, https://www.altera.com/content/dam/altera-www/global/en_US/pdfs/literature/packaging/04r00470-01.pdf', 'tags': 'Altera UBGA U169 BGA-169', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/BGA-169_11.0x11.0mm_Layout13x13_P0.8mm_Ball0.5mm_Pad0.4mm_NSMD.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : BGA-169_11.0x11.0mm_Layout13x13_P0.8mm_Ball0.5mm_Pad0.4mm_NSMD')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

