
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "left+-left*/rightuminusleftouxouleftdiflefteqleftmaieqleftmeneqlefteleft<left>Fim Inicio assign ate carater de dif e enquanto entao eq escreva faca falso fim_enquanto fim_funcao fim_para fim_se float funcao int inteiro leia logico maieq meneq nao ou para passo real retorna se senao string varName verdadeiro void xou port : Inicio code Fim  port : fun Inicio code Fim  code : com  code : code com  fun : funcao varType varName '(' vars ')' ':' code fim_funcao  fun : funcao void varName '(' vars ')' ':' code fim_funcao  vars :  vars : varType varName\n                 | vars ',' varType varName  com : lines\n                | cond\n                | cycle  lines : varName assign value ';'  lines : varType ':' varName_list ';'  lines : escreva value_list ';'  lines : leia value_list ';'  lines : retorna value ';'  cond : se value entao code fim_se  cond : se value entao code senao code fim_se  cycle : para varName de value ate value passo value faca code fim_para  cycle : enquanto value_list faca code fim_enquanto value : varName  value : bool\n                  | calc\n                  | string  value : varName '(' value_list ')'\n                  | varName '(' ')'  varType : inteiro\n                    | real\n                    | carater\n                    | logico  varName_list : varName\n                         | varName_list ',' varName  value_list : value\n                       | value_list ',' value  value_list : '(' value_list ')'  bool : opt\n                 | value e value\n                 | value ou value\n                 | value xou value  calc : int\n                 | float\n                 | '-' value  %prec uminus   calc : value '+' value\n                 | value '-' value\n                 | value '*' value\n                 | value '/' value\n                 | value '<' value\n                 | value '>' value\n                 | value dif value\n                 | value eq value\n                 | value maieq value\n                 | value meneq value  opt : verdadeiro  opt : falso  opt : nao opt "
    
