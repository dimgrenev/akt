# -*- coding: utf-8 -*-

from __future__ import print_function, division, absolute_import
from fontTools.varLib.models import VariationModel, normalizeLocation


# alternative axisMapper that uses map_forward and map_backward from fonttools

class AxisMapper(object):
    def __init__(self, axes):
        # axes: list of axis axisdescriptors
        self.axisOrder = [a.name for a in axes]
        self.axisDescriptors = {}
        for a in axes:
            self.axisDescriptors[a.name] = a

    def getMappedAxisValues(self):
        values = {}
        for axisName in self.axisOrder:
            a = self.axisDescriptors[axisName]
            values[axisName] = a.map_forward(a.minimum), a.map_forward(a.default), a.map_forward(a.maximum)
        return values

    def __call__(self, location):
        return self.map_forward(location)

    def _normalize(self, location):
        new = {}
        for axisName in location.keys():
            new[axisName] = normalizeLocation(dict(w=location[axisName]), dict(w=self.axes[axisName]))
        return new

    def map_backward(self, location):
        new = {}
        for axisName in location.keys():
            if not axisName in self.axisOrder:
                continue
            if axisName not in location:
                continue
            new[axisName] = self.axisDescriptors[axisName].map_backward(location[axisName])
        return new

    def map_forward(self, location):
        new = {}
        for axisName in location.keys():
            if not axisName in self.axisOrder:
                continue
            if axisName not in location:
                continue
            new[axisName] = self.axisDescriptors[axisName].map_forward(location[axisName])
        return new



class VariationModelMutator(object):
    """ a thing that looks like a mutator on the outside,
        but uses the fonttools varlib logic to calculate.
    """

    def __init__(self, items, axes, model=None, extrapolate=True):
        # items: list of locationdict, value tuples
        # axes: list of axis dictionaries, not axisdescriptor objects.
        # model: a model, if we want to share one
        self.extrapolate = extrapolate
        self.axisOrder = [a.name for a in axes]
        self.axisMapper = AxisMapper(axes)
        self.axes = {}
        for a in axes:
            axisMinimum, axisMaximum = self.getAxisMinMax(a)
            mappedMinimum, mappedDefault, mappedMaximum = a.map_forward(axisMinimum), a.map_forward(a.default), a.map_forward(axisMaximum)
            self.axes[a.name] = (mappedMinimum, mappedDefault, mappedMaximum)
            
        if model is None:
            dd = [self._normalize(a) for a,b in items]
            ee = self.axisOrder
            self.model = VariationModel(dd, axisOrder=ee, extrapolate=self.extrapolate)
        else:
            self.model = model
        self.masters = [b for a, b in items]
        self.locations = [a for a, b in items]

    def getAxisMinMax(self, axis):
        # return tha axis.minimum and axis.maximum for continuous axes
        # return the min(axis.values), max(axis.values) for discrete axes
        if hasattr(axis, "values"):
            return min(axis.values), max(axis.values)
        return axis.minimum, axis.maximum

    def get(self, key):
        if key in self.model.locations:
            i = self.model.locations.index(key)
            return self.masters[i]
        return None

    def getFactors(self, location):
        nl = self._normalize(location)
        return self.model.getScalars(nl)

    def getMasters(self):
        return self.masters

    def getSupports(self):
        return self.model.supports

    def getReach(self):
        items = []
        for supportIndex, s in enumerate(self.getSupports()):
            sortedOrder = self.model.reverseMapping[supportIndex]
            items.append((self.masters[sortedOrder], s))
        return items

    def makeInstance(self, location, bend=False):
        # check for anisotropic locations here
        if bend:
            location = self.axisMapper(location)
        nl = self._normalize(location)
        return self.model.interpolateFromMasters(nl, self.masters)

    def _normalize(self, location):
        return normalizeLocation(location, self.axes)


if __name__ == "__main__":
    from fontTools.designspaceLib import AxisDescriptor
    a = AxisDescriptor()
    a.name = "A"
    a.tag = "A___"
    a.minimum = 40
    a.default = 45
    a.maximum = 50
    a.map = [(40, -100), (45,0), (50, 100)]

    b = AxisDescriptor()
    b.name = "B"
    b.tag = "B___"
    b.minimum = 0
    b.default = 50
    b.maximum = 100
    axes = [a,b]
    
    items = [
        ({}, 0),
        #({'A': 50, 'B': 50}, 10),
        ({'A': 40}, 10),
        ({'B': 50}, -10),
        #({'B': -100}, -10),    # this will fail, no extrapolating
        ({'A': 40, 'B': 50}, 22),
        #({'A': 55, 'B': 75}, 1),
        #({'A': 65, 'B': 99}, 1),
    ]

    am = AxisMapper(axes)
    #assert am(dict(A=0)) == {'A': 45}
    print(1, am(dict(A=40, B=None)))
    #assert am(dict(A=0, B=100)) == {'A': 45}

    # mm = VariationModelMutator(items, axes)

    # assert mm.makeInstance(dict(A=0, B=0)) == 0
    # assert mm.makeInstance(dict(A=100, B=0)) == 10
    # assert mm.makeInstance(dict(A=0, B=100)) == 10
    # assert mm.makeInstance(dict(A=100, B=100)) == 0
    # assert mm.makeInstance(dict(A=50, B=0),bend=False) == 5
    # assert mm.makeInstance(dict(A=50, B=0),bend=True) == 2.5

    # mm.getReach()

    

    a = AxisDescriptor()
    a.name = "Weight"
    a.tag = "wght"
    a.minimum = 300
    a.default = 300
    a.maximum = 600
    a.map = ((300,0), (600,1000))

    b = AxisDescriptor()
    b.name = "Width"
    b.tag = "wdth"
    b.minimum = 200
    b.default = 800
    b.maximum = 800
    b.map = ((200,5), (800,10))
    axes = [a,b]
    
    aam = AxisMapper(axes)
    print(2, aam({}))
    print(2, aam(dict(Weight=300, Width=200)))
    print(2, aam(dict(Weight=0, Width=0)))
    print(2, 'getMappedAxisValues', aam.getMappedAxisValues())

    print(2, aam.map_forward({'Weight': 0}))

    # fine. sources are in user values. Progress.
    # are they?
    items = [
        ({}, 13),
        ({'Weight': 0, 'Width': 5}, 20),
        ({'Weight': 1000, 'Width': 10}, 60),
    ]

    mm = VariationModelMutator(items, axes)
    # ok so normalise uses designspace coordinates
    print(3, "_normalize", mm._normalize(dict(Weight=0, Width=1000)))   
    # oh wow, master locations need to be in user coordinates!?
    print('mm.makeInstance(dict())', mm.makeInstance(dict()))
    assert mm.makeInstance(dict()) == 13
    assert mm.makeInstance(dict(Weight=0, Width=10)) == 13


    l = dict(Weight=400, Width=20)
    lmapped = aam(l)
    print('0 loc', l)
    print('0 loc mapped', lmapped)
    print('1 with map', mm.makeInstance(l, bend=True))
    print('1 without map', mm.makeInstance(l, bend=False))
    print('2 with map', mm.makeInstance(lmapped, bend=True))
    print('2 without map', mm.makeInstance(lmapped, bend=False))
