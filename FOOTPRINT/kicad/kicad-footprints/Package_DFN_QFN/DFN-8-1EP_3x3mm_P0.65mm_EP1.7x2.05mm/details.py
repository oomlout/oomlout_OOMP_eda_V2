
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "DFN-8-1EP_3x3mm_P0.65mm_EP1.7x2.05mm"
    hexID = "FZKDFNDFN81EP3X3P65EP17X25"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DFN-8-1EP_3x3mm_P0.65mm_EP1.7x2.05mm', 'description': 'DFN, 8 Pin (http://www.ixysic.com/home/pdfs.nsf/www/IX4426-27-28.pdf/$file/IX4426-27-28.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'DFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-8-1EP_3x3mm_P0.65mm_EP1.7x2.05mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : DFN-8-1EP_3x3mm_P0.65mm_EP1.7x2.05mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

