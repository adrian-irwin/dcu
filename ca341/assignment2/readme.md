# CA341 - Assignment 2 - Comparing Functional Programming and Logic

## How to compile/load

### Prolog
To execute the Prolog code, first you must ensure that [SWI-Prolog](https://www.swi-prolog.org/Download.html) is installed on your system.  
Once installed, run SWI-Prolog by typing `swipl` into the terminal.  
Next, type `[compare].` into the terminal to load the program.

### Haskell
To execute the Haskell code, first you must ensure that the [Glasgow Haskell Compiler Interpreter](https://www.haskell.org/downloads/) (GHCi) is installed.  
Once installed, run GHCi by typing `ghci` into the terminal.  
Next type `:load compare.hs` into the terminal to load the program.

## How to use

### Prolog
The format for a binary tree in the Prolog implementations is ***t(Root, Left, Right)*** or ***nil*** for an empty tree.

#### Insert
##### Inserting into an empty tree
To insert an integer A into an empty binary tree, type `insert(A, nil, X).` into the terminal.  
##### Inserting into a given binary tree
If you would like to insert an integer A into a given binary tree Y, type `insert(A, Y, X).` into the terminal

#### Search
To search for an integer A in a binary tree X, type `search(A, X).` into the terminal.  

#### Traversals
##### Preorder
To list the nodes in a given tree X in preorder traversal, type `preorder(X).` into the terminal.
##### Postorder
To list the nodes in a given tree X in postorder traversal, type `preorder(X).` into the terminal.
##### Inorder
To list the nodes in a given tree X in inorder traversal, type `inorder(X).` into the terminal.

#### To exit the program
To exit the program, type `halt.` into the terminal.

### Haskell
The format for a binary tree in the Haskell implementations is ***Root X Left Right*** or ***Empty*** for an empty tree.

#### Insert
##### Inserting into an empty tree
To insert an integer A into an empty binary tree, type `insert A Empty` into the terminal.  
##### Inserting into a given binary tree
If you would like to insert an integer A into a given binary tree Y, type `insert A (Y)` into the terminal

#### Search
To search for an integer A in a binary tree X, type `search A (X)` into the terminal.  

#### Traversals
##### Preorder
To list the nodes in a given tree X in preorder traversal, type `preorder (X)` into the terminal.
##### Postorder
To list the nodes in a given tree X in postorder traversal, type `preorder (X)` into the terminal.
##### Inorder
To list the nodes in a given tree X in inorder traversal, type `inorder (X)` into the terminal.

#### To exit the program
To exit the program, type `:quit` into the terminal.

## Test Cases

### Prolog
#### Insert
```
?- insert(1, nil, X).
X = t(1, nil, nil).

?- insert(1, t(2, nil, nil), X).
X = t(2, t(1, nil, nil), nil).

?- insert(3, t(2, t(1, nil, nil), nil), X).
X = t(2, t(1, nil, nil), t(3, nil, nil)).


?- insert(6, t(2, t(1, nil, nil), t(4, nil, nil)), X).
X = t(2, t(1, nil, nil), t(4, nil, t(6, nil, nil))).

?- insert(12, t(11, t(10, nil, nil), t(13, nil, nil)), X).
X = t(11, t(10, nil, nil), t(13, t(12, nil, nil), nil)).
```

#### Search
```
?- search(1, nil).
false.

?- search(1, t(1, nil, nil)).
true.

?- search(1, t(2, t(1, nil, nil), nil)).
true.

?- search(1, t(2, t(1, nil, nil), t(4, nil, nil))).
true.

?- search(6, t(2, t(1, nil, nil), t(4, nil, nil))).
false.

?- search(12, t(11, t(10, nil, nil), t(13, t(12, nil, nil), nil))).
true.
```

#### Traversals
##### Preorder
```
?- preorder(nil).
true.

?- preorder(t(11, t(10, nil, nil), t(13, t(12, nil, nil), nil))).
11 10 13 12 
true.

?- preorder(t(40 , t(20, t(10, nil, nil), t(30, nil, nil)), t(60, t(50, nil, nil), t(70, nil, nil)))).
40 20 10 30 60 50 70 
true.
```

##### Postorder
```
?- postorder(nil).
true.

?- postorder(t(11, t(10, nil, nil), t(13, t(12, nil, nil), nil))).
10 12 13 11 
true.

?- postorder(t(40 , t(20, t(10, nil, nil), t(30, nil, nil)), t(60, t(50, nil, nil), t(70, nil, nil)))).
10 30 20 50 70 60 40 
true.
```

##### Inorder
```
?- inorder(nil).
true.

?- inorder(t(11, t(10, nil, nil), t(13, t(12, nil, nil), nil))).
10 11 12 13
true.

?- inorder(t(40 , t(20, t(10, nil, nil), t(30, nil, nil)), t(60, t(50, nil, nil), t(70, nil, nil)))).
10 20 30 40 50 60 70 
true.
```

### Haskell
#### Insert
```
*Main> insert 1 Empty
Root 1 Empty Empty

*Main> insert 1 (Root 2 Empty Empty)
Root 2 (Root 1 Empty Empty) Empty

*Main> insert 3 (Root 2 (Root 1 Empty Empty) Empty)
Root 2 (Root 1 Empty Empty) (Root 3 Empty Empty)

*Main> insert 6 (Root 2 (Root 1 Empty Empty) (Root 4 Empty Empty))
Root 2 (Root 1 Empty Empty) (Root 4 Empty (Root 6 Empty Empty))

*Main> insert 12 (Root 11 (Root 10 Empty Empty) (Root 13 Empty Empty))
Root 11 (Root 10 Empty Empty) (Root 13 (Root 12 Empty Empty) Empty)
```

#### Search
```
*Main> search 1 Empty
False

*Main> search 1 (Root 1 Empty Empty)
True

*Main> search 1 (Root 2 (Root 1 Empty Empty) Empty)
True

*Main> search 4 (Root 2 (Root 1 Empty Empty) (Root 4 Empty Empty))
True

*Main> search 6 (Root 2 (Root 1 Empty Empty) (Root 4 Empty Empty))
False

*Main> search 12 (Root 11 (Root 10 Empty Empty) (Root 13 (Root 12 Empty Empty) Empty))
True
```

#### Traversals
##### Preorder
```
*Main> preorder Empty
[]

*Main> preorder (Root 11 (Root 10 Empty Empty) (Root 13 (Root 12 Empty Empty) Empty))
[11,10,13,12]

*Main> preorder (Root 40 (Root 20 (Root 10 Empty Empty) (Root 30 Empty Empty)) (Root 60 (Root 50 Empty Empty) (Root 70 Empty Empty)))
[40,20,10,30,60,50,70]
```

##### Postorder
```
*Main> postorder Empty
[]

*Main> postorder (Root 11 (Root 10 Empty Empty) (Root 13 (Root 12 Empty Empty) Empty))
[10,12,13,11]

*Main> postorder (Root 40 (Root 20 (Root 10 Empty Empty) (Root 30 Empty Empty)) (Root 60 (Root 50 Empty Empty) (Root 70 Empty Empty)))
[10,30,20,50,70,60,40]
```

##### Inorder
```
*Main> inorder Empty
[]

*Main> inorder (Root 11 (Root 10 Empty Empty) (Root 13 (Root 12 Empty Empty) Empty))
[10,11,12,13]

*Main> inorder (Root 40 (Root 20 (Root 10 Empty Empty) (Root 30 Empty Empty)) (Root 60 (Root 50 Empty Empty) (Root 70 Empty Empty)))
[10,20,30,40,50,60,70]
```