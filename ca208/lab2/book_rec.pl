% book(title, author, genre, number_pages).
% genre options = [crime, drama, comedy, study, fiction, reference]

book(illiad, homer, study, 500).
book(c, Richie, study, 150).
book(nt_bible, sams, reference, 480).
book(monty_python, cleese, comedy, 300).
book(pride_and_prejudice, austen, drama, 250).
book(the_big_sleep, chandler, crime, 280).
book(harry_potter, rowling, fiction, 350).

buildLibrary(Lib) :- findall(book(Title, Author, Genre, Size), book(Title, Author,
Genre, Size), Lib).

% books less than 400 pages, not study or reference
is_holiday(book(_, _, Genre, Size)) :- Genre \== study, Genre \== reference, Size < 400.

holiday(Book, [Book | _]) :- is_holiday(Book).
holiday(Book, [_ | T]) :- holiday(Book, T).

% books more than 300 pages, study or reference
is_revision(book(_, _, Genre, Size)) :- Genre == study; Genre == reference, Size > 300.

revision(Book, [Book | _]) :- is_revision(Book).
revision(Book, [_ | T]) :- revision(Book, T).

% drama books
is_literary(book(_, _, Genre, Size)) :- Genre == drama.

literary(Book, [Book | _]):- is_literary(Book).
literary(Book, [_ | T]):- literary(Book, T).

% comedy or fiction books
is_leisure(book(_, _, Genre, Size)) :- Genre == comedy; Genre == fiction.

leisure(Book, [Book | _]) :- is_leisure(Book).
leisure(Book, [_ | T]) :- leisure(Book, T).
