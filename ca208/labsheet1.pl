/* LABSHEET 1 */


/* FACTS */
/* in parents(X,Y,Z), X has parents Y and Z */
/* father first, ALWAYS*/
parents(mike, tom, mary).
parents(jane, tom, mary).
parents(anna,mike,anne).
parents(scott,david,jane).

/* in married(X,Y), X married to Y */
married(tom,mary).
married(mary,tom).
married(mike,anne).
married(anne,mike).
married(jane,david).
married(david,jane).


/* Relationships */


/* X is father of Y IF(:-) parents of Y is X and any other */
father(X, Y) :- parents(Y, X, _).
/* X is male IF(:-) X is father of any */
male(X) :- father(X, _).
/* X is mother of Y IF(:-) parents of Y is X and any other */
mother(X, Y) :- parents(Y, _, X).
/* X is female IF(:-) X is mother of any */
female(X) :- mother(X, _).


/* X is the grandfather of Y, IF(:-) X is the father of Z,
and Z is the father of Y, (Y's father's side) */
grandfather(X, Y) :- father(X, Z), father(Z, Y).
/* X is the grandfather of Y, IF(:-) X is the father of Z,
and Z is the mother of Y, (Y'smother's side) */
grandfather(X, Y) :- father(X, Z), mother(Z, Y).
/* X is the grandmother of Y, IF(:-) X is the mother of Z,
and Z is the mother of Y, (Y's mother's side) */
grandmother(X, Y) :- mother(X, Z), mother(Z, Y).
/* X is the grandmother of Y, IF(:-) X is the mother of Z,
and Z is the father of Y, (Y's father's side) */
grandmother(X, Y) :- mother(X, Z), father(Z, Y).


/* X is the brother of Y IF(:-) X is male and Z is
the father of both X and Y */
brother(X, Y) :- male(X), father(Z, X), father(Z, Y), X \= Y.
/* X is the sister of Y IF(:-) X is female and Z is
the father of both X and Y */
sister(X, Y) :- female(X), father(Z, X), father(Z, Y), X \= Y.



/* X is uncle of Y IF(:-) X is male, Z is father of Y,
X is the brother of Z */
uncle(X, Y) :- male(X), father(Z, Y), brother(X, Z).
/* X is uncle of Y IF(:-) X is male, Z is mother of Y,
and Z is the sister of X*/
uncle(X, Y) :- male(X), mother(Z, Y), sister(Z, X).
/* X is the uncle of Y IF(:-) X is male, X is married to Z,
Z is ZZ brother, and ZZ is father of Y */
uncle(X, Y) :- male(X), married(X, Z), brother(ZZ, Z), father(ZZ, Y).
/* X is the uncle of Y IF(:-) X is male, X is married to Z,
Z is ZZ sister, and ZZ is mother of Y */
uncle(X, Y) :- male(X), married(X, Z), sister(ZZ, Z), mother(ZZ, Y).


/* X is aunt of Y IF(:-) X is female, Z is father of Y,
X is sister of Z */
aunt(X, Y) :- female(X), father(Z, Y), sister(X, Z).
/* X is aunt of Y IF(:-) X is female, Z is mother of Y,
X is sister of Z */
aunt(X, Y) :- female(X), mother(Z, Y), sister(X, Z).
/* X is aunt of Y IF(:-) X is female, X is married to Z,
ZZ is sister of Z, ZZ is mother of Y */
aunt(X, Y) :- female(X), married(X, Z), sister(ZZ, Z), mother(ZZ, Y).
/* X is aunt of Y IF(:-) X is female, X is married to Z,
ZZ is brother of Z, ZZ is father of Y*/
aunt(X,Y) :- female(X), married(X, Z), brother(ZZ, Z), father(ZZ, Y).


/* X is cousin of Y IF(:-) Z is father of X, ZZ is brother of Z,
ZZ is father of Y*/
cousins(X, Y) :- father(Z, X), brother(ZZ, Z), father(ZZ, Y).
/* X is cousin of Y IF(:-) Z is father of X, ZZ is sister of Z,
ZZ is mother of Y*/
cousins(X, Y) :- father(Z, X), sister(ZZ, Z), mother(ZZ, Y).
/* X is cousin of Y IF(:-) Z is mother of X, ZZ is brother of Z,
ZZ is father of Y*/
cousins(X, Y) :- mother(Z, X), brother(ZZ, Z), father(ZZ, Y).
/* X is cousin of Y IF(:-) Z is mother of X, ZZ is sister of Z,
ZZ is mother of Y*/
cousins(X, Y) :- mother(Z, X), sister(ZZ, Z), mother(ZZ, Y).
