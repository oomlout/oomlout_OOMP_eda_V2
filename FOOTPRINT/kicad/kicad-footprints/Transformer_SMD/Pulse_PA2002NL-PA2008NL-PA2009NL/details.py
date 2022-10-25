
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Transformer_SMD"
    oIndex = "Pulse_PA2002NL-PA2008NL-PA2009NL"
    hexID = "FZKTRSMPULSEPA22NLPA28NLPA29NL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Pulse_PA2002NL-PA2008NL-PA2009NL', 'description': 'SMT Gate Drive Transformer, 1:1:1 or 2:1:1 or 2.5:1:1 or 1:1, 9.0x8.6x7.6mm (https://productfinder.pulseeng.com/products/datasheets/P663.pdf)', 'tags': 'pulse pa2002nl pa2008nl pa2009nl p0544nl pa0184nl pa0297nl pa0510nl', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Transformer_SMD.3dshapes/Pulse_PA2002NL-PA2008NL-PA2009NL.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Transformer_SMD : Pulse_PA2002NL-PA2008NL-PA2009NL')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