_lr_action_items = {'Inicio':([0,3,128,129,],[2,22,-5,-6,]),'funcao':([0,],[4,]),'$end':([1,25,78,],[0,-1,-2,]),'varName':([2,5,6,7,8,9,12,13,14,15,16,17,18,19,20,21,22,23,24,26,27,28,31,39,48,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,73,74,75,76,77,81,82,83,101,103,104,109,110,111,112,117,119,120,121,122,123,124,126,130,131,132,],[10,10,-3,-10,-11,-12,32,32,32,32,46,32,-28,-29,-30,-31,10,49,50,-4,32,53,32,32,10,-15,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-16,-17,10,32,10,-13,-14,107,10,10,113,-18,10,32,-21,10,10,125,10,-19,32,10,10,10,10,-20,]),'escreva':([2,5,6,7,8,9,22,26,48,54,73,74,75,77,81,82,101,103,109,110,112,117,119,121,122,124,126,130,131,132,],[12,12,-3,-10,-11,-12,12,-4,12,-15,-16,-17,12,12,-13,-14,12,12,-18,12,-21,12,12,12,-19,12,12,12,12,-20,]),'leia':([2,5,6,7,8,9,22,26,48,54,73,74,75,77,81,82,101,103,109,110,112,117,119,121,122,124,126,130,131,132,],[13,13,-3,-10,-11,-12,13,-4,13,-15,-16,-17,13,13,-13,-14,13,13,-18,13,-21,13,13,13,-19,13,13,13,13,-20,]),'retorna':([2,5,6,7,8,9,22,26,48,54,73,74,75,77,81,82,101,103,109,110,112,117,119,121,122,124,126,130,131,132,],[14,14,-3,-10,-11,-12,14,-4,14,-15,-16,-17,14,14,-13,-14,14,14,-18,14,-21,14,14,14,-19,14,14,14,14,-20,]),'se':([2,5,6,7,8,9,22,26,48,54,73,74,75,77,81,82,101,103,109,110,112,117,119,121,122,124,126,130,131,132,],[15,15,-3,-10,-11,-12,15,-4,15,-15,-16,-17,15,15,-13,-14,15,15,-18,15,-21,15,15,15,-19,15,15,15,15,-20,]),'para':([2,5,6,7,8,9,22,26,48,54,73,74,75,77,81,82,101,103,109,110,112,117,119,121,122,124,126,130,131,132,],[16,16,-3,-10,-11,-12,16,-4,16,-15,-16,-17,16,16,-13,-14,16,16,-18,16,-21,16,16,16,-19,16,16,16,16,-20,]),'enquanto':([2,5,6,7,8,9,22,26,48,54,73,74,75,77,81,82,101,103,109,110,112,117,119,121,122,124,126,130,131,132,],[17,17,-3,-10,-11,-12,17,-4,17,-15,-16,-17,17,17,-13,-14,17,17,-18,17,-21,17,17,17,-19,17,17,17,17,-20,]),'inteiro':([2,4,5,6,7,8,9,22,26,48,54,73,74,75,77,79,80,81,82,101,103,109,110,112,115,117,119,121,122,124,126,130,131,132,],[18,18,18,-3,-10,-11,-12,18,-4,18,-15,-16,-17,18,18,18,18,-13,-14,18,18,-18,18,-21,18,18,18,18,-19,18,18,18,18,-20,]),'real':([2,4,5,6,7,8,9,22,26,48,54,73,74,75,77,79,80,81,82,101,103,109,110,112,115,117,119,121,122,124,126,130,131,132,],[19,19,19,-3,-10,-11,-12,19,-4,19,-15,-16,-17,19,19,19,19,-13,-14,19,19,-18,19,-21,19,19,19,19,-19,19,19,19,19,-20,]),'carater':([2,4,5,6,7,8,9,22,26,48,54,73,74,75,77,79,80,81,82,101,103,109,110,112,115,117,119,121,122,124,126,130,131,132,],[20,20,20,-3,-10,-11,-12,20,-4,20,-15,-16,-17,20,20,20,20,-13,-14,20,20,-18,20,-21,20,20,20,20,-19,20,20,20,20,-20,]),'logico':([2,4,5,6,7,8,9,22,26,48,54,73,74,75,77,79,80,81,82,101,103,109,110,112,115,117,119,121,122,124,126,130,131,132,],[21,21,21,-3,-10,-11,-12,21,-4,21,-15,-16,-17,21,21,21,21,-13,-14,21,21,-18,21,-21,21,21,21,21,-19,21,21,21,21,-20,]),'void':([4,],[24,]),'Fim':([5,6,7,8,9,26,48,54,73,74,81,82,109,112,122,132,],[25,-3,-10,-11,-12,-4,78,-15,-16,-17,-13,-14,-18,-21,-19,-20,]),'fim_se':([6,7,8,9,26,54,73,74,81,82,101,109,112,117,122,132,],[-3,-10,-11,-12,-4,-15,-16,-17,-13,-14,109,-18,-21,122,-19,-20,]),'senao':([6,7,8,9,26,54,73,74,81,82,101,109,112,122,132,],[-3,-10,-11,-12,-4,-15,-16,-17,-13,-14,110,-18,-21,-19,-20,]),'fim_enquanto':([6,7,8,9,26,54,73,74,81,82,103,109,112,122,132,],[-3,-10,-11,-12,-4,-15,-16,-17,-13,-14,112,-18,-21,-19,-20,]),'fim_funcao':([6,7,8,9,26,54,73,74,81,82,109,112,122,124,126,132,],[-3,-10,-11,-12,-4,-15,-16,-17,-13,-14,-18,-21,-19,128,129,-20,]),'fim_para':([6,7,8,9,26,54,73,74,81,82,109,112,122,131,132,],[-3,-10,-11,-12,-4,-15,-16,-17,-13,-14,-18,-21,-19,132,-20,]),'assign':([10,],[27,]),':':([11,18,19,20,21,114,116,],[28,-28,-29,-30,-31,119,121,]),'(':([12,13,17,31,32,49,50,70,],[31,31,31,31,70,79,80,31,]),'string':([12,13,14,15,17,27,31,39,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,76,111,123,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'int':([12,13,14,15,17,27,31,39,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,76,111,123,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'float':([12,13,14,15,17,27,31,39,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,76,111,123,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'-':([12,13,14,15,17,27,30,31,32,33,34,35,36,37,38,39,40,41,44,45,51,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,71,72,76,84,85,86,87,88,89,90,91,92,93,94,95,96,97,100,102,108,111,118,123,127,],[39,39,39,39,39,39,60,39,-22,-23,-24,-25,-37,-41,-42,39,-54,-55,60,60,60,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,-43,-56,39,60,-38,-39,-40,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-27,60,-26,39,60,39,60,]),'verdadeiro':([12,13,14,15,17,27,31,39,42,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,76,111,123,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'falso':([12,13,14,15,17,27,31,39,42,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,76,111,123,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'nao':([12,13,14,15,17,27,31,39,42,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,76,111,123,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),';':([29,30,32,33,34,35,36,37,38,40,41,43,44,51,52,53,71,72,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,107,108,],[54,-34,-22,-23,-24,-25,-37,-41,-42,-54,-55,73,74,81,82,-32,-43,-56,-35,-38,-39,-40,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-36,-27,-33,-26,]),',':([29,30,32,33,34,35,36,37,38,40,41,43,47,52,53,69,71,72,79,80,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,105,106,107,108,113,125,],[55,-34,-22,-23,-24,-25,-37,-41,-42,-54,-55,55,55,83,-32,55,-43,-56,-7,-7,-35,-38,-39,-40,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-36,55,-27,115,115,-33,-26,-8,-9,]),'faca':([30,32,33,34,35,36,37,38,40,41,47,71,72,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,108,127,],[-34,-22,-23,-24,-25,-37,-41,-42,-54,-55,77,-43,-56,-35,-38,-39,-40,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-36,-27,-26,130,]),')':([30,32,33,34,35,36,37,38,40,41,69,70,71,72,79,80,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,105,106,108,113,125,],[-34,-22,-23,-24,-25,-37,-41,-42,-54,-55,98,100,-43,-56,-7,-7,-35,-38,-39,-40,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-36,108,-27,114,116,-26,-8,-9,]),'e':([30,32,33,34,35,36,37,38,40,41,44,45,51,71,72,84,85,86,87,88,89,90,91,92,93,94,95,96,97,100,102,108,118,127,],[56,-22,-23,-24,-25,-37,-41,-42,-54,-55,56,56,56,56,-56,56,-38,56,56,56,56,56,56,-48,-49,56,56,56,56,-27,56,-26,56,56,]),'ou':([30,32,33,34,35,36,37,38,40,41,44,45,51,71,72,84,85,86,87,88,89,90,91,92,93,94,95,96,97,100,102,108,118,127,],[57,-22,-23,-24,-25,-37,-41,-42,-54,-55,57,57,57,57,-56,57,-38,-39,-40,57,57,57,57,-48,-49,-50,-51,-52,-53,-27,57,-26,57,57,]),'xou':([30,32,33,34,35,36,37,38,40,41,44,45,51,71,72,84,85,86,87,88,89,90,91,92,93,94,95,96,97,100,102,108,118,127,],[58,-22,-23,-24,-25,-37,-41,-42,-54,-55,58,58,58,58,-56,58,-38,-39,-40,58,58,58,58,-48,-49,-50,-51,-52,-53,-27,58,-26,58,58,]),'+':([30,32,33,34,35,36,37,38,40,41,44,45,51,71,72,84,85,86,87,88,89,90,91,92,93,94,95,96,97,100,102,108,118,127,],[59,-22,-23,-24,-25,-37,-41,-42,-54,-55,59,59,59,-43,-56,59,-38,-39,-40,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-27,59,-26,59,59,]),'*':([30,32,33,34,35,36,37,38,40,41,44,45,51,71,72,84,85,86,87,88,89,90,91,92,93,94,95,96,97,100,102,108,118,127,],[61,-22,-23,-24,-25,-37,-41,-42,-54,-55,61,61,61,-43,-56,61,-38,-39,-40,61,61,-46,-47,-48,-49,-50,-51,-52,-53,-27,61,-26,61,61,]),'/':([30,32,33,34,35,36,37,38,40,41,44,45,51,71,72,84,85,86,87,88,89,90,91,92,93,94,95,96,97,100,102,108,118,127,],[62,-22,-23,-24,-25,-37,-41,-42,-54,-55,62,62,62,-43,-56,62,-38,-39,-40,62,62,-46,-47,-48,-49,-50,-51,-52,-53,-27,62,-26,62,62,]),'<':([30,32,33,34,35,36,37,38,40,41,44,45,51,71,72,84,85,86,87,88,89,90,91,92,93,94,95,96,97,100,102,108,118,127,],[63,-22,-23,-24,-25,-37,-41,-42,-54,-55,63,63,63,63,-56,63,63,63,63,63,63,63,63,-48,-49,63,63,63,63,-27,63,-26,63,63,]),'>':([30,32,33,34,35,36,37,38,40,41,44,45,51,71,72,84,85,86,87,88,89,90,91,92,93,94,95,96,97,100,102,108,118,127,],[64,-22,-23,-24,-25,-37,-41,-42,-54,-55,64,64,64,64,-56,64,64,64,64,64,64,64,64,64,-49,64,64,64,64,-27,64,-26,64,64,]),'dif':([30,32,33,34,35,36,37,38,40,41,44,45,51,71,72,84,85,86,87,88,89,90,91,92,93,94,95,96,97,100,102,108,118,127,],[65,-22,-23,-24,-25,-37,-41,-42,-54,-55,65,65,65,65,-56,65,-38,65,65,65,65,65,65,-48,-49,-50,-51,-52,-53,-27,65,-26,65,65,]),'eq':([30,32,33,34,35,36,37,38,40,41,44,45,51,71,72,84,85,86,87,88,89,90,91,92,93,94,95,96,97,100,102,108,118,127,],[66,-22,-23,-24,-25,-37,-41,-42,-54,-55,66,66,66,66,-56,66,-38,66,66,66,66,66,66,-48,-49,66,-51,-52,-53,-27,66,-26,66,66,]),'maieq':([30,32,33,34,35,36,37,38,40,41,44,45,51,71,72,84,85,86,87,88,89,90,91,92,93,94,95,96,97,100,102,108,118,127,],[67,-22,-23,-24,-25,-37,-41,-42,-54,-55,67,67,67,67,-56,67,-38,67,67,67,67,67,67,-48,-49,67,67,-52,-53,-27,67,-26,67,67,]),'meneq':([30,32,33,34,35,36,37,38,40,41,44,45,51,71,72,84,85,86,87,88,89,90,91,92,93,94,95,96,97,100,102,108,118,127,],[68,-22,-23,-24,-25,-37,-41,-42,-54,-55,68,68,68,68,-56,68,-38,68,68,68,68,68,68,-48,-49,68,68,68,-53,-27,68,-26,68,68,]),'entao':([32,33,34,35,36,37,38,40,41,45,71,72,85,86,87,88,89,90,91,92,93,94,95,96,97,100,108,],[-22,-23,-24,-25,-37,-41,-42,-54,-55,75,-43,-56,-38,-39,-40,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-27,-26,]),'ate':([32,33,34,35,36,37,38,40,41,71,72,85,86,87,88,89,90,91,92,93,94,95,96,97,100,102,108,],[-22,-23,-24,-25,-37,-41,-42,-54,-55,-43,-56,-38,-39,-40,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-27,111,-26,]),'passo':([32,33,34,35,36,37,38,40,41,71,72,85,86,87,88,89,90,91,92,93,94,95,96,97,100,108,118,],[-22,-23,-24,-25,-37,-41,-42,-54,-55,-43,-56,-38,-39,-40,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-27,-26,123,]),'de':([46,],[76,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'port':([0,],[1,]),'fun':([0,],[3,]),'code':([2,22,75,77,110,119,121,130,],[5,48,101,103,117,124,126,131,]),'com':([2,5,22,48,75,77,101,103,110,117,119,121,124,126,130,131,],[6,26,6,26,6,6,26,26,6,26,6,6,26,26,6,26,]),'lines':([2,5,22,48,75,77,101,103,110,117,119,121,124,126,130,131,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'cond':([2,5,22,48,75,77,101,103,110,117,119,121,124,126,130,131,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'cycle':([2,5,22,48,75,77,101,103,110,117,119,121,124,126,130,131,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'varType':([2,4,5,22,48,75,77,79,80,101,103,110,115,117,119,121,124,126,130,131,],[11,23,11,11,11,11,11,104,104,11,11,11,120,11,11,11,11,11,11,11,]),'value_list':([12,13,17,31,70,],[29,43,47,69,99,]),'value':([12,13,14,15,17,27,31,39,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,76,111,123,],[30,30,44,45,30,51,30,71,84,85,86,87,88,89,90,91,92,93,94,95,96,97,30,102,118,127,]),'bool':([12,13,14,15,17,27,31,39,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,76,111,123,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'calc':([12,13,14,15,17,27,31,39,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,76,111,123,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'opt':([12,13,14,15,17,27,31,39,42,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,76,111,123,],[36,36,36,36,36,36,36,36,72,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'varName_list':([28,],[52,]),'vars':([79,80,],[105,106,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> port","S'",1,None,None,None),
  ('port -> Inicio code Fim','port',3,'p_port1','logic_grammar.py',36),
  ('port -> fun Inicio code Fim','port',4,'p_port2','logic_grammar.py',40),
  ('code -> com','code',1,'p_code1','logic_grammar.py',46),
  ('code -> code com','code',2,'p_code2','logic_grammar.py',50),
  ('fun -> funcao varType varName ( vars ) : code fim_funcao','fun',9,'p_fun1','logic_grammar.py',56),
  ('fun -> funcao void varName ( vars ) : code fim_funcao','fun',9,'p_fun2','logic_grammar.py',60),
  ('vars -> <empty>','vars',0,'p_vars1','logic_grammar.py',66),
  ('vars -> varType varName','vars',2,'p_vars2','logic_grammar.py',70),
  ('vars -> vars , varType varName','vars',4,'p_vars2','logic_grammar.py',71),
  ('com -> lines','com',1,'p_com1','logic_grammar.py',80),
  ('com -> cond','com',1,'p_com1','logic_grammar.py',81),
  ('com -> cycle','com',1,'p_com1','logic_grammar.py',82),
  ('lines -> varName assign value ;','lines',4,'p_lines1','logic_grammar.py',88),
  ('lines -> varType : varName_list ;','lines',4,'p_lines2','logic_grammar.py',92),
  ('lines -> escreva value_list ;','lines',3,'p_lines3','logic_grammar.py',96),
  ('lines -> leia value_list ;','lines',3,'p_lines4','logic_grammar.py',100),
  ('lines -> retorna value ;','lines',3,'p_lines5','logic_grammar.py',104),
  ('cond -> se value entao code fim_se','cond',5,'p_cond1','logic_grammar.py',110),
  ('cond -> se value entao code senao code fim_se','cond',7,'p_cond2','logic_grammar.py',114),
  ('cycle -> para varName de value ate value passo value faca code fim_para','cycle',11,'p_cycle1','logic_grammar.py',120),
  ('cycle -> enquanto value_list faca code fim_enquanto','cycle',5,'p_cycle2','logic_grammar.py',124),
  ('value -> varName','value',1,'p_value1','logic_grammar.py',130),
  ('value -> bool','value',1,'p_value2','logic_grammar.py',134),
  ('value -> calc','value',1,'p_value2','logic_grammar.py',135),
  ('value -> string','value',1,'p_value2','logic_grammar.py',136),
  ('value -> varName ( value_list )','value',4,'p_value3','logic_grammar.py',140),
  ('value -> varName ( )','value',3,'p_value3','logic_grammar.py',141),
  ('varType -> inteiro','varType',1,'p_varType1','logic_grammar.py',149),
  ('varType -> real','varType',1,'p_varType1','logic_grammar.py',150),
  ('varType -> carater','varType',1,'p_varType1','logic_grammar.py',151),
  ('varType -> logico','varType',1,'p_varType1','logic_grammar.py',152),
  ('varName_list -> varName','varName_list',1,'p_varName_list1','logic_grammar.py',158),
  ('varName_list -> varName_list , varName','varName_list',3,'p_varName_list1','logic_grammar.py',159),
  ('value_list -> value','value_list',1,'p_value_list1','logic_grammar.py',168),
  ('value_list -> value_list , value','value_list',3,'p_value_list1','logic_grammar.py',169),
  ('value_list -> ( value_list )','value_list',3,'p_value_list2','logic_grammar.py',176),
  ('bool -> opt','bool',1,'p_bool1','logic_grammar.py',182),
  ('bool -> value e value','bool',3,'p_bool1','logic_grammar.py',183),
  ('bool -> value ou value','bool',3,'p_bool1','logic_grammar.py',184),
  ('bool -> value xou value','bool',3,'p_bool1','logic_grammar.py',185),
  ('calc -> int','calc',1,'p_calc1','logic_grammar.py',194),
  ('calc -> float','calc',1,'p_calc1','logic_grammar.py',195),
  ('calc -> - value','calc',2,'p_calc1','logic_grammar.py',196),
  ('calc -> value + value','calc',3,'p_calc2','logic_grammar.py',200),
  ('calc -> value - value','calc',3,'p_calc2','logic_grammar.py',201),
  ('calc -> value * value','calc',3,'p_calc2','logic_grammar.py',202),
  ('calc -> value / value','calc',3,'p_calc2','logic_grammar.py',203),
  ('calc -> value < value','calc',3,'p_calc2','logic_grammar.py',204),
  ('calc -> value > value','calc',3,'p_calc2','logic_grammar.py',205),
  ('calc -> value dif value','calc',3,'p_calc2','logic_grammar.py',206),
  ('calc -> value eq value','calc',3,'p_calc2','logic_grammar.py',207),
  ('calc -> value maieq value','calc',3,'p_calc2','logic_grammar.py',208),
  ('calc -> value meneq value','calc',3,'p_calc2','logic_grammar.py',209),
  ('opt -> verdadeiro','opt',1,'p_opt1','logic_grammar.py',215),
  ('opt -> falso','opt',1,'p_opt2','logic_grammar.py',219),
  ('opt -> nao opt','opt',2,'p_opt3','logic_grammar.py',223),
]
