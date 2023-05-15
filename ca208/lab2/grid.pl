row1([a, b, c, d, e]).
row2([f, g, h, i, j]).
row3([k, l, m, n, o]).
row4([p, q, r, s, t]).

directly_north(a,f).
directly_north(b,g).
directly_north(c,h).
directly_north(d,i).
directly_north(e,j).
directly_north(f,k).
directly_north(g,l).
directly_north(h,m).
directly_north(i,n).
directly_north(j,o).
directly_north(k,p).
directly_north(l,q).
directly_north(m,r).
directly_north(n,s).
directly_north(o,t).

directly_west(a,b).
directly_west(b,c).
directly_west(c,d).
directly_west(d,e).
directly_west(f,g).
directly_west(g,h).
directly_west(h,i).
directly_west(i,j).
directly_west(k,l).
directly_west(l,m).
directly_west(m,n).
directly_west(n,o).
directly_west(p,q).
directly_west(q,r).
directly_west(r,s).
directly_west(s,t).

directly_south(X, Y) :- directly_north(Y, X).
directly_east(X, Y) :- directly_west(Y, X).

is_due_north(X, Y) :- directly_north(X, Y).
is_due_north(X, Y) :- directly_north(X, Z), is_due_north(Z, Y).

is_due_south(X, Y) :- directly_south(X, Y).
is_due_south(X, Y) :- directly_south(X, Z), is_due_south(Z, Y).

is_due_west(X, Y) :- directly_west(X, Y).
is_due_west(X, Y) :- directly_west(X, Z), is_due_west(Z, Y).

is_due_east(X, Y) :- directly_east(X, Y).
is_due_east(X, Y) :- directly_east(X, Z), is_due_east(Z, Y).

is_due_north_east(X, Y) :- is_due_north(X, Z), is_due_east(Z, Y).

is_due_north_west(X, Y) :- is_due_north(X, Z), is_due_west(Z, Y).

is_due_south_east(X, Y) :- is_due_south(X, Z), is_due_east(Z, Y).

is_due_south_west(X, Y) :- is_due_south(X, Z), is_due_west(Z, Y).
