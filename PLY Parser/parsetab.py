
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '637F75B41B3CE09EF0106E2F6BACDB32'
    
_lr_action_items = {'PID':([0,],[2,]),'$end':([0,1,2,3,],[-3,0,-1,-2,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'empty':([0,],[3,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> PID','start',1,'p_start','PLYstarter.py',38),
  ('start -> empty','start',1,'p_start','PLYstarter.py',39),
  ('empty -> <empty>','empty',0,'p_empty','PLYstarter.py',45),
]
