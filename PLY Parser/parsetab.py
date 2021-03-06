
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = 'EAD2CAD0BBC63127FD74F3007D201FA6'
    
_lr_action_items = {'%':([24,31,],[27,35,]),'STRING':([0,1,4,7,8,9,12,15,18,21,22,23,27,35,36,39,42,43,44,],[1,7,8,9,11,12,15,18,21,24,25,26,31,39,-5,42,45,46,47,]),'.':([28,],[32,]),'INTEGER':([0,8,10,11,13,14,16,17,19,20,25,26,29,30,32,33,34,36,40,41,],[4,10,13,14,16,17,19,20,22,23,28,28,28,28,36,37,38,-5,28,28,]),':':([37,38,],[40,41,]),'$end':([0,2,3,5,6,45,46,47,],[-8,-1,0,-2,-3,-4,-7,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[3,]),'float':([25,26,29,30,40,41,],[29,30,33,34,43,44,]),'data':([0,],[5,]),'empty':([0,],[6,]),'header':([0,],[2,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> header','start',1,'p_start','PLYstarter.py',38),
  ('start -> data','start',1,'p_start','PLYstarter.py',39),
  ('start -> empty','start',1,'p_start','PLYstarter.py',40),
  ('header -> STRING STRING STRING STRING STRING STRING STRING STRING % STRING % STRING STRING STRING','header',14,'p_header','PLYstarter.py',45),
  ('float -> INTEGER . INTEGER','float',3,'p_float','PLYstarter.py',49),
  ('data -> INTEGER STRING STRING INTEGER INTEGER INTEGER INTEGER STRING float float INTEGER : float STRING','data',14,'p_data','PLYstarter.py',53),
  ('data -> INTEGER STRING INTEGER INTEGER INTEGER INTEGER INTEGER STRING float float INTEGER : float STRING','data',14,'p_data','PLYstarter.py',54),
  ('empty -> <empty>','empty',0,'p_empty','PLYstarter.py',59),
]
