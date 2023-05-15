% Format for the binary tree used throughout the program
% t(Root, Left, Right)

% insert a new node into a binary tree and return the new tree
insert(X, nil, t(X, nil, nil)) :- !. % if the tree is empty, create a new tree with the new node as the root
insert(X, t(Y, L, R), t(Y, L1, R)) :- X < Y, insert(X, L, L1). % insert into left subtree if X is less than Y
insert(X, t(Y, L, R), t(Y, L, R1)) :- X >= Y, insert(X, R, R1). % insert into right subtree if X is greater than or equal to Y

% search for a node in a binary tree
search(X, t(X, _, _)) :- !. % if X is the root, return true
search(X, t(Y, L, _)) :- X < Y, search(X, L), !. % search left subtree if X is less than Y
search(X, t(Y, _, R)) :- X >= Y, search(X, R), !. % search right subtree if X is greater than or equal to Y

% preorder traversal of a binary tree
preorder(nil). % if the tree is empty, do nothing
preorder(t(X, nil, nil)) :- write(X), write(" "), !. % if the tree has no children, write the root and return
preorder(t(X, L, R)) :- write(X), write(" "), preorder(L), preorder(R), !. % write the root, then traverse the left subtree, then traverse the right subtree

% postorder traversal of a binary tree
postorder(nil). % if the tree is empty, do nothing
postorder(t(X, nil, nil)) :- write(X), write(" "), !. % if the tree has no children, write the root and return
postorder(t(X, L, R)) :- postorder(L), postorder(R), write(X), write(" "),!. % traverse the left subtree, then traverse the right subtree, then write the root

% inorder traversal of a binary tree
inorder(nil). % if the tree is empty, do nothing
inorder(t(X, nil, nil)) :- write(X), write(" "), !. % if the tree has no children, write the root and return
inorder(t(X, L, nil)) :- inorder(L), write(X), write(" "), !. % if the tree has no right child, traverse the left subtree, then write the root
inorder(t(X, nil, R)) :- write(X), write(" "), inorder(R), !. % if the tree has no left child, write the root, then traverse the right subtree
inorder(t(X, L, R)) :- inorder(L), write(X), write(" "), inorder(R), !. % if the tree has both children, traverse the left subtree, then write the root, then traverse the right subtree
