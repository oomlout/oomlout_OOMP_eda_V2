
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Transformer_SMD"
    oIndex = "Pulse_PA2777NL"
    hexID = "FZKTRSMPULSEPA2777NL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Pulse_PA2777NL', 'description': 'SMT Gate Drive Transformer, 1:1, 7.1x6.1x5.5mm (https://productfinder.pulseeng.com/products/datasheets/SPM2007_61.pdf)', 'tags': 'pulse pa2777nl', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Transformer_SMD.3dshapes/Pulse_PA2777NL.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Transformer_SMD : Pulse_PA2777NL')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

