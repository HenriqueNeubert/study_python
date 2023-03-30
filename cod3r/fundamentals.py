'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
###operadores aritméticos###
+ 
-
*
/
// resultado sempre inteiro
** elevado
% resto da divisão

###operadores unários###
+= INC
-= DEC
not 1
not 0
+a altera para um número positivo
-a altera para um número negativo

###operadores relacionais###
>  
>=
<
<=
!=
==

###operadores de atribuição###
+= 
-=
*=
/=
%= resto da divisão
**= elevado
//= resultado sempre inteiro

###operadores lógicos###
and
or
xor exclusivamente tem que ser um ou o outro, jamais os dois
not true
not false

###operadores ternários###
esta_chovendo = false
# 'malhadas' está mais perto do [], por isso seria false
# já 'secas', está mais longe, por isso representa true
ex:1
print('Hoje está chovendo ' + ('secas', 'molhadas')[],)
ex2:
print('Hoje está chovendo ' + ('secas', if esta_chovendo else 'secas'))

###operadores de membro###

/////in
lista = [1,2,3,''Ana,'Carla']
2 in lista (true)
'Ana' not in lista (false)

/////is
x = 3
y = x
z = 3

x is y (true)
y is z (true)
x is not z (false\)

listaA = [1,2] 
listaB = listaA
listaC = [1,2]

listaA is listaB (true)
listaB is listaC (false) pq apesar das listas serem iguais, elas não são as mesmas
listaA is not listaC (true) pq apesar das listas serem iguais, elas não são as mesmas

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

