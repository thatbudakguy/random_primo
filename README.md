# random_primo

return metadata of random primo items as JSON. see `book_100_2458.json` for example output.

## usage

```
:~$ ./random_primo.py -h
usage: random_primo.py [-h] [-p url] [-i code] [-n number] [-r type]

Return random Primo records as JSON.

optional arguments:
  -h, --help  show this help message and exit
  -p url      url of primo instance (default: http://primo.lclark.edu/)
  -i code     institution code (default: LCC)
  -n number   number of items to return (default: 100)
  -r type     resource type to return (default: book)
```

to retrieve a random set of 100 books from L&C primo instance (default):

```
:~$ ./random_primo.py
```

to retrieve a random set of 250 ebooks from your primo instance:

```
:~$ ./random_primo.py -p http://myprimo.myschool.edu/ -i MYSCHOOL -n 250 -r ebook
```

## notes

- results have no particular order that I could determine.
- uses the primo "xservice" brief search API - [more info here](https://developers.exlibrisgroup.com/primo/apis/webservices/xservices/search/briefsearch).
- only returns the "display" parameter of the record for brevity, but you could [change that here](https://github.com/thatbudakguy/random_primo/blob/master/random_primo.py#L39).
- currently limited to `book`,`ebook`,`article` resource types because I'm not sure what else works.
- requests with `n > 1000` will get pretty slow. don't know the upper limit.
- picks a random (`k < 10000`) point in the catalog from which to take a slice of size `n`, so overlap is possible.
