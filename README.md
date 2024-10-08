## Описание задачи

Для манипулятора вывести формулы для определения углов поворота $\theta_1$, $\theta_2$, $\theta_3$ в зависимости от положения ТСР с координатами ($x$, $y$) при условии, что BC остается параллельно оси Ox.

Написать скрипт, в котором на вход принимаются координаты $x$, $y$, длины звеньев $L_1$, $L_2$, $L_3$. Вычисляются углы $\theta_1$, $\theta_2$, $\theta_3$ для достижения заданного положения.

## Решение

Программа состоит из 3 частей (основных):

*calc_ungle* - расчет углов с проверкой на их минимальные и максимальные значения

*coordinate_test_start* - функция проверки на дурака. На случай если вводимые координаты выходят за круг радиуса $R = L_1 + L_2 + L_3$

*coordinate_test_end* - проверка соответствуют ли введеные координаты тем, что получаются при расчете через полученные углы.

Формулы для углов:

Если $x - L_3 = 0$, тогда $\theta_1 = \arcctan( (x - L_3) / y ) - \arccos( (-L_2^2 + L_1^2 + y^2 + (x - L_3)^2) /
(2. * L_1 * \sqrt{( y^2 + (x - L_3)^2 )} ) )$

Если $y = 0$, тогда $\theta_1 = \arctan( y / (x - L_3) ) - \arccos( (-L_2^2 + L_1^2 + y^2 + (x - L_3)^2) /
(2. * L_1 * \sqrt{( y^2 + (x - L_3)^2 )} ) )$

$\theta_2 = \arccos( (y^2 + (x - L_3)^2 - L_2^2 - L_1^2) / 2. / L_1 / L_2 )$

$\theta_3 = \theta_1 + \theta_2$
