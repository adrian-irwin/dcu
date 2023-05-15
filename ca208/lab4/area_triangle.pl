
% Define an infix binary operator, tA, that is true if the right operand
% is the area of a triangle definfed by the left operand. A triangle A/B
% has a base of A and a perpendicular height of B. For example, the
% clause '6/4 tA X' is true if the value X is 12.


:- op(500, xfy, tA).

Base/Height tA Area :- Area is 0.5*Base*Height.
