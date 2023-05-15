


myElem(X, [X | _]).
myElem(X, [_ | T]) :- myElem(X, T).

myHead(X, [X | _]).

myLast(X, [X]).
myLast(X, [_ | T]) :- myLast(X, T).

myTail(A, [_ | A]).

% true if list C is list B appended onto the end of list A
% myAppend(A, B, C).
myAppend([], L, L).
myAppend([H | T], B, [H | C]):- myAppend(T, B, C).

% true if list A is reverse of list B
% myReverse(A, B).
myReverse([], []).
myReverse([X | T] , Y) :- myReverse(T, T1), myAppend(T1, [X], Y).

% true if list B is list A with first occurance of X removed.
% myDelete(X, A, B).

myDelete(X, [X | T], T).
myDelete(X, [Y | T], [Y | L]) :- myDelete(X, T, L).
