
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Transformer_SMD"
    oIndex = "Pulse_PA3493NL"
    hexID = "FZKTRSMPULSEPA3493NL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Pulse_PA3493NL', 'description': 'SMT Gate Drive Transformer, 1.25:1, 10.9x9.7x2.7mm (https://productfinder.pulseeng.com/products/datasheets/SPM2007_61.pdf)', 'tags': 'pulse pa3493nl', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Transformer_SMD.3dshapes/Pulse_PA3493NL.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Transformer_SMD : Pulse_PA3493NL')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

