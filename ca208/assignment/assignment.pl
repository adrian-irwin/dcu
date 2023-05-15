% Name: Adrian Irwin
% Student Number: 20415624
% I acknowledge that the work submitted in this assignment is my own work and does not breach the DCU Academic Integrity Policy.

% 2-3 Trees
% t(Left, Root, Right)
% t(Left, Root1, Middle, Root2, Right)

% add(X, T1, T2), true if adding X to 2-3 tree T1 generates 2-3 tree T2.
add(X, nil, t(nil, X, nil)).                                    % base case, nil tree, create new tree, X as root

% adding to a 1 root tree with nil children and making a 2-3 tree
add(X, t(nil, Y, nil), t(nil, Y, nil, X, nil)) :- X > Y.
add(X, t(nil, Y, nil), t(nil, X, nil, Y, nil)) :- X =< Y.

% adding to 2-3
add(X, t(L, Y, M, Z, R), t(L1, Y, M, Z, R)) :- X =< Y, add(X, L, L1).
add(X, t(L, Y, M, Z, R), t(L, Y, M1, Z, R)) :- X =< Z, X > Y, add(X, M, M1).
add(X, t(L, Y, M, Z, R), t(L, Y, M, Z, R1)) :- X > Z, add(X, R, R1).


% member(X, T), true if X is a member of 2-3 tree T

member(X, t(_, X, _)).                                          % checks the root, 1 root tree
member(X, t(_, Y, _, Z, _)) :- X =:= Y; X =:= Z.                % checks the roots, 2-3 tree

member(X, t(L, Y, _)) :- X =< Y, member(X, L).                  % checks the left subtree, 1 root tree
member(X, t(_, _, R)) :- member(X, R).                          % checks the right subtree, 1 root tree
member(X, t(L, Y, _, _, _)) :- X =< Y, member(X, L).            % checks the left subtree, 2-3 tree
member(X, t(_, Y, M, Z, _)) :- X > Y, X =< Z ,member(X, M).     % checks the middle subtree, 2-3 tree
member(X, t(_, _, _, Y, R)) :- X > Y, member(X, R).             % checks the right subtree, 2-3 tree


% height(T, N), true if N is the height of 2-3 tree T
height(nil, 0).                                                 % base case, height of empty tree is 0

% height of tree is the max height of its subtrees + 1
height(t(L, _, R), N) :-
    height(L, NL), height(R, NR),
    N is max(NL, NR) + 1.

height(t(L, _, M, _, R) , N) :-
    height(L, NL), height(M, NM), height(R, NR),
    N is max(NL, max(NM, NR)) + 1.


% prettyPrint(T), always true, prints out the tree 2-3 tree T

prettyPrint(nil) :- write("nil").                               % base case, empty tree


prettyPrint(t(L,X,R)) :-
    height(t(L,X,R), H),

    Num is H * 10,

    tab(Num),
    write(X),

    Right is Num - 5,
    nl,

    prettyPrint(L),

    tab(Right),
    prettyPrint(R),

    nl.

prettyPrint(t(L, X, M, Y, R)) :-
    height(t(L, X, M, Y, R), H),

    Num is H * 10,
    tab(Num),
    write(X), write(","), write(Y),

    Mid is Num - 3,
    Right is Num - 5,
    nl,

    prettyPrint(L),

    tab(Mid),
    prettyPrint(M),

    tab(Right),
    prettyPrint(R),

    nl.
