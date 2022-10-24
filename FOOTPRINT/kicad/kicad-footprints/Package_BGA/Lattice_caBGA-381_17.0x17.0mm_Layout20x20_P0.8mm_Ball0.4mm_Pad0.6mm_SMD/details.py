
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "Lattice_caBGA-381_17.0x17.0mm_Layout20x20_P0.8mm_Ball0.4mm_Pad0.6mm_SMD"
    hexID = "FZKBGALATTICECABGA38117X17LAYOUT2X2P8BALL4PAD6SM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Lattice_caBGA-381_17.0x17.0mm_Layout20x20_P0.8mm_Ball0.4mm_Pad0.6mm_SMD', 'description': 'Lattice caBGA-381 footprint for ECP5 FPGAs, based on http://www.latticesemi.com/view_document?document_id=213', 'tags': 'BGA 381 0.8', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Lattice_caBGA-381_17.0x17.0mm_Layout20x20_P0.8mm_Ball0.4mm_Pad0.6mm_SMD.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : Lattice_caBGA-381_17.0x17.0mm_Layout20x20_P0.8mm_Ball0.4mm_Pad0.6mm_SMD')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

