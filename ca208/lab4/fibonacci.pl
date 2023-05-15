
% Write a Prolog relation fib(X,Y) that is true if Y is the Fibonacci
% Number of X. The Fibonacci Number of X is the sum of the Fibonacci
% Numbers of (X-1) and (X-2), for X > 1. The Fibonacci Number of 1 is 1
% and the Fibonacci Number of 0 is 1.

fib(0, 0).
fib(1, 1).


fib(X, N) :-X1 is X - 1, X2 is X -2, fib(X1, N1), fib(X2, N2), N is N1 + N2.
