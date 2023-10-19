"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

group = {'Jil':{'age':26,
                'job':'Biologist',
                'connections':{'friend':['Zalika'], 
                               'partner':['John'],
                               'cousin':[], 
                               'landlord':[]}},
'Zalika':{'age':28,
          'job':'Artist',
          'connections':{'friend':['Jill'], 
                               'partner':[],
                               'cousin':[], 
                               'landlord':[]}},
'John':{'age':27,
        'job':'Writer',
        'connections':{'friend':[], 
                               'partner':['Jill'],
                               'cousin':[], 
                               'landlord':[]}},
'Nash':{'age':34,
        'job':'Chef',
        'connections':{'friend':[], 
                               'partner':[],
                               'cousin':['John'], 
                               'landlord':['Zalika']}}
}



